import pytest
from pathlib import Path 
import json



# **********************************************TESTS**********************************************
class Test_shelly_binary_sensor():
    def setup_method(self):
        output_dir = Path("shelly_test_outputs").resolve()
        path = output_dir / "binary_sensor_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_block_binary_sensor_0(self):
        test_case = self.data[0]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_off"

    def test_block_binary_sensor_1(self):
        test_case = self.data[0]

        assert test_case["transitions"][1]["action"] == "set_overpower_and_update"
        assert test_case["transitions"][1]["starting_state"] == "state_off"
        assert test_case["transitions"][1]["ending_state"] == "state_on"


    def test_block_binary_gas_sensor_creation_0(self):
        test_case = self.data[1]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "STATE_ON"

    def test_block_binary_gas_sensor_creation_1(self):
        test_case = self.data[1]

        assert test_case["transitions"][1]["action"] == "setattr"
        assert test_case["transitions"][1]["starting_state"] == "STATE_ON"
        assert test_case["transitions"][1]["ending_state"] == "STATE_OFF"


    def test_block_rest_binary_sensor_0(self):
        test_case = self.data[2]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_block_rest_binary_sensor_1(self):
        test_case = self.data[2]

        assert test_case["transitions"][1]["action"] == "mock_rest_update"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"



    def test_block_rest_binary_sensor_connected_battery_devices_0(self):
        test_case = self.data[3]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_block_rest_binary_sensor_connected_battery_devices_1(self):
        test_case = self.data[3]

        assert test_case["transitions"][1]["action"] == "mock_rest_update"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_block_rest_binary_sensor_connected_battery_devices_2(self):
        test_case = self.data[3]

        assert test_case["transitions"][2]["action"] == "mock_rest_update"
        assert test_case["transitions"][2]["starting_state"] == "state_2"
        assert test_case["transitions"][2]["ending_state"] == "state_3"


    def test_block_sleeping_binary_sensor_0(self):
        test_case = self.data[4]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_block_sleeping_binary_sensor_1(self):
        test_case = self.data[4]
        assert test_case["transitions"][1]["action"] == "async_block_till_done"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_block_sleeping_binary_sensor_2(self):
        test_case = self.data[4]
        assert test_case["transitions"][2]["action"] == "mock_update"
        assert test_case["transitions"][2]["starting_state"] == "state_2"
        assert test_case["transitions"][2]["ending_state"] == "state_3"


    def test_block_restored_sleeping_binary_sensor_0(self):
        test_case = self.data[5]   
        assert test_case["transitions"][0]["action"] == "hass.config_entries.async_setup"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "STATE_ON"

    def test_block_restored_sleeping_binary_sensor_1(self):
        test_case = self.data[5]
        assert test_case["transitions"][1]["action"] == "mock_block_device.mock_online"
        assert test_case["transitions"][1]["starting_state"] == "STATE_ON"
        assert test_case["transitions"][1]["ending_state"] == "STATE_OFF"

    def test_block_restored_sleeping_binary_sensor_no_last_state_0(self):
        test_case = self.data[6]

        assert test_case["transitions"][0]["action"] == "async_setup"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_unknown"

    def test_block_restored_sleeping_binary_sensor_no_last_state_1(self):
        test_case = self.data[6]

        assert test_case["transitions"][1]["action"] == "mock_online"
        assert test_case["transitions"][1]["starting_state"] == "state_unknown"
        assert test_case["transitions"][1]["ending_state"] == "state_off"

    def test_rpc_binary_sensor_0(self):
        test_case = self.data[7]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_rpc_binary_sensor_1(self):
        test_case = self.data[7]

        assert test_case["transitions"][1]["action"] == "mutate_rpc_device_status"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_rpc_binary_sensor_input_custom_name_0(self):
        test_case = self.data[8]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_on"

    def test_rpc_binary_sensor_removal_0(self):
        test_case = self.data[9]

        assert test_case["transitions"][0]["action"] == "register_entity"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_rpc_binary_sensor_removal_1(self):
        test_case = self.data[9]

        assert test_case["transitions"][1]["action"] == "init_integration"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_rpc_sleeping_binary_sensor_0(self):
        test_case = self.data[10]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_rpc_sleeping_binary_sensor_1(self):
        test_case = self.data[10]

        assert test_case["transitions"][1]["action"] == "register_entity_and_online"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_rpc_sleeping_binary_sensor_2(self):
        test_case = self.data[10]

        assert test_case["transitions"][2]["action"] == "mutate_and_update"
        assert test_case["transitions"][2]["starting_state"] == "state_2"
        assert test_case["transitions"][2]["ending_state"] == "state_3"

    def test_rpc_sleeping_binary_sensor_with_channel_name_0(self):
        test_case = self.data[11]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "no_entity"

    def test_rpc_sleeping_binary_sensor_with_channel_name_1(self):
        test_case = self.data[11]

        assert test_case["transitions"][1]["action"] == "mock_online"
        assert test_case["transitions"][1]["starting_state"] == "no_entity"
        assert test_case["transitions"][1]["ending_state"] == "idle_off"

    def test_rpc_sleeping_binary_sensor_with_channel_name_2(self):
        test_case = self.data[11]

        assert test_case["transitions"][2]["action"] == "set_alarm"
        assert test_case["transitions"][2]["starting_state"] == "idle_off"
        assert test_case["transitions"][2]["ending_state"] == "alarm_on"

    def test_rpc_restored_sleeping_binary_sensor_0(self):
        test_case = self.data[12]

        assert test_case["transitions"][0]["action"] == "mock_restore_cache"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "STATE_ON"

    def test_rpc_restored_sleeping_binary_sensor_1(self):
        test_case = self.data[12]

        assert test_case["transitions"][1]["action"] == "mock_rpc_device.mock_update"
        assert test_case["transitions"][1]["starting_state"] == "STATE_ON"
        assert test_case["transitions"][1]["ending_state"] == "STATE_OFF"

    def test_rpc_restored_sleeping_binary_sensor_no_last_state_0(self):
        test_case = self.data[13]

        assert test_case["transitions"][0]["action"] == "setup_entry"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "STATE_UNKNOWN"

    def test_rpc_restored_sleeping_binary_sensor_no_last_state_1(self):
        test_case = self.data[13]

        assert test_case["transitions"][1]["action"] == "restore_device"
        assert test_case["transitions"][1]["starting_state"] == "STATE_UNKNOWN"
        assert test_case["transitions"][1]["ending_state"] == "STATE_OFF"

    def test_rpc_device_virtual_binary_sensor_0(self):
        test_case = self.data[14]

        assert test_case["transitions"][0]["action"] == "init_integration"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_rpc_device_virtual_binary_sensor_1(self):
        test_case = self.data[14]

        assert test_case["transitions"][1]["action"] == "update_status"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

