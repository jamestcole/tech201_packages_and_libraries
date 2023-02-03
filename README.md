# tech201_packages_and_libraries
tech201_packages_and_libraries

## Python Libraries

A library is a set of related modules bundled together which in turn contains useful functions that we can import for our code.
The following code will import random , we can then use the random function from random just like any other function.
```
import random
print(random.random())
```
We can also import the random function from the random module.
```
from random import random
print(random())
```
This is for when we know exactly what we need from our module or library.

Another useful module to import is the math module, which has a large variety of functions to complement pythons operators.

```
import math
num_float =23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
```

## Modules

The following modules and libraries are also useful.

`import os
import math, datetime, sys`

Here we can contain our os module functions in our own functions and call them from other parts of our program.
```
working_directory = os.getcwd()
print(working_directory)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.name)
```

```
print(datetime.date.today())
print((sys.path))
print(math.remainder(1, 5))
```

## Using Modules
A module is a collection of functions that can be used in your code by importing it, or specific functions from the module.
To import all the functions of a module, you can use the * key.

`from modules import *`

By calling our functions made in the previous file, we can print the data gathered by the .os functions.

`return_user_id()`

`return_user_name()`

##pip and packages

pip is Python's package manager and installer

use `pip -V` in the terminal to find version

requests is usfull for scraping data from the web.

`import requests`

This following line will get all the html code from the bbc homepage.

`request_bbc = requests.get("https://www.bbc.co.uk")`

We can print out all of this code by using the following lines.

`print(request_bbc.status_code)`
`print(request_bbc.content)`

