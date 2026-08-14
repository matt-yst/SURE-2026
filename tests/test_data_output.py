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

    def test_block_binary_sensor_0(self):
        test_case = self.data[0]

        assert test_case["states"]["state_off"]["variables"] == {"state.state": "STATE_OFF"} 

    def test_block_binary_sensor_1(self):
        test_case = self.data[0]

        assert test_case["states"]["state_on"]["variables"] == {"state.state": "STATE_ON", 
                                                                "entry.unique_id": "'123456789ABC-relay_0-overpower'"}

    def test_block_binary_gas_sensor_creation_0(self):
        test_case = self.data[1]

        assert test_case["states"]["STATE_ON"]["variables"] == {"state.state": "STATE_ON"} 

    def test_block_binary_gas_sensor_creation_1(self):
        test_case = self.data[1]

        assert test_case["states"]["STATE_OFF"]["variables"] == {"state.state": "STATE_OFF", 
                                                                "entry.unique_id": "123456789ABC-sensor_0-gas"}
        
    def test_block_rest_binary_sensor_0(self):
        test_case = self.data[2]

        assert test_case["states"]["state_1"]["variables"] == {"state.state": "STATE_OFF"} 

    def test_block_rest_binary_sensor_1(self):
        test_case = self.data[2]

        assert test_case["states"]["state_2"]["variables"] == {
                    "state.state": "STATE_ON",
                    "entry.unique_id": "'123456789ABC-cloud'"
                }

    def test_block_rest_binary_sensor_connected_battery_devices_0(self):
        test_case = self.data[3]

        assert test_case["states"]["state_1"]["variables"] == {"state.state": "STATE_OFF"} 

    def test_block_rest_binary_sensor_connected_battery_devices_1(self):
        test_case = self.data[3]

        assert test_case["states"]["state_2"]["variables"] == {"state.state": "STATE_OFF"} 

    def test_block_rest_binary_sensor_connected_battery_devices_2(self):
        test_case = self.data[3]

        assert test_case["states"]["state_3"]["variables"] == {
                    "state.state": "STATE_ON",
                    "entry.unique_id": "123456789ABC-cloud"
                }

    def test_block_sleeping_binary_sensor_0(self):
        test_case = self.data[4]

        assert test_case["states"]["state_1"]["variables"] == {"hass.states.get(entity_id)": "None"}

    def test_block_sleeping_binary_sensor_1(self):
        test_case = self.data[4]

        assert test_case["states"]["state_2"]["variables"] == {"state.state": "STATE_OFF"} 

    def test_block_sleeping_binary_sensor_2(self):
        test_case = self.data[4]

        assert test_case["states"]["state_3"]["variables"] == {
                    "state.state": "STATE_ON",
                    "entry.unique_id": "'123456789ABC-sensor_0-motion'"
                }
    def test_block_restored_sleeping_binary_sensor_0(self):
        test_case = self.data[5]

        assert test_case["states"]["STATE_ON"]["variables"] == {"state.state": "STATE_ON"} 

    def test_block_restored_sleeping_binary_sensor_1(self):
        test_case = self.data[5]
        assert test_case["states"]["STATE_OFF"]["variables"] == {"state.state": "STATE_OFF"}

    def test_block_restored_sleeping_binary_sensor_no_last_state_0(self):
        test_case = self.data[6]

        assert test_case["states"]["state_unknown"]["variables"] == {"state.state": "STATE_UNKNOWN"}

    def test_block_restored_sleeping_binary_sensor_no_last_state_1(self):
        test_case = self.data[6]

        assert test_case["states"]["state_off"]["variables"] == {"state.state": "STATE_OFF"} 

    def test_rpc_binary_sensor_0(self):
        test_case = self.data[7]

        assert test_case["states"]["state_1"]["variables"] == {"state.state": "STATE_OFF"}

    def test_rpc_binary_sensor_1(self):
        test_case = self.data[7]

        assert test_case["states"]["state_2"]["variables"] == {
                    "state.state": "STATE_ON",
                    "entry.unique_id": "123456789ABC-cover:0-overpower"
                }

    def test_rpc_binary_sensor_input_custom_name_0(self):
        test_case = self.data[8]

        assert test_case["states"]["state_on"]["variables"] == {"state.state": "STATE_ON"} 

    def test_rpc_binary_sensor_removal_0(self):
        test_case = self.data[9]

        assert test_case["states"]["state_1"]["variables"] == {"entity_registry.async_get(entity_id)": "None"}

    def test_rpc_binary_sensor_removal_1(self):
        test_case = self.data[9]

        assert test_case["states"]["state_2"]["variables"] == {"entity_registry.async_get(entity_id)": "None"}


    def test_rpc_sleeping_binary_sensor_0(self):
        test_case = self.data[10]

        assert test_case["states"]["state_1"]["variables"] == {"hass.states.get(entity_id)": "None"}

    def test_rpc_sleeping_binary_sensor_1(self):
        test_case = self.data[10]

        assert test_case["states"]["state_2"]["variables"] == {"state.state": "STATE_OFF"}

    def test_rpc_sleeping_binary_sensor_2(self):
        test_case = self.data[10]

        assert test_case["states"]["state_3"]["variables"] =={
                    "state.state": "STATE_ON",
                    "entry.unique_id": "123456789ABC-devicepower:0-external_power"
                }

    def test_rpc_sleeping_binary_sensor_with_channel_name_0(self):
        test_case = self.data[11]

        assert test_case["states"]["no_entity"]["variables"] == {"hass.states.get(entity_id)": "None"}

    def test_rpc_sleeping_binary_sensor_with_channel_name_1(self):
        test_case = self.data[11]

        assert test_case["states"]["idle_off"]["variables"] == {
                    "state.attributes['friendly_name']": "Test name test channel name smoke",
                    "state.state": "STATE_OFF"
                }

    def test_rpc_sleeping_binary_sensor_with_channel_name_2(self):
        test_case = self.data[11]

        assert test_case["states"]["alarm_on"]["variables"] == {"state.state": "STATE_ON"}

    def test_rpc_restored_sleeping_binary_sensor_0(self):
        test_case = self.data[12]

        assert test_case["states"]["STATE_ON"]["variables"] == {"state.state": "STATE_ON"}

    def test_rpc_restored_sleeping_binary_sensor_1(self):
        test_case = self.data[12]

        assert test_case["states"]["STATE_OFF"]["variables"] == {"state.state": "STATE_OFF"}

    def test_rpc_restored_sleeping_binary_sensor_no_last_state_0(self):
        test_case = self.data[13]

        assert test_case["states"]["STATE_UNKNOWN"]["variables"] == {"state.state": "STATE_UNKNOWN"}

    def test_rpc_restored_sleeping_binary_sensor_no_last_state_1(self):
        test_case = self.data[13]

        assert test_case["states"]["STATE_OFF"]["variables"] == {"state.state": "STATE_OFF"}

    def test_rpc_device_virtual_binary_sensor_0(self):
        test_case = self.data[14]

        assert test_case["states"]["state_1"]["variables"] == {
                    "state.state": "STATE_ON",
                    "entry.unique_id": "'123456789ABC-boolean:203-boolean_generic'"
                }

    def test_rpc_device_virtual_binary_sensor_1(self):
        test_case = self.data[14]

        assert test_case["states"]["state_2"]["variables"] == {"state.state": "STATE_OFF"}

