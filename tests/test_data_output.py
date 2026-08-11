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
            print(node.name)
            i = 0
            while i < len(node.body):
                node.body[i]
                if isinstance(node.body[i], ast.Assert):
                    assert_list.append(ast.unparse(node.body[i])) 
                i += 1
    return assert_list

# **********************************************TESTS**********************************************
file_dir = source_dir / "test_light.py"
assert_list = extract_asserts(file_dir)
print(assert_list)

# output_list = list(output_dir.iterdir())
# output_list.sort()

# source_list = [f for f in source_dir.iterdir() if (f.is_file and f.name.startswith("test_"))]
# source_list.sort()

# for i in range(len(source_list)):
#     print(source_list[i].name)
#     print(output_list[i].name)