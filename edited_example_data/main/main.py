from itertools import combinations
from re import L
from celloapi2 import CelloQuery, CelloResult,celloapi
import os
from celloapi2 import celloapi
import celloapi2
import numpy as np
import json
import ast

in_dir=os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), 'input')
out_dir=os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), 'output')
v_file = 'and.v'
options = 'options.csv'
# Calculate number of inputs into the Circuit.
signal_input = 2


chassis_name = ["Eco1C1G1T1"]
chassis = 'Eco1C1G1T1'
input_sensor_file = f'{chassis}.input.json'
output_device_file = f'{chassis}.output.json'
# in_dir = os.path.join(root_path, "example_data")
# out_dir = os.path.join(in_dir, "dummy_output")
in_ucf = f'{chassis}.UCF.json'
signal_option_file = f'{chassis}.signal_option.json'
modified_signal_file = f'{chassis}.modified_signal.json'
gate_option_file = f'{chassis}.gate_option.json'
modified_gate_file = f'{chassis}.modified_gate.UCF.json'
result_txt_file = f'{chassis}.result_file.txt'
modified_result_txt_file = f'{chassis}.modified_result_file.txt'

####################2####################
# define the options to modify signals #
####################2####################
class signal_options:
    def __init__(self):
        self.ymax =  0,
        self.ymin = 0,
        self.alpha = 0,
        self.beta = 0,

    def Stretch(self,x):
        if x == 0:
            print('x in Stretch cannot be 0')
            print('Stretch() have not be operated')
        else:
            self.ymax = self.ymax * min(1.5,x)
            self.ymin = self.ymin / min(1.5,x)
        return self

    def Increase_Slope(self,x):
        self.alpha = self.alpha * min(1.05,x)
        return self

    def Decrease_Slope(self,x):
        if x == 0:
            print('x in Decrease_Slope cannot be 0')
            print('Decrease_Slope() have not be operated')
        else:
            self.alpha = self.alpha / min(1.05,x)
        return self

    def Stronger_Promoter(self,x):
        self.ymax = self.ymax * x
        self.ymin = self.ymin * x
        return self

    def Weaker_Promoter(self,x):
        if x == 0:
            print('x in Weaker_Promoter cannot be 0')
            print('Weaker_Promoter() have not be operated')
        else:
            self.ymax = self.ymax / x
            self.ymin = self.ymin / x
        return self

    def Stronger_RBS(self,x):
        if x == 0:
            print('x in RBS cannot be 0')
            print('RBS() have not be operated')
        else:
            self.beta = self.beta / x
        return self

    def Weaker_RBS(self,x):
        self.beta = self.beta * x
        return self

    def get_parameter(self):
        return self.ymax, self.ymin, self.alpha, self.beta

class gate_options:
    def __init__(self):
        self.ymax =  0,
        self.ymin = 0,
        self.K = 0,
        self.n = 0,
        self.alpha = 0,
        self.beta = 0

    def Stretch(self,x):
        if x == 0:
            print('x in Stretch cannot be 0')
            print('Stretch() have not be operated')
        else:
            self.ymax = self.ymax * min(1.5,x)
            self.ymin = self.ymin / min(1.5,x)
        return self

    def Increase_Slope(self,x):
        self.n = self.n * min(1.05,x)
        return self

    def Decrease_Slope(self,x):
        if x == 0:
            print('x in Decrease_Slope cannot be 0')
            print('Decrease_Slope() have not be operated')
        else:
            self.n = self.n / min(1.05,x)
        return self

    def Stronger_Promoter(self,x):
        self.ymax = self.ymax * x
        self.ymin = self.ymin * x
        return self

    def Weaker_Promoter(self,x):
        if x == 0:
            print('x in Weaker_Promoter cannot be 0')
            print('Weaker_Promoter() have not be operated')
        else:
            self.ymax = self.ymax / x
            self.ymin = self.ymin / x
        return self

    def Stronger_RBS(self,x):
        if x == 0:
            print('x in RBS cannot be 0')
            print('RBS() have not be operated')
        else:
            self.K = self.K / x
        return self

    def Weaker_RBS(self,x):
        self.K = self.K * x
        return self

    def get_parameter(self):
        return self.ymax, self.ymin, self.K, self.n, self.alpha, self.beta
       

# get the signal option from the json file input
# user can specify the sensor, options, and the values
# the json file input will convert to a list of option commond directionary
# each directionary contains the sensor name and the option/options and parameter/parameters

def get_signal_option(signal_option_file_path):
    with open(os.path.join(in_dir, signal_option_file_path),'rb') as f:

        option_list = list()
        option_file = json.load(f)

        for row in option_file:
            if row["collection"] == "option":
                raw_name = row["name"]
                row_option = row["options"]
                option_list.append([raw_name.split("_")[0],row_option])
        
    return option_list

# modify the signal based on the options that the user defines
# each commond can modify a sensor with one or multiple options
# one sensor can be modified once or multiple times
# the original sensor information and the modified sensor information will be save in the modified_signal file

