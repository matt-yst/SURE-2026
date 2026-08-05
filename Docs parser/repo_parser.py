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

# API declaration 
# load_dotenv()
# CLAUDE_KEY = os.getenv("API_KEY")
# client = Anthropic(api_key = CLAUDE_KEY)


# file declaration
tools = []

script_dir = Path("repo_parser.py").resolve().parent
path = script_dir.parent / "core" / "tests" / "components" / "shelly" / "test_light.py"

output_file = open("output4.txt", "w")



with path.open("r") as file:
    raw = file.read()

# schema declaratrion
class State(BaseModel):
    variables: dict[str, str] = Field(
        description="Dictionary of observable state variables. State variables meant to be extracted from the snapshot entries.",
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
        description="Action invoked in the test. Translate the proprietary terms to common terms, 'SERVICE_TURN_OFF' to 'off' for example"
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
# schema_json = json.dumps(schema, indent=4)


# **********************************************CODE PROCEDURE**********************************************
tree = ast.parse(raw)
tests = []
lines = raw.splitlines()

print("input tests: ")

for node in tree.body:
    if isinstance(node, ast.AsyncFunctionDef) and node.name.startswith("test_"):
        print(node.name)
        behaviour = []
        i = 0
        while i < len(node.body):
            line = node.body[i]
            if not isinstance(line, ast.Assert):
                behaviour.append(ast.unparse(line)) 
                i += 1
            else:
                curr = {"snapshot": []}
                while i < len(node.body) and isinstance(line, ast.Assert):
                    comparison = line.test
                    if isinstance(comparison, ast.Compare):
                        left = ast.unparse(comparison.left)
                        right = ast.unparse(comparison.comparators[0])
                        curr["snapshot"].append({left: right})      
                    i +=  1
                behaviour.append(curr)


        # print(node.body)
        tests.append("name: " + node.name + "\n" + "behaviour: " + str(behaviour) + "\n" + "linenum: " + str(node.lineno))



print("\n")
print("********************************************************************************************************")
print("\n")

output = []

tools = [
    {
        "name": "extract_test_cases",
        "description": "Extract behavioral scenarios from the provided list",
        "input_schema": schema,
    }
]

for i in range(1):
    # message = client.messages.create(
    #     max_tokens=1000,
    #     tools = tools,
    #     tool_choice = {
    #         "type": "tool",
    #         "name": "extract_test_cases",
    #     },
    #     messages=[
    #         {
    #         "role": "user",
    #         "content": f"Extract all the test case information following the schema provided, from the following list of test cases {tests[i]}" ,
    #         }
    #     ],
    #     model="claude-haiku-4-5",
    # )

    print(tests[i])
    print("\n")
    print("********************************************************************************************************")
    print("\n")


    prompt = f"""Extract all the test case information following the schema provided, from the following list of test cases {tests[i]}.
    Utilise the schema in the provided format
    'name' is the name of the test function
    'device_type' is the type of device being tested, meant to be extracted from the test case name or source code.
    'states' are defined as the snapshot asserts within the test case behaviour. Extract all the listed entries within the snapshot dictionary objects to be the entries in the "variables" field of the state object.
    'transitions' are the actions moving from one state to another, the 'starting_state' and 'ending_state'. The 'action' is the action involved with the state transition, and 'inputs' are the parameters of the action. the statring and ending sattes must be defined in the 'states' field, and the other information must be taken from the behaviour field of the 'tests' list. 

    """

#     response = chat(
#         messages=[
#             {
#                 'role': 'user',
#                 'content': prompt
#             }
#         ],
#         model="gpt-oss:120b",
#         format = schema
#     )
#     # print(response.message.content)
#     curr = json.loads(response.message.content)
#     output.append(curr)

# #     for block in response.message.content:
# #         # print(block.type)
# #         if block.type == "tool_use":
# #         # print(block.name)
# #             # print(block.input)
# #             output.test_scenarios.append(block.input)

# # print(json.dumps(output.model_dump(), indent=4))
# output_file.write(json.dumps(output, indent=4))

# print(message.usage)
