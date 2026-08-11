import pytest
from pathlib import Path
from docs_parser.repo_parser import TestScenario
import pydantic 
import json


def _load_all_cases():
    output_dir = Path("shelly_test_outputs").resolve()
    all_cases = []
    for child in output_dir.iterdir():
        with child.open("r") as f:
            cases = json.load(f)
        all_cases.extend(cases)
    return all_cases


@pytest.mark.parametrize("test_case", _load_all_cases(), ids=lambda x: x["name"])
def test_schema_validity(test_case):
    TestScenario.model_validate(test_case)
