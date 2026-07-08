import os, sys

from os.path import dirname,abspath,join

parent_dir_path = abspath(join(dirname(__file__), ".."))

sys.path.insert(0, parent_dir_path)

#from teacher import teacher_details

def student():
    print("This is the students details")

#teacher_details.teacher()