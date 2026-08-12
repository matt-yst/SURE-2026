import pytest
from pathlib import Path
import pydantic 
import json
import ast


# **********************************************CONST DECLARATION**********************************************
output_dir = Path("shelly_test_outputs").resolve()
path = output_dir / "binary_sensor_output.json"

with open(path) as f:
    data = json.load(f)


def test_block_binary_sensor():
    test_case = data[0]
    assert len(test_case["transitions"]) == 2
    assert test_case["transitions"][0]["action"] == "init_integration"
    assert test_case["transitions"][0]["starting_state"] == "initial_state"
    assert test_case["transitions"][0]["ending_state"] == "state_off"
    assert test_case["transitions"][1]["action"] == "set_overpower_and_update"
    assert test_case["transitions"][1]["starting_state"] == "state_off"
    assert test_case["transitions"][1]["ending_state"] == "state_on"
    