import person
#other module import ways
from os import path
import os.path
import os.path as location

import sys

print(dir(person))
print(__file__)
print('Name: %s' %person.getName(), __name__)


if path.exists('person.py'):
 print('Person.py exists')

print(sys.argv)            #this is a list of arguments
print(sys.path)            # ['/Volumes/SSD2/Projects/Python/Tutorial/modules', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages']
print(sys.platform)        # darwin


