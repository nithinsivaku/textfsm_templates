import textfsm

def test_show_chassis_hardware():
    hardware_file = open("hardware_info", "r")
    hardware_info = hardware_file.read()
    hardware_file.close()
    print(hardware_info)
    
    template = "sonic_show_chassis_hardware.textfsm"
    f = open(template)
    re_table = textfsm.TextFSM(f)
    fsm_results = re_table.ParseText(hardware_info)
    print(fsm_results)
    
    chassis_record = fsm_results[0] if fsm_results else None
    chassis_data = {
        'os': {
            'name': 'Sonicos'
        }
    }
    if chassis_record:
        chassis_data['os_version'] = 'os_version'
        chassis_data['serial_number'] = 'serial_number'
        components = []
        for result in fsm_results[1:]:
            component = get_component(result)
            components.append(component)
            print(result)
        chassis_data['component'] = components

    # when im in a record 
        # r be a record, then check if this is parent (i.e no whitespace before)
            # if parent
                # check if next record nr,  has two space infront
                    # yes ? then make nr child of r
                        # repeat previous step
                    # no ? repeat r
    
    
    
    # print(re_table.header)
    # for result in fsm_results:
    #     print(result) 

    # collection_of_results = [dict(zip(re_table.header, pr)) for pr in fsm_results]
    # print(collection_of_results)

def get_chassis_info(data):
    chassis_data = {}
    return chassis_data

def get_component(result):
    component_type_name = ''
    component_model_description = ''
    component_model_manufacturer = ''
    component_model_name = ''
    compoent_model_partnumber = ''
    component_position = ''
    component_serial = ''
    
    component_model = {}
    component_model['name'] = component_model_name
    component_model['part_number'] = compoent_model_partnumber
    component_model['description'] = component_model_description
    component_model['manufacturer'] = {
        'name': component_model_manufacturer
    }
    component_model['component_type'] = {
        'name': component_type_name
    }
                                                                                                                                                                                                                                                                                                                                                    
    component_data = {}
    component_data['position'] = component_position
    component_data['trace'] = {
        'serial_number': component_serial
    }
    component_data['component_model'] = component_model

    return component_data


def get_chassis_info():
    
    pass

def get_chassis():
    pass

def get_component():
    pass

test_show_chassis_hardware()
