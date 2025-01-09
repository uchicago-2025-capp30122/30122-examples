# bad1.py
import json,os,sys
import random    # unused import
from datetime   import datetime

def process_data(x,y,     z):
    a=x+y
    if(z=="test"):
         return a*2
    else:
        return    a

def calculate_stuff( items ):
    total=0
    for i in range(len(items)):   # should use enumerate
        total+=items[i]
    

    return total

result = process_data(1,2,"test")
print(result)
