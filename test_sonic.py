import textfsm
from textfsm import clitable

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
    for result in fsm_results:
        print(result)
    # cli_obj = clitable.CliTable("index", f)
    # cli_obj.ParseCmd(hardware_info, raw_text=False)
    collection_of_results = [dict(zip(re_table.header, pr)) for pr in fsm_results]
    print(collection_of_results)

#Routing_engine


test_show_chassis_hardware()