class Test_hue_binary_sensor():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "binary_sensor_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_binary_sensors_0(self):
        test_case = self.data[0]
    
        assert test_case["states"]["post_setup"]["variables"] == {"len(mock_bridge_v2.mock_requests)": "0"} 

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_binary_sensors_1(self):
        test_case = self.data[0]
    
        assert test_case["states"]["hue_motion_sensor_motion_created"]["variables"] == {
                    "sensor": "not None",
                    "sensor.state": "'off'",
                    "sensor.name": "'Hue motion sensor Motion'",
                    "sensor.attributes['device_class']": "'motion'"
                }

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_binary_sensors_2(self):
        test_case = self.data[0]

        assert test_case["states"]["philips_hue_entertainmentroom_1_created"]["variables"] == {
                    "sensor": "not None",
                    "sensor.state": "'off'",
                    "sensor.name": "'Philips hue Entertainmentroom 1'",
                    "sensor.attributes['device_class']": "'running'"
                }

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_binary_sensors_3(self):
        test_case = self.data[0]

        assert test_case["states"]["test_contact_sensor_opening_created"]["variables"] == {
                    "sensor": "not None",
                    "sensor.state": "'off'",
                    "sensor.name": "'Test contact sensor Opening'",
                    "sensor.attributes['device_class']": "'opening'"
                }

    def test_binary_sensors_4(self):
        test_case = self.data[0]

        assert test_case["states"]["test_contact_sensor_opening_unknown"]["variables"] == {"sensor.state": "'unknown'"}

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_binary_sensors_5(self):
        test_case = self.data[0]

        assert test_case["states"]["test_contact_sensor_tamper_created"]["variables"] == {
                    "sensor": "not None",
                    "sensor.state": "'off'",
                    "sensor.name": "'Test contact sensor Tamper'",
                    "sensor.attributes['device_class']": "'tamper'"
                }

    def test_binary_sensors_6(self):
        test_case = self.data[0]

        assert test_case["states"]["test_contact_sensor_tamper_after_update"]["variables"] == {"sensor.state": "'off'"}

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_binary_sensors_7(self):
        test_case = self.data[0]

        assert test_case["states"]["test_camera_motion_created"]["variables"] == {
                    "sensor": "not None",
                    "sensor.state": "'on'",
                    "sensor.name": "'Test Camera Motion'",
                    "sensor.attributes['device_class']": "'motion'"
                }

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_binary_sensors_8(self):
        test_case = self.data[0]

        assert test_case["states"]["sensor_group_motion_created"]["variables"] == {
                    "sensor": "not None",
                    "sensor.state": "'off'",
                    "sensor.name": "'Sensor group Motion'",
                    "sensor.attributes['device_class']": "'motion'"
                }

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_binary_sensors_9(self):
        test_case = self.data[0]

        assert test_case["states"]["test_room_motion_aware_sensor_1_created"]["variables"] == {
                    "sensor": "not None",
                    "sensor.state": "'off'",
                    "sensor.name": "'Test Room Motion Aware Sensor 1'",
                    "sensor.attributes['device_class']": "'motion'"
                }

    def test_binary_sensor_add_update_0(self):
        test_case = self.data[1]

        assert test_case["states"]["state0"]["variables"] == {"hass.states.get(test_entity_id)": "None"}

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_binary_sensor_add_update_1(self):
        test_case = self.data[1]

        assert test_case["states"]["state1"]["variables"] == {
                    "test_entity": "not None",
                    "test_entity.state": "'off'"
                }
        
    @pytest.mark.xfail(reason="output None instead of not None")
    def test_binary_sensor_add_update_2(self):
        test_case = self.data[1]

        assert test_case["states"]["state2"]["variables"] == {
                    "test_entity": "not None",
                    "test_entity.state": "'on'"
                }

    def test_binary_sensor_add_update_3(self):
        test_case = self.data[1]

        assert test_case["states"]["state3"]["variables"] == {"hass.states.get(test_entity_id).state": "'on'"}

    def test_binary_sensor_add_update_4(self):
        test_case = self.data[1]

        assert test_case["states"]["state4"]["variables"] == {"hass.states.get(test_entity_id).state": "'off'"}

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_grouped_motion_sensor_0(self):
        test_case = self.data[2]

        assert test_case["states"]["state_off"]["variables"] == {
                    "sensor": "not None",
                    "sensor.state": "off",
                    "sensor.attributes['device_class']": "motion"
                }

    def test_grouped_motion_sensor_1(self):
        test_case = self.data[2]

        assert test_case["states"]["state_on"]["variables"] == {"sensor.state": "on"}

    def test_grouped_motion_sensor_2(self):
        test_case = self.data[2]

        assert test_case["states"]["state_unknown"]["variables"] == {"sensor.state": "unknown"}

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_motion_aware_sensor_0(self):
        test_case = self.data[3]

        assert test_case["states"]["state_1"]["variables"] == {
                    "sensor": "not None",
                    "sensor.state": "off",
                    "sensor.attributes['device_class']": "motion"
                }

    def test_motion_aware_sensor_1(self):
        test_case = self.data[3]

        assert test_case["states"]["state_2"]["variables"] == {"sensor.state": "on"}

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_motion_aware_sensor_2(self):
        test_case = self.data[3]

        assert test_case["states"]["state_1"]["variables"] == {
                    "sensor": "not None",
                    "sensor.name": "Test Room Updated Motion Area"
                }

