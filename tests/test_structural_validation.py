import pytest
from pathlib import Path
from docs_parser.repo_parser import TestScenario
import pydantic 
import json


output_dir = Path("shelly_test_outputs").resolve()


def _load_cases():
    path = Path(__file__).resolve().parents[1] / "shelly_test_outputs" / "event_output.json"
    with path.open() as f:
        return json.load(f)

@pytest.mark.parametrize("test_case", _load_cases(), ids=lambda x: x["name"])
def test_schema_validity(test_case):
    TestScenario.model_validate(test_case)

# for child in output_dir.iterdir():
#     with open(child, 'r') as f:
#         test_cases = json.load(f)
#     print(test_cases)

    # @pytest.mark.parametrize("test_case", test_cases, ids=lambda x: x["name"])
    # def test_schema_validity(test_case):
    #     TestScenario.model_validate(test_case)
