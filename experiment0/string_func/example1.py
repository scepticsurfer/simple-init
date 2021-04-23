# example1.py
# this file works without __init__.py 
# but only if it's in the same folder with functions

import stringLength
import stringToLower
import stringToUpper

some_string = "Hello, Universe!"

print(stringLength.stringLength(some_string))
print(stringToLower.stringToLower(some_string))
print(stringToUpper.stringToUpper(some_string))