class Test_hue_bridge():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "bridge_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    @pytest.mark.xfail(reason="missing value")
    def test_bridge_setup_v1_0(self):
        test_case = self.data[0]
    
        assert test_case["states"]["state_1"]["variables"] == {
                    "hue_bridge.api": "mock_api_v1",
                    "isinstance(hue_bridge.api, HueBridgeV1)": "True",
                    "hue_bridge.api_version": "1",
                    "len(mock_forward.mock_calls)": "1"
                }

    def test_bridge_setup_v1_1(self):
        test_case = self.data[0]

        assert test_case["states"]["state_2"]["variables"] == {"forward_entries": "{'light', 'binary_sensor', 'sensor'}"}

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_bridge_device_v1_0(self):
        test_case = self.data[1]

        assert test_case["states"]["state1"]["variables"] == {
                    "bridge_device": "not None",
                    "bridge_device.connections": "{(dr.CONNECTION_NETWORK_MAC, mock_api_v1.config.mac_address)}"
                }
        
    def test_bridge_device_v1_1(self):
        test_case = self.data[1]
        assert test_case["states"]["state2"]["variables"] == {"len(create_events)": "1"}

    @pytest.mark.xfail(reason="output None instead of not None")
    def test_bridge_device_v1_2(self):
        test_case = self.data[1]

        assert test_case["states"]["state2"]["variables"] == {
                    "light_device": "not None",
                    "light_device.via_device_id": "bridge_device.id"
                }

    @pytest.mark.xfail(reason="output None instead of not None")    
    def test_bridge_device_v2_0(self):
        test_case = self.data[2]

        assert test_case["states"]["state_1"]["variables"] == {
                    "bridge_device": "not None",
                    "bridge_device.identifiers": "{(DOMAIN, mock_bridge_v2.api.config.bridge_id), (DOMAIN, mock_bridge_v2.api.config.bridge_device.id)}",
                    "bridge_device.connections": "{(dr.CONNECTION_NETWORK_MAC, '00:17:88:01:aa:bb:fd:c7'), (dr.CONNECTION_NETWORK_MAC, mock_bridge_v2.api.config.mac_address)}"
                }

    def test_bridge_device_v2_1(self):
        test_case = self.data[2]
        assert test_case["states"]["state_2"]["variables"] == {"len(create_events)": "1"}

    @pytest.mark.xfail(reason="missing value") 
    def test_bridge_setup_v2_0(self):
        test_case = self.data[3]

        assert test_case["states"]["state1"]["variables"] == {
                    "hue_bridge.api": "mock_api_v2",
                    "isinstance(hue_bridge.api, HueBridgeV1)": "True",
                    "hue_bridge.api_version": "2",
                    "len(mock_forward.mock_calls)": "1"
                }

    def test_bridge_setup_v2_1(self):
        test_case = self.data[3]

        assert test_case["states"]["state2"]["variables"] == {"forward_entries": "{'light', 'binary_sensor', 'event', 'sensor', 'switch', 'scene'}"}

    def test_bridge_setup_invalid_api_key_0(self):
        test_case = self.data[4]

        assert test_case["states"]["post_init"]["variables"] == {
                    "len(mock_init.mock_calls)": "1",
                    "mock_init.mock_calls[0][2]['data']": "{'host': '1.2.3.4'}"
                }

    def test_bridge_setup_timeout_0(self):
        test_case = self.data[5]

        assert test_case["states"]["error_state"]["variables"] == {"exception": "ConfigEntryNotReady"}

    def test_reset_unloads_entry_if_setup_0(self):
        test_case = self.data[6]

        assert test_case["states"]["initialized"]["variables"] == {
                    "len(hass.services.async_services())": "0",
                    "len(mock_forward.mock_calls)": "1"
                }

    def test_reset_unloads_entry_if_setup_1(self):
        test_case = self.data[6]

        assert test_case["states"]["reset"]["variables"] == {
                    "len(mock_forward.mock_calls)": "3",
                    "len(hass.services.async_services())": "0"
                }

    def test_reset_unloads_entry_if_setup_0(self):
        test_case = self.data[7]

        assert test_case["states"]["unauthorized_handled_state"]["variables"] == {
                    "hue_bridge.authorized": "False",
                    "len(mock_create.mock_calls)": "1",
                    "mock_create.mock_calls[0][1][1]": "'1.2.3.4'"
                }

