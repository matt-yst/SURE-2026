import pytest
from pathlib import Path
import pydantic 
import json
import ast


# **********************************************CONST DECLARATION**********************************************
output_dir = Path("shelly_test_outputs").resolve()


# **********************************************TESTS**********************************************
def test_block_binary_sensor():
    path = output_dir / "binary_sensor_output.json"
    with open(path) as f:
        data = json.load(f)

    test_case = data[0]

    assert len(test_case["transitions"]) == 2
    assert test_case["transitions"][0]["action"] == "init_integration"
    assert test_case["transitions"][0]["starting_state"] == "initial_state"
    assert test_case["transitions"][0]["ending_state"] == "state_off"
    assert test_case["transitions"][1]["action"] == "set_overpower_and_update"
    assert test_case["transitions"][1]["starting_state"] == "state_off"
    assert test_case["transitions"][1]["ending_state"] == "state_on"

@pytest.mark.xfail(reason="this sucks")
def test_block_binary_gas_sensor_creation():
    path = output_dir / "binary_sensor_output.json"
    with open(path) as f:
        data = json.load(f)

    test_case = data[1]

    assert len(test_case["transitions"]) == 2
    assert test_case["transitions"][0]["action"] == "init_integration"
    assert test_case["transitions"][0]["starting_state"] == "initial_state"
    assert test_case["transitions"][0]["ending_state"] == "STATE_ON"
    assert test_case["transitions"][1]["action"] == "setattr"
    assert test_case["transitions"][1]["starting_state"] == "STATE_ON"
    assert test_case["transitions"][1]["ending_state"] == "STATE_OFF"

def test_block_rest_binary_sensor():
    path = output_dir / "binary_sensor_output.json"
    with open(path) as f:
        data = json.load(f)

    test_case = data[2]

    assert len(test_case["transitions"]) == 2
    assert test_case["transitions"][0]["action"] == "init_integration"
    assert test_case["transitions"][0]["starting_state"] == "initial_state"
    assert test_case["transitions"][0]["ending_state"] == "state_1"
    assert test_case["transitions"][1]["action"] == "mock_rest_update"
    assert test_case["transitions"][1]["starting_state"] == "state_1"
    assert test_case["transitions"][1]["ending_state"] == "state_2"

def test_block_rest_binary_sensor_connected_battery_devices():
    path = output_dir / "binary_sensor_output.json"
    with open(path) as f:
        data = json.load(f)

    test_case = data[3]

    assert len(test_case["transitions"]) == 3
    assert test_case["transitions"][0]["action"] == "init_integration"
    assert test_case["transitions"][0]["starting_state"] == "initial_state"
    assert test_case["transitions"][0]["ending_state"] == "state_1"
    assert test_case["transitions"][1]["action"] == "mock_rest_update"
    assert test_case["transitions"][1]["starting_state"] == "state_1"
    assert test_case["transitions"][1]["ending_state"] == "state_2"
    assert test_case["transitions"][2]["action"] == "mock_rest_update"
    assert test_case["transitions"][2]["starting_state"] == "state_2"
    assert test_case["transitions"][2]["ending_state"] == "state_3"

def test_block_sleeping_binary_sensor():
    path = output_dir / "binary_sensor_output.json"
    with open(path) as f:
        data = json.load(f)

    test_case = data[4]

    assert len(test_case["transitions"]) == 3
    assert test_case["transitions"][0]["action"] == "init_integration"
    assert test_case["transitions"][0]["starting_state"] == "initial_state"
    assert test_case["transitions"][0]["ending_state"] == "state_1"
    assert test_case["transitions"][1]["action"] == "async_block_till_done"
    assert test_case["transitions"][1]["starting_state"] == "state_1"
    assert test_case["transitions"][1]["ending_state"] == "state_2"
    assert test_case["transitions"][2]["action"] == "mock_update"
    assert test_case["transitions"][2]["starting_state"] == "state_2"
    assert test_case["transitions"][2]["ending_state"] == "state_3"

def test_block_restored_sleeping_binary_sensor():
    path = output_dir / "binary_sensor_output.json"
    with open(path) as f:
        data = json.load(f)

    test_case = data[5]

    assert len(test_case["transitions"]) == 2
    assert test_case["transitions"][0]["action"] == "hass.config_entries.async_setup"
    assert test_case["transitions"][0]["starting_state"] == "initial_state"
    assert test_case["transitions"][0]["ending_state"] == "STATE_ON"
    assert test_case["transitions"][1]["action"] == "mock_block_device.mock_online"
    assert test_case["transitions"][1]["starting_state"] == "STATE_ON"
    assert test_case["transitions"][1]["ending_state"] == "STATE_OFF"