# convert-to-DIMAC
Python script
convert a txt file with "*", "0", "1" instead of values for the variables into DIMAC form where:
"*": the variable does not exist
"0": the variable is negative
"1": the variable is positive
example:
*****01010
1111000***
0001111***
will be
p cnf 10 3
-6 7 -8 9 -10 0
 1 2 3 4 -5 -6 -7 0
 -1 -2 -3 4 5 6 7 0

Try with given files in python editor for file location