class Test_hue_device_trigger_v1():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "device_trigger_v1_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_get_triggers_0(self):
        test_case = self.data[0]

        assert test_case["states"]["state_setup"]["variables"] == {
                    "len(mock_bridge_v1.mock_requests)": "1",
                    "len(hass.states.async_all())": "1"
                }

    def test_get_triggers_1(self):
        test_case = self.data[0]

        assert test_case["states"]["state_tap_triggers"]["variables"] == {"triggers": "unordered(expected_triggers)"}

    def test_get_triggers_2(self):
        test_case = self.data[0]

        assert test_case["states"]["state_dimmer_triggers"]["variables"] == {"triggers": "unordered(expected_triggers)"}

    def test_if_fires_on_state_change_0(self):
        test_case = self.data[1]

        assert test_case["states"]["state_1"]["variables"] == {
                    "len(mock_bridge_v1.mock_requests)": "1",
                    "len(hass.states.async_all())": "1"
                }

    def test_if_fires_on_state_change_1(self):
        test_case = self.data[1]

        assert test_case["states"]["state_2"]["variables"] == {
                    "len(mock_bridge_v1.mock_requests)": "2",
                    "len(service_calls)": "1",
                    "service_calls[0].data['some']": "'B4 - 18'"
                }

    def test_if_fires_on_state_change_2(self):
        test_case = self.data[1]

        assert test_case["states"]["state_3"]["variables"] == {
                    "len(mock_bridge_v1.mock_requests)": "3",
                    "len(service_calls)": "1"
                }

