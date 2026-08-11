import pytest
from pathlib import Path
from docs_parser.repo_parser import TestScenario
import pydantic 


output_dir = Path("shelly_test_outputs").resolve()
for child in output_dir.iterdir():
    test_cases = child.read_text()

    print(test_cases)
    print("\n")
    print("********************************************************************************************************")
    print("\n")

    @pytest.mark.parametrize("test_case", test_cases)
    def test_schema_validity(test_case):
        pass