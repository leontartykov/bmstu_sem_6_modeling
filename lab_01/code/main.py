from differ_equation import *
from input_output import *

if __name__ == "__main__":
    values = input_values()
    cauchy_equation = DifferEquation(values[0], values[1], values[2])
    cauchy_equation.get_table()