class Test_hue_device_trigger_v2():
    def setup_method(self):
        output_dir = Path("hue_test_outputs").resolve()
        path = output_dir / "device_trigger_v2_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_hue_event_0(self):
        test_case = self.data[0]

        assert test_case["states"]["post_event_state"]["variables"] == {
                    "len(events)": "1",
                    "events[0].data['id']": "wall_switch_with_2_controls_button",
                    "events[0].data['unique_id']": "btn_event['id']",
                    "events[0].data['type']": "btn_event['button']['button_report']['event']",
                    "events[0].data['subtype']": "btn_event['metadata']['control_id']"
                }

class Test_elgato_button():
    def setup_method(self):
        output_dir = Path("elgato_test_outputs").resolve()
        path = output_dir / "button_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_buttons_0(self):
        test_case = self.data[0]

        assert test_case["states"]["state_1"]["variables"] == {
                    "state": "snapshot",
                    "entry": "snapshot",
                    "device_entry": "snapshot"
                }
        
    def test_buttons_1(self):
        test_case = self.data[0]

        assert test_case["states"]["state_2"]["variables"] == {"len(mocked_method.mock_calls)": "1"}

    def test_buttons_2(self):
        test_case = self.data[0]

        assert test_case["states"]["state_3"]["variables"] == {"state.state": "'2021-11-13T11:48:00+00:00'"}

    def test_buttons_3(self):
        test_case = self.data[0]

        assert test_case["states"]["state_4"]["variables"] == {"len(mocked_method.mock_calls)": "2"}

    def test_buttons_4(self):
        test_case = self.data[0]

        assert test_case["states"]["state_5"]["variables"] == {"len(mocked_method.mock_calls)": "3"}

