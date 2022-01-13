#defining the function of paint can calculator
import math

def paint_calc(height, width, cover):
    number_of_paint_cans = (height*width)/cover
    print(int(math.ceil(number_of_paint_cans)))    
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)