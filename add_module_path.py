import sys as system, os

now = os.getcwd()

def  path_append():
    system.path.append(now + '\\data_Path')
    system.path.append(now + '\\GameOperate')

path_append()