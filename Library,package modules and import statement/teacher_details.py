import os,sys

from os.path import join,abspath,dirname
 
parent_dir_path = abspath(join(dirname(__file__),".."))

sys.path.insert(0, parent_dir_path)

from student import student_details

def teacher():
    print("This is the teacher's details")
    
student_details.student()