def modify_signal(option_list,input_sensor_file_path,modified_signal_file_path):
    modified_signal_txt_file = os.path.join(in_dir, modified_signal_file_path) + '.txt'
    file = open(os.path.join(in_dir, modified_signal_txt_file),'w')

    with open(os.path.join(in_dir,input_sensor_file_path), 'rb') as f:
        input_sensor_file = json.load(f)
        row_index = 0
        while input_sensor_file[row_index]["collection"] != "parts":
            file.write(str(input_sensor_file[row_index]) + '\n')
            file.write(str(input_sensor_file[row_index +1]) + '\n')
            file.write(str(input_sensor_file[row_index +2]) + '\n') 
            row = input_sensor_file[row_index]
            for item in option_list:
                if item[0] == row["name"].split("_")[0]:
                    # change the row of input_sensors
                    name_string = row["name"]
                    name_string_list = name_string.split("_")
                    new_row = row
                    for option in item[1]:
                        name_string_list[0] += option["name"].replace(" ","")
                    new_name_string = '_'.join(name_string_list)
                    new_row["name"] = row["name"].replace(name_string,new_name_string)
                    new_row["model"] = row["model"].replace(name_string,new_name_string)
                    new_row["structure"] = row["structure"].replace(name_string,new_name_string)
                    file.write(str(new_row) + '\n')
                    # change the row of model
                    row_model = input_sensor_file[row_index+1]
                    new_row_model = row_model
                    new_row_model["name"] = row_model["name"].replace(name_string,new_name_string)
                    parameters = row_model["parameters"]
                    parameter_list = [parameters[0]['value'],parameters[1]['value'],parameters[2]['value'], parameters[3]['value']]
                    parameter = signal_options()
                    [parameter.ymax,parameter.ymin,parameter.alpha,parameter.beta] = parameter_list
                    for option in item[1]:
                        option_coef = option["value"]
                        option_exe_name = "parameter." + option["name"].replace(" ","_") + "(" + str(option_coef) + ")"
                        exec(option_exe_name)
                    # print(exec(option_exe_name).ymax)
                    for para in parameters:
                        if para["name"] == "ymax":
                            para["value"] = parameter.ymax
                        if para["name"] == "ymin":
                            para["value"] = parameter.ymin
                        if para["name"] == "alpha":
                            para["value"] = parameter.alpha
                        if para["name"] == "beta":
                            para["value"] = parameter.beta
                    new_row_model["parameters"] = parameters
                    file.write(str(new_row_model) + '\n')
                    # change the row of structures
                    row_structure = input_sensor_file[row_index+2]
                    new_row_structure = row_structure
                    new_row_structure["name"] = row_structure["name"].replace(name_string,new_name_string)
                    file.write(str(new_row_structure) + '\n')
            row_index += 3
        while row_index < len(input_sensor_file):
            file.write(str(input_sensor_file[row_index]) + '\n')
            row_index += 1
        file.close()
    

    file = open(os.path.join(in_dir, modified_signal_txt_file),'r')
    lines = file.readlines()
    data_list = list()
    for line in lines:
        #data = json.dumps(line.replace(" ","").replace("\n",""))
        #data = json.loads(line.replace("\n",""))
        data = ast.literal_eval(line)
        data_list.append(data)

    data_json = json.dumps(data_list, ensure_ascii = False, indent = 4)
    with open(os.path.join(in_dir, modified_signal_file_path), 'w') as f:
        f.write(data_json)
    f.close()


def get_gate_option(gate_option_file_path):
    with open(os.path.join(in_dir, gate_option_file_path),'rb') as f:

        option_list = list()
        option_file = json.load(f)

        for row in option_file:
            if row["collection"] == "option":
                raw_name = row["name"]
                row_option = row["options"]
                option_list.append([raw_name[:7],row_option])
    # print(option_list)    
    return option_list


def modify_gate(option_list,input_gate_file_path,modified_gate_file_path):
    modified_gate_txt_file = os.path.join(in_dir, modified_gate_file_path) + '.txt'
    file = open(os.path.join(in_dir,modified_gate_txt_file),'w', encoding = "utf-8")

    with open(os.path.join(in_dir,input_gate_file_path), 'rb') as f:
        input_gate_file = json.load(f)
        for row in input_gate_file:
            if row["collection"] == "models":
                for item in option_list:
                    if item[0] == row["name"][:7]:
                        parameters = row["parameters"]
                        parameter_list = [parameters[0]['value'],parameters[1]['value'],parameters[2]['value'], parameters[3]['value'], parameters[4]['value'], parameters[5]['value']]
                        parameter = gate_options()
                        [parameter.ymax,parameter.ymin,parameter.K, parameter.n, parameter.alpha,parameter.beta] = parameter_list
                        for option in item[1]:
                            option_coef = option["value"]
                            option_exe_name = "parameter." + option["name"].replace(" ","_") + "(" + str(option_coef) + ")"
                            exec(option_exe_name)
                        # print(exec(option_exe_name).ymax)
                        for para in parameters:
                            if para["name"] == "ymax":
                                para["value"] = parameter.ymax
                            if para["name"] == "ymin":
                                para["value"] = parameter.ymin
                            if para["name"] == "alpha":
                                para["value"] = parameter.alpha
                            if para["name"] == "beta":
                                para["value"] = parameter.beta
                            if para["name"] == "K":
                                para["value"] = parameter.K
                            if para["name"] == "n":
                                para["value"] = parameter.n
                        row["parameters"] = parameters
            file.write(str(row) + '\n')
    file.close()
    
    file = open(os.path.join(in_dir,modified_gate_txt_file),'r', encoding = "utf-8")
    lines = file.readlines()
    data_list = list()
    for line in lines:
        data = ast.literal_eval(line)
        data_list.append(data)

    data_json = json.dumps(data_list, ensure_ascii = False, indent = 4)
    with open(os.path.join(in_dir, modified_gate_file_path), 'w', encoding = "utf-8") as f:
        f.write(data_json)
    f.close()