class Test_elgato_config_flow():
    def setup_method(self):
        output_dir = Path("elgato_test_outputs").resolve()
        path = output_dir / "config_flow_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data

    def test_full_user_flow_implementation_0(self):
        test_case = self.data[0]

        assert test_case["states"]["form_state"]["variables"] == {
                    "result['type']": "FlowResultType.FORM",
                    "result['step_id']": "user"
                }

    def test_full_user_flow_implementation_1(self):
        test_case = self.data[0]

        assert test_case["states"]["create_entry_state"]["variables"] == {"result['type']": "FlowResultType.CREATE_ENTRY"}

    def test_full_user_flow_implementation_2(self):
        test_case = self.data[0]

        assert test_case["states"]["final_state"]["variables"] == {
                    "config_entry.unique_id": "CN11A1A00001",
                    "config_entry.data": "{CONF_HOST: '127.0.0.1', CONF_MAC: None}",
                    "len(mock_setup_entry.mock_calls)": "1",
                    "len(mock_elgato.info.mock_calls)": "1"
                }

    def test_full_zeroconf_flow_implementation_0(self):
        test_case = self.data[1]

        assert test_case["states"]["state_1"]["variables"] == {
                    "result['description_placeholders']": "{'serial_number': 'CN11A1A00001'}",
                    "result['step_id']": "'zeroconf_confirm'",
                    "result['type']": "FlowResultType.FORM"
                }

    def test_full_zeroconf_flow_implementation_1(self):
        test_case = self.data[1]

        assert test_case["states"]["state_2"]["variables"] == {
                    "len(progress)": "1",
                    "progress[0].get('flow_id')": "result['flow_id']",
                    "context": "progress[0]",
                    "progress[0]['context'].get('confirm_only')": "True"
                }

    def test_full_zeroconf_flow_implementation_2(self):
        test_case = self.data[1]

        assert test_case["states"]["state_3"]["variables"] == {"result['type']": "FlowResultType.CREATE_ENTRY"}

    @pytest.mark.xfail(reason="missing value")
    def test_full_zeroconf_flow_implementation_3(self):
        test_case = self.data[1]

        assert test_case["states"]["state_4"]["variables"] == {
                    "config_entry.unique_id": "'CN11A1A00001'",
                    "config_entry.data": "{CONF_HOST: '127.0.0.1', CONF_MAC: 'AA:BB:CC:DD:EE:FF'}",
                    "config_entry.options": "False",
                    "len(mock_setup_entry.mock_calls)": "1",
                    "len(mock_elgato.info.mock_calls)": "1"
                }

    def test_connection_error_0(self):
        test_case = self.data[2]

        assert test_case["states"]["error_form"]["variables"] == {
                    "result['type']": "FlowResultType.FORM",
                    "result['errors']": "{'base': 'cannot_connect'}",
                    "result['step_id']": "'user'"
                }

    def test_connection_error_1(self):
        test_case = self.data[2]

        assert test_case["states"]["create_entry"]["variables"] == {"result['type']": "FlowResultType.CREATE_ENTRY"}

    @pytest.mark.xfail(reason="missing value")
    def test_connection_error_2(self):
        test_case = self.data[2]

        assert test_case["states"]["entry_details"]["variables"] == {
                    "config_entry.unique_id": "'CN11A1A00001'",
                    "config_entry.data": "{CONF_HOST: '127.0.0.2', CONF_MAC: None}",
                    "config_entry.options": "False"
                }

    def test_zeroconf_connection_error_0(self):
        test_case = self.data[3]

        assert test_case["states"]["aborted_state"]["variables"] == {
                    "result['reason']": "cannot_connect",
                    "result['type']": "FlowResultType.ABORT"
                }

    def test_user_device_exists_abort_0(self):
        test_case = self.data[4]

        assert test_case["states"]["abort_state"]["variables"] == {
                    "result['type']": "FlowResultType.ABORT",
                    "result['reason']": "already_configured"
                }

    def test_zeroconf_device_exists_abort_0(self):
        test_case = self.data[5]

        assert test_case["states"]["abort_state_1"]["variables"] == {
                    "result['type']": "FlowResultType.ABORT",
                    "result['reason']": "already_configured"
                }

    def test_zeroconf_device_exists_abort_1(self):
        test_case = self.data[5]

        assert test_case["states"]["entry_state_1"]["variables"] == {"entries[0].data[CONF_HOST]": "127.0.0.1"}

    def test_zeroconf_device_exists_abort_2(self):
        test_case = self.data[5]

        assert test_case["states"]["abort_state_2"]["variables"] == {
                    "result['type']": "FlowResultType.ABORT",
                    "result['reason']": "already_configured"
                }

    def test_zeroconf_device_exists_abort_3(self):
        test_case = self.data[5]

        assert test_case["states"]["entry_state_2"]["variables"] == {"entries[0].data[CONF_HOST]": "127.0.0.2"}

    def test_zeroconf_during_onboarding_0(self):
        test_case = self.data[6]

        assert test_case["states"]["post_async_init"]["variables"] == {"result['type']": "FlowResultType.CREATE_ENTRY"}

    @pytest.mark.xfail(reason="missing value")
    def test_zeroconf_during_onboarding_1(self):
        test_case = self.data[6]

        assert test_case["states"]["entry_created"]["variables"] == {
                    "config_entry.unique_id": "CN11A1A00001",
                    "config_entry.data": "{CONF_HOST: '127.0.0.1', CONF_MAC: 'AA:BB:CC:DD:EE:FF'}",
                    "config_entry.options": "False",
                    "len(mock_setup_entry.mock_calls)": "1",
                    "len(mock_elgato.info.mock_calls)": "1",
                    "len(mock_onboarding.mock_calls)": "1"
                }

    def test_dhcp_discovery_updates_host_0(self):
        test_case = self.data[7]

        assert test_case["states"]["final_state"]["variables"] == {
                    "result['type']": "FlowResultType.ABORT",
                    "result['reason']": "already_configured",
                    "mock_config_entry.data[CONF_HOST]": "127.0.0.42"
                }

    def test_dhcp_discovery_same_host_0(self):
        test_case = self.data[8]

        assert test_case["states"]["final_state"]["variables"] == {
                    "result['type']": "FlowResultType.ABORT",
                    "result['reason']": "already_configured",
                    "mock_config_entry.data[CONF_HOST]": "127.0.0.1"
                }

    def test_dhcp_discovery_no_match_0(self):
        test_case = self.data[9]

        assert test_case["states"]["final_state"]["variables"] == {
                    "result['type']": "FlowResultType.ABORT",
                    "result['reason']": "no_devices_found",
                    "mock_config_entry.data[CONF_HOST]": "127.0.0.1"
                }

    def test_reconfigure_flow_0(self):
        test_case = self.data[10]

        assert test_case["states"]["form_state"]["variables"] == {
                    "result['type']": "FlowResultType.FORM",
                    "result['step_id']": "reconfigure"
                }

    def test_reconfigure_flow_1(self):
        test_case = self.data[10]

        assert test_case["states"]["abort_state"]["variables"] == {
                    "result['type']": "FlowResultType.ABORT",
                    "result['reason']": "reconfigure_successful",
                    "mock_config_entry.data[CONF_HOST]": "127.0.0.42"
                }

    def test_reconfigure_flow_cannot_connect_0(self):
        test_case = self.data[11]

        assert test_case["states"]["state_form_error"]["variables"] == {
                    "result['type']": "FlowResultType.FORM",
                    "result['step_id']": "reconfigure",
                    "result['errors']": "{'base': 'cannot_connect'}"
                }

    def test_reconfigure_flow_cannot_connect_1(self):
        test_case = self.data[11]

        assert test_case["states"]["state_abort_success"]["variables"] == {
                    "result['type']": "FlowResultType.ABORT",
                    "result['reason']": "reconfigure_successful"
                }

    def test_reconfigure_flow_different_device_0(self):
        test_case = self.data[12]

        assert test_case["states"]["abort_state"]["variables"] == {
                    "result['type']": "FlowResultType.ABORT",
                    "result['reason']": "different_device",
                    "mock_config_entry.data[CONF_HOST]": "127.0.0.1"
                }

