import pandas
import sklearn as sk

print(sk.__version__)  # it will tell the version of sklearn

"""
From where do we get this module
to know this is there is a module  >>>> sys
"""

import sys

print(sys.path)
# the above line will print the hierarchy of the paths, from where till where it check the
# imported module is there or not
# means print the path of the imported module

import T29_RockPaperScissor as rockpaperscissor

rockpaperscissor  # this line is directly calling the function of the
# module T29_RockPaperScissor

"""
interpreter first find the imported file in the directory where the current file is running
so if u imported a module an du kept another python file name withe the same name as 
of the module imported

then it will first search that module in the directory in which the current file is 
running and it got the file which you have imported then it will give error
if the required function not present in the in that file

so we won't give the python file name as same as the modules present in the 
python  
"""

