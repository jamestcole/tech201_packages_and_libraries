# Modules

import os
import math, datetime, sys

working_directory = os.getcwd()
print(working_directory)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.name)


print(datetime.date.today())
print((sys.path))
print(math.remainder(1, 5))
