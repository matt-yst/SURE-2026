import pytest
from pathlib import Path
import pydantic 
import json
import ast


# **********************************************TESTS**********************************************

class Test_shelly_binary_sensor():
    def setup_method(self):
        output_dir = Path("shelly_test_outputs").resolve()
        path = output_dir / "binary_sensor_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_block_binary_sensor_length(self):
        test_case = self.data[0]
        assert len(test_case["transitions"]) == 2

    @pytest.mark.xfail(reason="wrong number of transitions")
    def test_block_binary_gas_sensor_creation_length(self):
        test_case = self.data[1]

        assert len(test_case["transitions"]) == 2

    def test_block_rest_binary_sensor_length(self):
        test_case = self.data[2]

        assert len(test_case["transitions"]) == 2


    def test_block_rest_binary_sensor_connected_battery_devices_length(self):
        test_case = self.data[3]

        assert len(test_case["transitions"]) == 3

    def test_block_sleeping_binary_sensor_length(self):
        test_case = self.data[4]

        assert len(test_case["transitions"]) == 3

    def test_block_restored_sleeping_binary_sensor_length(self):
        test_case = self.data[5]

        assert len(test_case["transitions"]) == 2

    def test_block_restored_sleeping_binary_sensor_no_last_state_length(self):
        test_case = self.data[6]

        assert len(test_case["transitions"]) == 2

    @pytest.mark.xfail(reason="wrong number of transitions")
    def test_rpc_binary_sensor_length(self):
        test_case = self.data[7]

        assert len(test_case["transitions"]) == 2

    def test_rpc_binary_sensor_input_custom_name_length(self):
        test_case = self.data[8]

        assert len(test_case["transitions"]) == 1

    def test_rpc_binary_sensor_removal_length(self):
        test_case = self.data[9]

        assert len(test_case["transitions"]) == 2

    def test_rpc_sleeping_binary_sensor_length(self):
        test_case = self.data[10]

        assert len(test_case["transitions"]) == 3

    def test_rpc_sleeping_binary_sensor_with_channel_name_length(self):
        test_case = self.data[11]

        assert len(test_case["transitions"]) == 3

    def test_rpc_restored_sleeping_binary_sensor_length(self):
        test_case = self.data[12]

        assert len(test_case["transitions"]) == 2

    @pytest.mark.xfail(reason="wrong number of transitions")
    def test_rpc_restored_sleeping_binary_sensor_no_last_state_length(self):
        test_case = self.data[13]

        assert len(test_case["transitions"]) == 2

    def test_rpc_device_virtual_binary_sensor_length(self):
        test_case = self.data[14]

        assert len(test_case["transitions"]) == 2

class Test_hue_binary_sensor():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "binary_sensor_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    @pytest.mark.xfail(reason="wrong number of transitions")
    def test_binary_sensors_length(self):
        test_case = self.data[0]

        assert len(test_case["transitions"]) == 10

    def test_binary_sensor_add_update_length(self):
        test_case = self.data[1]

        assert len(test_case["transitions"]) == 4

    def test_grouped_motion_sensor_length(self):
        test_case = self.data[2]

        assert len(test_case["transitions"]) == 3

    def test_motion_aware_sensor_length(self):
        test_case = self.data[3]

        assert len(test_case["transitions"]) == 3

class Test_hue_bridge():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "bridge_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_bridge_setup_v1_length(self):
        test_case = self.data[0]

        assert len(test_case["transitions"]) == 2

    def test_bridge_device_v1_length(self):
        test_case = self.data[1]

        assert len(test_case["transitions"]) == 3

    def test_bridge_device_v2_length(self):
        test_case = self.data[2]

        assert len(test_case["transitions"]) == 2

    @pytest.mark.xfail(reason="1 extra transition(s)")
    def test_bridge_setup_v2_length(self):
        test_case = self.data[3]

        assert len(test_case["transitions"]) == 2

    def test_bridge_setup_invalid_api_key_length(self):
        test_case = self.data[4]

        assert len(test_case["transitions"]) == 1

    def test_bridge_setup_timeout_length(self):
        test_case = self.data[5]

        assert len(test_case["transitions"]) == 1

    def test_reset_unloads_entry_if_setup_length(self):
        test_case = self.data[6]

        assert len(test_case["transitions"]) == 2

    @pytest.mark.xfail(reason="1 extra transition(s)")
    def test_handle_unauthorized_length(self):
        test_case = self.data[7]

        assert len(test_case["transitions"]) == 1

class Test_hue_device_trigger_v1():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "device_trigger_v1_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_get_triggers_length(self):
        test_case = self.data[0]

        assert len(test_case["transitions"]) == 3

    def test_if_fires_on_state_change_length(self):
        test_case = self.data[1]

        assert len(test_case["transitions"]) == 3

class Test_hue_device_trigger_v2():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "device_trigger_v2_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_hue_event_length(self):
        test_case = self.data[0]

        assert len(test_case["transitions"]) == 1

class Test_elgato_button():
    def setup_method(self):
        output_dir = Path("elgato_test_outputs").resolve()
        path = output_dir / "button_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_button_length(self):
        test_case = self.data[0]

        assert len(test_case["transitions"]) == 5

class Test_elgato_config_flow():
    def setup_method(self):
        output_dir = Path("elgato_test_outputs").resolve()
        path = output_dir / "config_flow_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_full_user_flow_implementation_length(self):
        test_case = self.data[0]

        assert len(test_case["transitions"]) == 3

    def test_full_zeroconf_flow_implementation_length(self):
        test_case = self.data[1]

        assert len(test_case["transitions"]) == 4

    def test_connection_error_length(self):
        test_case = self.data[2]

        assert len(test_case["transitions"]) == 3

    @pytest.mark.xfail(reason="1 extra transition(s)")
    def test_zeroconf_connection_error_length(self):
        test_case = self.data[3]

        assert len(test_case["transitions"]) == 1

    def test_user_device_exists_abort_length(self):
        test_case = self.data[4]

        assert len(test_case["transitions"]) == 1

    def test_zeroconf_device_exists_abort_length(self):
        test_case = self.data[5]

        assert len(test_case["transitions"]) == 4

    def test_zeroconf_during_onboarding_length(self):
        test_case = self.data[6]

        assert len(test_case["transitions"]) == 2

    def test_dhcp_discovery_updates_host_length(self):
        test_case = self.data[7]

        assert len(test_case["transitions"]) == 1

    def test_dhcp_discovery_same_host_length(self):
        test_case = self.data[8]

        assert len(test_case["transitions"]) == 1

    def test_dhcp_discovery_no_match_length(self):
        test_case = self.data[9]

        assert len(test_case["transitions"]) == 1

    def test_reconfigure_flow_length(self):
        test_case = self.data[10]

        assert len(test_case["transitions"]) == 3

    def test_reconfigure_flow_cannot_connect_length(self):
        test_case = self.data[11]

        assert len(test_case["transitions"]) == 2

    def test_reconfigure_flow_different_device_length(self):
        test_case = self.data[12]

        assert len(test_case["transitions"]) == 3

class Test_elgato_light():
    def setup_method(self):
        output_dir = Path("elgato_test_outputs").resolve()
        path = output_dir / "light_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_light_state_temperature_length(self):
        test_case = self.data[0]

        assert len(test_case["transitions"]) == 0

    def test_light_change_state_temperature_length(self):
        test_case = self.data[1]

        assert len(test_case["transitions"]) == 4