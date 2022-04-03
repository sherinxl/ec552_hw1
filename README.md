# CelloAPI 2 Patch Package

1. What it is and what it does 
 This package is a modification and addition to th eexisting framework of CelloAPI2. CelloAPI2 is python interface for interacting with [Cellov2](https://github.com/CIDARLAB/Cello-v2), a CAD Tool for designing and scoring Genetic Circuits.
 This package perfroms the folling oprations:
 - Fix:
    - the problem that some path cannot reach via root in window
 - Add:
    - An Input Library contains input file examples
    - Four verilog files: or.v, nor.v, eq.v, and nand.v to the Input Library for users to use directly
    - Function to modify sensors and devices in the genetic circuit
 
2. File description
```
├── celloapi2   			# modified celloapi2.py
├── input
│   ├── and.v				# a verilog file that describes the genetic circuit
│   ├── Eco1C1G1T1.input.json		# a *.input.json file that describes the input signals into the circuit
│   ├── Eco1C1G1T1.output.json		# a *.output.json file that describes the resultant output singal at the end of the circuit
│   ├── Eco1C1G1T1.UCF.json		# a user-constraint-file (UCF) that describes the target vector
│   ├── Eco1C1G1T1.signal_option.json	# a *.signal_option.json file that describes the operations applied to modify the sensors
│   ├── Eco1C1G1T1.gate_option.json	# a *.gate_option.json file that describes the operations applied to modify the gates
│   └── options.csv			# a CSV describing various inputs to the compiler
├── input_library			# a library contains some input file examples
├── main.py
├── output				# the folder contains the output files
├── example_data			# an example folder contains an input folder, main.py, and output folder	
│   ├── input
│   ├── main.py	
│   └── output
└── README.md
```

3. Installation
 - Requirements
   - Prerequisites: Docker
   - Python 3.8+

 - Commands
 
 	- `  $ docker pull cidarlab/cello-dnacompiler:latest`
 
  	- `  $ pip install celloapi2`

4. Additional Function and File Description
 - sensor singal operation:
     *.signal_option.json: a .json file declear the operations to the sensors, contains one or multiple operation statements
        each operation statement containts:
	  - object: what sensor would be modify, one sensor at a time
	  - operation: what operations would be applied, one or multiple operations, The final result will be manipulated and calculated according to the order
	  - value: the parameters for the operations
        notice:
	  - if the user wishes to test the different results that may result from different operations applied to the same sensor, the user needs to declare multiple operation statements with the object of the sensor
	  - if the user wants to test the superimposed effect of different operations on the same receptor at the same time, the user needs to declear multiple options and values to one operation statement
          - new opeartion statements will not overwrite the previous statements
 	  - each operation statement will modify the original sensor once, while retaining the information of the original sensor
          - the number of sensors in the new input file will be the sum of the number of sensors in the original input file and the number of operation statements
     built-in functions of main.py: keep the original sensor and add the modified sensor and information
     *.signal_modified.json: a .json output file contains the original and modified sensor. 
	  - this file is output to the input folder as an input file to build and evaluate the genetic circuit
 - gate singal operation:
     *.gate_option.json: a .json file declear the operations to the gates, contains one or multiple operation statements
        each operation statement containts:
	  - object: what gate would be modify, one gate at a time
	  - operation: what operations would be applied, one or multiple operations, The final result will be manipulated and calculated according to the order
	  - value: the parameters for the operations
        notice:
	  - the user cannot test the different results that may result from different operations applied to the same sensor
	  - if the user wants to test the superimposed effect of different operations on the same receptor at the same time, the user can to declear multiple options and values to one operation statement or declear multiple operation statements
          - the operation effect on one gate will be interative, old result will be removed, the original gate will not be kept
          - the number of gates in the new input file will be the same as the number of gates in the original gate input library
     built-in functions of main.py: modify the original gate information
     *.gate_modified.UCF.json: a .json output file contains the modified gates 
	  - this file is output to the input folder as an input file to build and evaluate the genetic circuit
 - main.py:
     - modify and update the sensor input file and the gate library
     - generate the possible circuits statisify the logic gate
     - score the circuit
     - send back the score, input combination, genetic gates and the logic table for the best score
 - output folder:
     - multiple folders may be generated in the output folder, each of which will contain a genetic circuit and the associated results
     - as new inputs and gates combinations are used for computation in main.py, the previous output files are moved to a new folder in the directory
     - all combinations of circuits generated during the process that satisfy the logic gate are saved and can be traced

5. Problem and Directions
 - the computation time to generate all circuits that satify the logic gate is too long
 - connot specify one circuit or device in the circuit for modification or development
 - when the verilog file is the logic circuit other than the and gate, some of the output figures and files have the incorrect names 

 - directions: add more user freedom, such as specifying a circuit for modification after the user has obtained all viable circuits in the first round
               develop the algorithm for faster computation speed