class Test_elgato_light():
    def setup_method(self):
        output_dir = Path("elgato_test_outputs").resolve()
        path = output_dir / "light_output.json"
        with open(path) as f:
            data = json.load(f) 
        self.data = data
    
    def test_light_state_temperature_0(self):
        test_case = self.data[0]

        assert test_case["states"]["snapshot"]["variables"] == {
                    "state": "snapshot",
                    "entry": "snapshot",
                    "device_entry": "snapshot"
                }

    def test_light_change_state_temperature_0(self):
        test_case = self.data[1]

        assert test_case["states"]["state_0"]["variables"] == {"state.state": "STATE_ON"}

    def test_light_change_state_temperature_1(self):
        test_case = self.data[1]

        assert test_case["states"]["state_1"]["variables"] == {"len(mock_elgato.light.mock_calls)": "1"}

    def test_light_change_state_temperature_2(self):
        test_case = self.data[1]

        assert test_case["states"]["state_2"]["variables"] == {"len(mock_elgato.light.mock_calls)": "2"}

    def test_light_change_state_temperature_3(self):
        test_case = self.data[1]

        assert test_case["states"]["state_3"]["variables"] == {"len(mock_elgato.light.mock_calls)": "3"}

    def test_light_change_state_temperature_4(self):
        test_case = self.data[1]

        assert test_case["states"]["state_4"]["variables"] == {"len(mock_elgato.light.mock_calls)": "4"}