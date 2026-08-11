import pytest
from pathlib import Path
# from docs_parser.repo_parser import TestScenario
import pydantic 
import json


def test_try():
    assert True


# def _load_cases():
#     path = Path(__file__).resolve().parents[1] / "shelly_test_outputs" / "event_output.json"
#     with path.open() as f:
#         return json.load(f)

# @pytest.mark.parametrize("test_case", _load_cases(), ids=lambda x: x["name"])
# def test_schema_validity(test_case):
#     TestScenario.model_validate(test_case)

# for child in output_dir.iterdir():
#     print(child.name)
#     print("\n")
#     with open(path, 'r') as f:
#         test_cases = json.load(f)

#     @pytest.mark.parametrize("test_case", test_cases, ids=lambda x: x["name"])
#     def test_schema_validity(test_case):
#         TestScenario.model_validate(test_case)