#########################################################
######################### MAIN ##########################
################ get the original score #################
#########################################################

best_score = 0
best_chassis = None
best_input_signals = None
best_gates = None
best_logic_dict = None

for chassis in chassis_name:
    in_ucf = in_ucf
    input_sensor_file = input_sensor_file
    output_device_file = f"{chassis}.output.json"
    q = CelloQuery(
        input_directory=in_dir,
        output_directory=out_dir,
        verilog_file=v_file,
        compiler_options=options,
        input_ucf=in_ucf,
        input_sensors=input_sensor_file,
        output_device=output_device_file,
        logging=True,
    )
    signals = q.get_input_signals()
    signal_pairing = list(combinations(signals, signal_input))
    for signal_set in signal_pairing:
        signal_set = list(signal_set)
        q.set_input_signals(signal_set)
        q.get_results()
        try:
            res = CelloResult(results_dir=out_dir)
            if res.circuit_score > best_score:
                print(res.part_names)
                best_score = res.circuit_score
                best_chassis = chassis
                best_input_signals = signal_set
                best_gates = res.part_names
                best_logic_dict = res.logic_dict
        except:
            pass
        q.reset_input_signals()
    print("-----")
print(f"Best Score: {best_score}")
print(f"Best Chassis: {best_chassis}")
print(f"Best Input Signals: {best_input_signals}")
print(f"Best Gates: {best_gates}")
print(f"Best Logic Dict: {best_gates}")

file = open(os.path.join(out_dir, result_txt_file),'w')
file.write(f"Best Score: {best_score}\n")
file.write(f"Best Chassis: {best_chassis}\n")
file.write(f"Best Input Signals: {best_input_signals}\n")
file.write(f"Best Gates: {best_gates}\n")
file.write(f"Best Logic Dict: {best_gates}\n")
file.close()


#########################################################
################ get the modified score #################
#########################################################


# sensor_opt_list = get_signal_option(signal_option_file)
gate_opt_list = get_gate_option(gate_option_file)
# print(opt_list)
# modify_signal(sensor_opt_list,input_sensor_file,modified_signal_file)
modify_gate(gate_opt_list,in_ucf,modified_gate_file)

best_score = 0
best_chassis = None
best_input_signals = None
best_gates = None
best_logic_dict = None

for chassis in chassis_name:
    in_ucf = modified_gate_file
    input_sensor_file = input_sensor_file
    # input_sensor_file = modified_signal_file
    output_device_file = f"{chassis}.output.json"
    q = CelloQuery(
        input_directory=in_dir,
        output_directory=out_dir,
        verilog_file=v_file,
        compiler_options=options,
        input_ucf=in_ucf,
        input_sensors=input_sensor_file,
        output_device=output_device_file,
        logging=True,
    )
    signals = q.get_input_signals()
    signal_pairing = list(combinations(signals, signal_input))
    for signal_set in signal_pairing:
        signal_set = list(signal_set)
        q.set_input_signals(signal_set)
        q.get_results()
        try:
            res = CelloResult(results_dir=out_dir)
            if res.circuit_score > best_score:
                print(res.part_names)
                best_score = res.circuit_score
                best_chassis = chassis
                best_input_signals = signal_set
                best_gates = res.part_names
                best_logic_dict = res.logic_dict
        except:
            pass
        q.reset_input_signals()
    print("-----")
print(f"Best Score: {best_score}")
print(f"Best Chassis: {best_chassis}")
print(f"Best Input Signals: {best_input_signals}")
print(f"Best Gates: {best_gates}")
print(f"Best Logic Dict: {best_gates}")

file = open(os.path.join(out_dir, modified_result_txt_file),'w')
file.write(f"Best Score: {best_score}\n")
file.write(f"Best Chassis: {best_chassis}\n")
file.write(f"Best Input Signals: {best_input_signals}\n")
file.write(f"Best Gates: {best_gates}\n")
file.write(f"Best Logic Dict: {best_gates}\n")
file.close()