class Test_hue_binary_sensor():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "binary_sensor_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_binary_sensors_0(self):
        test_case = self.data[0]

        assert test_case["transitions"][0]["action"] == "load_test_data & setup_platform"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "post_setup"

    def test_binary_sensors_1(self):
        test_case = self.data[0]

        assert test_case["transitions"][1]["action"] == "emit_event"
        assert test_case["transitions"][1]["starting_state"] == "test_contact_sensor_opening_created"
        assert test_case["transitions"][1]["ending_state"] == "test_contact_sensor_opening_unknown"

    def test_binary_sensors_2(self):
        test_case = self.data[0]

        assert test_case["transitions"][2]["action"] == "emit_event"
        assert test_case["transitions"][2]["starting_state"] == "test_contact_sensor_tamper_created"
        assert test_case["transitions"][2]["ending_state"] == "test_contact_sensor_tamper_after_update"

    def test_binary_sensor_add_update_0(self):
        test_case = self.data[1]

        assert test_case["transitions"][0]["action"] == "emit_event"
        assert test_case["transitions"][0]["starting_state"] == "state0"
        assert test_case["transitions"][0]["ending_state"] == "state1"

    def test_binary_sensor_add_update_1(self):
        test_case = self.data[1]

        assert test_case["transitions"][1]["action"] == "emit_event"
        assert test_case["transitions"][1]["starting_state"] == "state1"
        assert test_case["transitions"][1]["ending_state"] == "state2"

    def test_binary_sensor_add_update_2(self):
        test_case = self.data[1]

        assert test_case["transitions"][2]["action"] == "emit_event"
        assert test_case["transitions"][2]["starting_state"] == "state2"
        assert test_case["transitions"][2]["ending_state"] == "state3"

    def test_binary_sensor_add_update_3(self):
        test_case = self.data[1]

        assert test_case["transitions"][3]["action"] == "emit_event"
        assert test_case["transitions"][3]["starting_state"] == "state3"
        assert test_case["transitions"][3]["ending_state"] == "state4"

    def test_grouped_motion_sensor_0(self):
        test_case = self.data[2]

        assert test_case["transitions"][0]["action"] == "setup_platform"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_off"

    def test_grouped_motion_sensor_1(self):
        test_case = self.data[2]

        assert test_case["transitions"][1]["action"] == "emit_event"
        assert test_case["transitions"][1]["starting_state"] == "state_off"
        assert test_case["transitions"][1]["ending_state"] == "state_on"

    def test_grouped_motion_sensor_2(self):
        test_case = self.data[2]

        assert test_case["transitions"][2]["action"] == "emit_event"
        assert test_case["transitions"][2]["starting_state"] == "state_on"
        assert test_case["transitions"][2]["ending_state"] == "state_unknown"

    def test_motion_aware_sensor_0(self):
        test_case = self.data[3]

        assert test_case["transitions"][0]["action"] == "setup_platform"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_motion_aware_sensor_1(self):
        test_case = self.data[3]

        assert test_case["transitions"][1]["action"] == "mock_bridge_v2.api.emit_event"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_motion_aware_sensor_2(self):
        test_case = self.data[3]

        assert test_case["transitions"][2]["action"] == "mock_bridge_v2.api.emit_event"
        assert test_case["transitions"][2]["starting_state"] == "state_2"
        assert test_case["transitions"][2]["ending_state"] == "state_3"

