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

load_dotenv()

CLAUDE_KEY = os.getenv("API_KEY")


client = Anthropic(api_key = CLAUDE_KEY)
tools = []

path = Path(".core-dev/tests/components/shelly/test_light.py")


with path.open("r") as file:
    raw = file.read()

# with open("snippet.txt", "r") as file:
#     raw = file.read()

class State(BaseModel):
    variables: dict[str, Any] = Field(
        description="Dictionary of observable state variables."
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

schema = TestFile.model_json_schema()
# schema_json = json.dumps(schema, indent=2)

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
            if not isinstance(node.body[i], ast.Assert):
                behaviour.append(ast.unparse(node.body[i])) 
                i += 1
            else:
                curr = {"snapshot": []}
                while i < len(node.body) and isinstance(node.body[i], ast.Assert):
                    curr["snapshot"].append(ast.unparse(node.body[i].test))
                    i +=  1
                behaviour.append(curr)


        # print(node.body)
        tests.append("name: " + node.name + "\n" + "behaviour: " + str(behaviour) + "\n" + "linenum: " + str(node.lineno))

# with open("test.txt", "w") as f:
#     for test in tests:
#         f.write(test + "\n\n")  # extra blank line between entries

print("\n")
print("********************************************************************************************************")
print("\n")

tools = [
    {
        "name": "extract_test_cases",
        "description": "Extract behavioral scenarios from the provided list",
        "input_schema": schema,
    }
]

for i in range(2):
    message = client.messages.create(
        max_tokens=1000,
        tools = tools,
        tool_choice = {
            "type": "tool",
            "name": "extract_test_cases",
        },
        messages=[
            {
            "role": "user",
            "content": f"Extract all the test case information following the schema provided, from the following list of test cases {tests[i]}" ,
            }
        ],
        model="claude-haiku-4-5",
    )

    for block in message.content:
        print(block.type)
    if block.type == "tool_use":
        print(block.name)
        print(block.input)


# print(message.usage)
