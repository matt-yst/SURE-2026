import pytest
from pathlib import Path
from docs_parser.repo_parser import TestScenario
import pydantic 
import json


shelly_dir = Path("shelly_test_outputs").resolve()
elgato_dir = Path("elgato_test_outputs").resolve()
hue_dir = Path("hue_test_outputs").resolve()

def load_all_cases(output_dir):
    all_cases = []
    for child in output_dir.iterdir():
        with child.open("r") as f:
            cases = json.load(f)
        all_cases.extend(cases)
    return all_cases


@pytest.mark.parametrize("test_case", load_all_cases(shelly_dir), ids=lambda x: x["name"])
def test_shelly_schema_validity(test_case):
    TestScenario.model_validate(test_case)

@pytest.mark.parametrize("test_case", load_all_cases(hue_dir), ids=lambda x: x["name"])
def test_hue_schema_validity(test_case):
    TestScenario.model_validate(test_case)

@pytest.mark.parametrize("test_case", load_all_cases(elgato_dir), ids=lambda x: x["name"])
def test_elgato_schema_validity(test_case):
    TestScenario.model_validate(test_case)