class Test_hue_bridge():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "bridge_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_bridge_setup_v1_0(self):
        test_case = self.data[0]

        assert test_case["transitions"][0]["action"] == "async_initialize_bridge"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_bridge_setup_v1_1(self):
        test_case = self.data[0]

        assert test_case["transitions"][1]["action"] == "extract_forward_entries"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"


    @pytest.mark.xfail(reason="weird action name")
    def test_bridge_device_v1_0(self):
        test_case = self.data[1]

        assert test_case["transitions"][0]["action"] == "async_setup"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state1"

    @pytest.mark.xfail(reason="weird action name")
    def test_bridge_device_v1_1(self):
        test_case = self.data[1]

        assert test_case["transitions"][1]["action"] == "create_events"
        assert test_case["transitions"][1]["starting_state"] == "state1"
        assert test_case["transitions"][1]["ending_state"] == "state2"

    @pytest.mark.xfail(reason="weird action name")
    def test_bridge_device_v1_2(self):
        test_case = self.data[1]

        assert test_case["transitions"][2]["action"] == "device_registry.async_get_device_by_identifier"
        assert test_case["transitions"][2]["starting_state"] == "state2"
        assert test_case["transitions"][2]["ending_state"] == "state3"

    def test_bridge_device_v2_0(self):
        test_case = self.data[2]

        assert test_case["transitions"][0]["action"] == "setup_platform"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_bridge_device_v2_1(self):
        test_case = self.data[2]

        assert test_case["transitions"][1]["action"] == "filter_create_events"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_bridge_setup_v2_0(self):
        test_case = self.data[3]

        assert test_case["transitions"][0]["action"] == "async_initialize_bridge"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state1"

    def test_bridge_setup_v2_1(self):
        test_case = self.data[3]

        assert test_case["transitions"][1]["action"] == "extract_forward_entries"
        assert test_case["transitions"][1]["starting_state"] == "state1"
        assert test_case["transitions"][1]["ending_state"] == "state2"

    def test_bridge_device_v2_0(self):
        test_case = self.data[4]

        assert test_case["transitions"][0]["action"] == "async_initialize_bridge"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "post_init"

    def test_bridge_setup_timeout_length(self):
        test_case = self.data[5]

        assert test_case["transitions"][0]["action"] == "async_initialize_bridge"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "error_state"

    def test_reset_unloads_entry_if_setup_length(self):
        test_case = self.data[6]

        assert test_case["transitions"][0]["action"] == "async_initialize_bridge"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "initialized"

    def test_reset_unloads_entry_if_setup_length(self):
        test_case = self.data[6]

        assert test_case["transitions"][1]["action"] == "async_reset"
        assert test_case["transitions"][1]["starting_state"] == "initialized"
        assert test_case["transitions"][1]["ending_state"] == "reset"

    @pytest.mark.xfail(reason="Wrong ending state, extra state in between")
    def test_handle_unauthorized_length(self):
        test_case = self.data[7]

        assert test_case["transitions"][0]["action"] == "async_initialize_bridge"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "unauthorized_handled_state"

