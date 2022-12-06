import textfsm

def test_show_chassis_hardware():
    hardware_file = open("hardware_info", "r")
    hardware_info = hardware_file.read()
    hardware_file.close()
    print(hardware_info)
    
    template = "template.textfsm"
    f = open(template)
    re_table = textfsm.TextFSM(f)
    fsm_results = re_table.ParseText(hardware_info)
    
    print(re_table.header)
    
    collection_of_results = [dict(zip(re_table.header, pr)) for pr in fsm_results]
    print(collection_of_results)


test_show_chassis_hardware()