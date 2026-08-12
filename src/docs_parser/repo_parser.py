import requests
import re
import json
from pydantic import BaseModel, Field
import os
from anthropic import Anthropic 
import ast 
from typing import Any
from pydantic import BaseModel, Field
from dotenv import load_dotenv 
from pathlib import Path
from ollama import chat

# **********************************************DECLARATIONS**********************************************

# file declaration
script_dir = Path("repo_parser.py").resolve().parent
component_dir = script_dir.parent / "core" / "tests" / "components" / "hue"



# schema declaratrion
class State(BaseModel):
    variables: dict[str, str] = Field(
        description="Dictionary of observable state variables. State variables meant to be extracted from the snapshot entries. Translate the names of the asserted variables and the state names to more common terms, like the examples given",
        examples = ["""{
                        "state": "on",
                        "color_mode": "rgbw",
                        "rgbw_color": [
                            70,
                            80,
                            90,
                            30
                        ],
                        "brightness": 33,
                        "effect": "Flash"
                    }
                    """,
                    """
                    {
                        "state": "on",
                        "color_mode": "color_temp",
                        "color_temp_kelvin": 3500,
                        "unique_id": "123456789ABC-light_0"
                    }
                    """
                    ]
    )


class Transition(BaseModel):
    action: str = Field(
        description="Action invoked in the test. Translate the proprietary terms to common terms, 'SERVICE_TURN_OFF' to 'off' for example. If an initial state is not explicitly defined, assume it to be called 'initial_state' with no variables to assert"
)
    starting_state : str = Field(
        description="State before the action."
    )
    ending_state : str = Field(
        description="State after the action."
    )
    inputs: dict[str, Any] = Field(
        default_factory=dict,
        description="Input parameters supplied to the action."
    )


class TestScenario(BaseModel):
    name: str = Field(
        description = "Name of the test scenario. To be extracted from the function name of the test case.",
        examples = ["test_block_device_white_bulb", "test_rpc_light"]
    )
    device_type: str = Field(
        description = "The type of device being tested. To be extracted from the test case name or the source code.",
        examples = ["light", "switch", "light_white", "light_rgbw"]
    )
    states: dict[str, State]
    transitions: list[Transition]

class TestFile(BaseModel):
    test_scenarios: list[TestScenario] = Field(
        description = "List of test scenarios extracted from the test file."
    )

schema = TestScenario.model_json_schema()

# **********************************************FUNTCION DEFS**********************************************
def extract_input_data(tree, tests, assert_types):
    num = 0
    for node in tree.body:
        if isinstance(node, ast.AsyncFunctionDef) and node.name.startswith("test_"):
            print(node.name)
            num += 1
            behaviour = []
            i = 0
            while i < len(node.body):
                if not isinstance(node.body[i], ast.Assert):
                    behaviour.append(ast.unparse(node.body[i])) 
                    i += 1
                else:
                    curr_assert = ast.parse(node.body[i])
                    assert_types.add(curr_assert.test.__class__.__name__)
                    curr = {"snapshot": []}
                    while i < len(node.body) and isinstance(node.body[i], ast.Assert):
                        comparison = node.body[i].test
                        if isinstance(comparison, ast.Compare):
                            left = ast.unparse(comparison.left)
                            right = ast.unparse(comparison.comparators[0])
                            curr["snapshot"].append({left: right})     
                        i +=  1
                    behaviour.append(curr)

            tests.append("name: " + node.name + "\n" + "behaviour: " + str(behaviour) + "\n" + "linenum: " + str(node.lineno))

    print("number of functions: " + str(num))
    return num

def LLM_prompt(prompt, output):
    response = chat(
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ],
        model="gpt-oss:120b",
        format = schema
    )
    curr = json.loads(response.message.content)
    output.append(curr)
    return output

def print_files(dir, indent):
    indent_str = "      " * indent
    for child in dir.iterdir():
        if child.is_file():
            print(indent_str + child.name)
        if child.is_dir():
            print(indent_str + child.name)
            print_files(child, indent + 1)

# **********************************************CODE PROCEDURE**********************************************
if __name__ == "__main__":
    print("FILES IN COMPONENT DIRECTORY: ")
    print_files(component_dir, 0)

    output_folder = script_dir / "hue_test_outputs"
    output_folder.mkdir(exist_ok=True)

    print("\n")
    print("********************************************************************************************************")
    print("\n")
    no_of_tests = 0
    j = 0
    for child in component_dir.iterdir():
        if child.is_file() and child.name.startswith("test_") and child.name.endswith(".py") and j < 1:
            path = child
            output_name = child.stem.removeprefix("test_") + "_output.json"
            output_file = output_folder / output_name
            output_file.touch(exist_ok=True)
        
            output_file = open(output_file, "w")

            print(f"Processing file: {path.name}")
            print("\n")

            #THE BULLSHIT IS HERE
            with path.open("r") as file:
                raw = file.read()

            print(raw)

            tree = ast.parse(raw)
            tests = []
            output_json = []
            assert_types = {""}

            print("INPUT TESTS: ")
            print("\n")
            no_of_tests += extract_input_data(tree, tests, assert_types)


            print("\n")
            print("********************************************************************************************************")
            print("\n")



            # for i in range(len(tests)):
            #     print(tests[i])
            #     print("\n")
            #     print("********************************************************************************************************")
            #     print("\n")

            #     prompt = f"""Extract all the test case information following the schema provided, from the following list of test cases {tests[i]}.
            #     Utilise the schema in the provided format
            #     'name' is the name of the test function
            #     'device_type' is the type of device being tested, meant to be extracted from the test case name or source code.
            #     'states' are defined as the snapshot asserts within the test case behaviour. Extract all the listed entries within the snapshot dictionary objects to be the entries in the "variables" field of the state object.
            #     'transitions' are the actions moving from one state to another, the 'starting_state' and 'ending_state'. The 'action' is the action involved with the state transition, and 'inputs' are the parameters of the action. the statring and ending sattes must be defined in the 'states' field, and the other information must be taken from the behaviour field of the 'tests' list. 

            #     If you find that an initialisation state is not explicityly defined by asserts but a transition action is present (let's say an initiialisation function is called for example), you can assume the initial state has no variables to assert. However, do name this null state as "initial_state" in the list of transitions
            #     """

            #     output = LLM_prompt(prompt, output_json)
            # output_file.write(json.dumps(output, indent=4))
            print(assert_types)
            j += 1

    print("total number of tests: " + str(no_of_tests))