class Test_hue_device_trigger_v1():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "device_trigger_v1_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_get_triggers_0(self):
        test_case = self.data[0]

        assert test_case["transitions"][0]["action"] == "mock_bridge_v1.mock_sensor_responses.append"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_setup"

    def test_get_triggers_1(self):
        test_case = self.data[0]

        assert test_case["transitions"][1]["action"] == "async_get_device_automations"
        assert test_case["transitions"][1]["starting_state"] == "state_setup"
        assert test_case["transitions"][1]["ending_state"] == "state_tap_triggers"

    def test_get_triggers_2(self):
        test_case = self.data[0]

        assert test_case["transitions"][2]["action"] == "async_get_device_automations"
        assert test_case["transitions"][2]["starting_state"] == "state_tap_triggers"
        assert test_case["transitions"][2]["ending_state"] == "state_dimmer_triggers"

    def test_if_fires_on_state_change_0(self):
        test_case = self.data[1]

        assert test_case["transitions"][0]["action"] == "setup_platform"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    @pytest.mark.xfail(reason="weird action name")
    def test_if_fires_on_state_change_1(self):
        test_case = self.data[1]

        assert test_case["transitions"][1]["action"] == "mock_bridge_v1.mock_sensor_responses.append(new_sensor_response)"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    @pytest.mark.xfail(reason="weird action name")
    def test_if_fires_on_state_change_2(self):
        test_case = self.data[1]

        assert test_case["transitions"][2]["action"] == "mock_bridge_v1.mock_sensor_responses.append(new_sensor_response)"
        assert test_case["transitions"][2]["starting_state"] == "state_2"
        assert test_case["transitions"][2]["ending_state"] == "state_3"

class Test_hue_device_trigger_v2():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "device_trigger_v2_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_hue_event_0(self):
        test_case = self.data[0]

        assert test_case["transitions"][0]["action"] == "emit_event"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "post_event_state"

class Test_elgato_button():
    def setup_method(self):
        output_dir = Path("elgato_test_outputs").resolve()
        path = output_dir / "button_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_buttons_0(self):
        test_case = self.data[0]

        assert test_case["transitions"][0]["action"] == "hass.services.async_call"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_buttons_1(self):
        test_case = self.data[0]

        assert test_case["transitions"][1]["action"] == "getattr(mock_elgato, method)"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_buttons_2(self):
        test_case = self.data[0]

        assert test_case["transitions"][2]["action"] == "hass.states.get"
        assert test_case["transitions"][2]["starting_state"] == "state_2"
        assert test_case["transitions"][2]["ending_state"] == "state_3"

    def test_buttons_3(self):
        test_case = self.data[0]

        assert test_case["transitions"][3]["action"] == "hass.services.async_call (ElgatoError)"
        assert test_case["transitions"][3]["starting_state"] == "state_3"
        assert test_case["transitions"][3]["ending_state"] == "state_4"

    def test_buttons_4(self):
        test_case = self.data[0]

        assert test_case["transitions"][4]["action"] == "hass.services.async_call (ElgatoConnectionError)"
        assert test_case["transitions"][4]["starting_state"] == "state_4"
        assert test_case["transitions"][4]["ending_state"] == "state_5"

