import requests
import re
from pydantic import BaseModel, Field
import os
from anthropic import Anthropic 
import ast 
from typing import Any
from pydantic import BaseModel, Field
from dotenv import load_dotenv 

load_dotenv()

CLAUDE_KEY = os.getenv("API_KEY")


client = Anthropic(api_key = CLAUDE_KEY)
tools = []

owner = "home-assistant"
repo = "core"
path = "tests/components/shelly/test_light.py"

url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"


response = requests.get(url)
data = response.json()

print(data["download_url"])

# raw = requests.get(data["download_url"]).text
raw = open("snippet.txt", "r", encoding="utf-8").read()



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

schema = TestScenario.model_json_schema()



tree = ast.parse(raw)
tests = []
lines = raw.splitlines()

for node in tree.body:
    if isinstance(node, ast.AsyncFunctionDef) and node.name.startswith("test_"):
        function_source = "\n".join(
            lines[node.lineno - 1 : node.end_lineno]
        )

        tests.append("name: " + node.name + "\n" + "source: " + function_source + "\n" + "linenum: " + str(node.lineno))

tools = [
    {
        "name": "extract_test_cases",
        "description": "Extract behavioral scenarios from the provided list",
        "input_schema": schema,
    }
]
            
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
        "content": f"Extract all the test case information following the schema provided, from the following list of test cases {tests}" ,
        }
    ],
    model="claude-haiku-4-5",
)

for block in message.content:
    print(block.type)
    if block.type == "tool_use":
        print(block.name)
        print(block.input)
print(message.usage)
