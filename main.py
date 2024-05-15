# Scenario
# Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
# Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
# Apply your decorator to those functions to ensure that the time of the function executions can be monitored.

###################################################################################################################################################

import datetime

def deco (fun):
    def wrapp(v1,v2):
        print(datetime.datetime.now().strftime("%Y-%M-%d %H:%M:%S"))
        return fun(v1,v2)
    return wrapp

@deco
def fun1 (v1,v2):
    return (v1+v2)

@deco
def fun2 (v1,v2):
    return (v1-v2)

@deco
def fun3 (v1,v2):
    return (v1*v2)

@deco
def fun4 (v1,v2):
    return (v1/v2)



print(fun1(15,5))
print(fun2(15,5))
print(fun3(15,5))
print(fun4(15,5))