class Test_elgato_config_flow():
    def setup_method(self):
        output_dir = Path("elgato_test_outputs").resolve()
        path = output_dir / "config_flow_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_buttons_0(self):
        test_case = self.data[0]

        assert test_case["transitions"][0]["action"] == "async_init"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "form_state"

    def test_buttons_1(self):
        test_case = self.data[0]

        assert test_case["transitions"][1]["action"] == "async_configure"
        assert test_case["transitions"][1]["starting_state"] == "form_state"
        assert test_case["transitions"][1]["ending_state"] == "create_entry_state"

    def test_buttons_2(self):
        test_case = self.data[0]

        assert test_case["transitions"][2]["action"] == "assign_config_entry"
        assert test_case["transitions"][2]["starting_state"] == "create_entry_state"
        assert test_case["transitions"][2]["ending_state"] == "final_state"

    def test_full_zeroconf_flow_implementation_0(self):
        test_case = self.data[1]

        assert test_case["transitions"][0]["action"] == "hass.config_entries.flow.async_init"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_full_zeroconf_flow_implementation_1(self):
        test_case = self.data[1]

        assert test_case["transitions"][1]["action"] == "hass.config_entries.flow.async_progress"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_full_zeroconf_flow_implementation_2(self):
        test_case = self.data[1]

        assert test_case["transitions"][2]["action"] == "hass.config_entries.flow.async_configure"
        assert test_case["transitions"][2]["starting_state"] == "state_2"
        assert test_case["transitions"][2]["ending_state"] == "state_3"

    def test_full_zeroconf_flow_implementation_3(self):
        test_case = self.data[1]

        assert test_case["transitions"][3]["action"] == "assign"
        assert test_case["transitions"][3]["starting_state"] == "state_3"
        assert test_case["transitions"][3]["ending_state"] == "state_4"

    def test_connection_error_0(self):
        test_case = self.data[2]

        assert test_case["transitions"][0]["action"] == "hass.config_entries.flow.async_init"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "error_form"

    def test_connection_error_1(self):
        test_case = self.data[2]

        assert test_case["transitions"][1]["action"] == "hass.config_entries.flow.async_init"
        assert test_case["transitions"][1]["starting_state"] == "error_form"
        assert test_case["transitions"][1]["ending_state"] == "create_entry"

    def test_connection_error_2(self):
        test_case = self.data[2]

        assert test_case["transitions"][2]["action"] == "extract_config_entry"
        assert test_case["transitions"][2]["starting_state"] == "create_entry"
        assert test_case["transitions"][2]["ending_state"] == "entry_details"

    def test_zeroconf_connection_error_0(self):
        test_case = self.data[3]

        assert test_case["transitions"][0]["action"] == "async_init zeroconf flow"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "aborted_state"

    def test_user_device_exists_abort_0(self):
        test_case = self.data[4]

        assert test_case["transitions"][0]["action"] == "hass.config_entries.flow.async_init"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "abort_state"

    def test_zeroconf_device_exists_abort_0(self):
        test_case = self.data[5]

        assert test_case["transitions"][0]["action"] == "hass.config_entries.flow.async_init"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "abort_state_1"

    def test_zeroconf_device_exists_abort_1(self):
        test_case = self.data[5]

        assert test_case["transitions"][1]["action"] == "hass.config_entries.async_entries"
        assert test_case["transitions"][1]["starting_state"] == "abort_state_1"
        assert test_case["transitions"][1]["ending_state"] == "entry_state_1"

    def test_zeroconf_device_exists_abort_2(self):
        test_case = self.data[5]

        assert test_case["transitions"][2]["action"] == "hass.config_entries.flow.async_init"
        assert test_case["transitions"][2]["starting_state"] == "entry_state_1"
        assert test_case["transitions"][2]["ending_state"] == "abort_state_2"

    def test_zeroconf_device_exists_abort_3(self):
        test_case = self.data[5]

        assert test_case["transitions"][3]["action"] == "hass.config_entries.async_entries"
        assert test_case["transitions"][3]["starting_state"] == "abort_state_2"
        assert test_case["transitions"][3]["ending_state"] == "entry_state_2"

    def test_zeroconf_during_onboarding_0(self):
        test_case = self.data[6]

        assert test_case["transitions"][0]["action"] == "hass.config_entries.flow.async_init"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "post_async_init"

    def test_zeroconf_during_onboarding_1(self):
        test_case = self.data[6]

        assert test_case["transitions"][1]["action"] == "assign config_entry = result['result'] and process entry"
        assert test_case["transitions"][1]["starting_state"] == "post_async_init"
        assert test_case["transitions"][1]["ending_state"] == "entry_created"

    def test_dhcp_discovery_updates_host_0(self):
        test_case = self.data[7]

        assert test_case["transitions"][0]["action"] == "dhcp_discovery_flow"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "final_state"


    def test_dhcp_discovery_same_host_0(self):
        test_case = self.data[8]

        assert test_case["transitions"][0]["action"] == "async_init dhcp discovery flow"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "final_state"

    def test_dhcp_discovery_no_match_0(self):
        test_case = self.data[9]

        assert test_case["transitions"][0]["action"] == "async_init_dhcp_flow"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "final_state"

    def test_reconfigure_flow_0(self):
        test_case = self.data[10]

        assert test_case["transitions"][0]["action"] == "start_reconfigure_flow"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "form_state"

    def test_reconfigure_flow_1(self):
        test_case = self.data[10]

        assert test_case["transitions"][1]["action"] == "async_configure"
        assert test_case["transitions"][1]["starting_state"] == "form_state"
        assert test_case["transitions"][1]["ending_state"] == "abort_state"

    def test_reconfigure_flow_2(self):
        test_case = self.data[10]

        assert test_case["transitions"][2]["action"] == "add_to_hass"
        assert test_case["transitions"][2]["starting_state"] == "initial_state"
        assert test_case["transitions"][2]["ending_state"] == "initial_state"

    def test_reconfigure_flow_cannot_connect_0(self):
        test_case = self.data[11]

        assert test_case["transitions"][0]["action"] == "hass.config_entries.flow.async_configure"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "state_form_error"

    def test_reconfigure_flow_cannot_connect_1(self):
        test_case = self.data[11]

        assert test_case["transitions"][1]["action"] == "hass.config_entries.flow.async_configure"
        assert test_case["transitions"][1]["starting_state"] == "state_form_error"
        assert test_case["transitions"][1]["ending_state"] == "state_abort_success"

    def test_reconfigure_flow_different_device_0(self):
        test_case = self.data[12]

        assert test_case["transitions"][0]["action"] == "add_to_hass"
        assert test_case["transitions"][0]["starting_state"] == "initial_state"
        assert test_case["transitions"][0]["ending_state"] == "added_state"

    def test_reconfigure_flow_different_device_1(self):
        test_case = self.data[12]

        assert test_case["transitions"][1]["action"] == "start_reconfigure_flow"
        assert test_case["transitions"][1]["starting_state"] == "added_state"
        assert test_case["transitions"][1]["ending_state"] == "reconfigure_started"

    def test_reconfigure_flow_different_device_2(self):
        test_case = self.data[12]

        assert test_case["transitions"][2]["action"] == "async_configure"
        assert test_case["transitions"][2]["starting_state"] == "reconfigure_started"
        assert test_case["transitions"][2]["ending_state"] == "abort_state"

class Test_elgato_light():
    def setup_method(self):
        output_dir = Path("elgato_test_outputs").resolve()
        path = output_dir / "light_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_light_change_state_temperature_0(self):
        test_case = self.data[1]

        assert test_case["transitions"][0]["action"] == "turn_on"
        assert test_case["transitions"][0]["starting_state"] == "state_0"
        assert test_case["transitions"][0]["ending_state"] == "state_1"

    def test_light_change_state_temperature_1(self):
        test_case = self.data[1]

        assert test_case["transitions"][1]["action"] == "turn_on"
        assert test_case["transitions"][1]["starting_state"] == "state_1"
        assert test_case["transitions"][1]["ending_state"] == "state_2"

    def test_light_change_state_temperature_2(self):
        test_case = self.data[1]

        assert test_case["transitions"][2]["action"] == "turn_off"
        assert test_case["transitions"][2]["starting_state"] == "state_2"
        assert test_case["transitions"][2]["ending_state"] == "state_3"

    def test_light_change_state_temperature_3(self):
        test_case = self.data[1]

        assert test_case["transitions"][3]["action"] == "turn_on"
        assert test_case["transitions"][3]["starting_state"] == "state_3"
        assert test_case["transitions"][3]["ending_state"] == "state_4"