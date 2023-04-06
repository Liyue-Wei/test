import os

dir_path = os.path.dirname(__file__)
abs_path = os.path.abspath(__file__)
bas_path = os.path.basename(__file__)

print(dir_path)
print(abs_path)
print(bas_path)

def switch(path_in):
    return(path_in.replace('\\', '/'))

dir_path = switch(dir_path)
abs_path = switch(abs_path)

print(dir_path)
print(abs_path)

def fusion(path_in, path_in_2):
    return(os.path.join(path_in, path_in_2).replace('\\', '/'))

fus_path = fusion(dir_path, bas_path)
print(fus_path)