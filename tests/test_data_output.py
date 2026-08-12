import pytest
from pathlib import Path
import pydantic 
import json
import ast

# **********************************************CONST DECLARATION**********************************************
output_dir = Path("shelly_test_outputs").resolve()
source_dir = Path("test_data_output.py").resolve().parent.parent / "core" / "tests" / "components" / "shelly"

# **********************************************FUNTCION DEFS**********************************************
def extract_asserts(file_dir):
    with file_dir.open("r") as f:
        raw = f.read()
    tree = ast.parse(raw)
    assert_list = []

    for node in tree.body:
        if isinstance(node, ast.AsyncFunctionDef) and node.name.startswith("test_"):
            i = 0
            while i < len(node.body):
                if isinstance(node.body[i], ast.Assert):
                    curr = {"snapshot": []}
                    while i < len(node.body) and isinstance(node.body[i], ast.Assert):
                        curr_assert = ast.unparse(node.body[i].test)
                        curr["snapshot"].append(curr_assert)     
                        i +=  1
                    assert_list.append(curr)
                i += 1
    return assert_list

def extract_snapshots(data):
    output = []
    for test in data:
        for key, value in test["states"].items():
            snapshot = {"snapshot": []}
            if not key == "initial_state":
                snapshot["snapshot"].append({key : value})
            output.append(snapshot)
    return output

# **********************************************TESTS**********************************************
file_dir = source_dir / "test_light.py"
assert_list = extract_asserts(file_dir)

output_file = output_dir / "light_output.json"

with open(output_file) as f:
    data = json.load(f)

print(extract_snapshots(data))
print("\n")
print("********************************************************************************************************")
print("\n")
print(assert_list)