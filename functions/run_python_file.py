import os
import subprocess

def run_python_file(working_directory='./calculator', file_path=None):
    if file_path is None:
        return 'Error: file_path parameter is required'
    joined_path = os.path.join(working_directory, file_path)
    
    if not os.path.isfile(os.path.abspath(joined_path)):
        return f'Error: File "{file_path}" not found.'
    elif not os.path.abspath(joined_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not file_path[-3:] == ".py":
        return f'Error: "{file_path}" is not a Python file.'
    else: 
        string_concat = "pass"
        run_values = (subprocess.run(["python3", joined_path], capture_output=True, timeout=30.0))
        return f"STDOUT: {run_values.stdout}\nSTDERROR: {run_values.stderr}"
    
'''
tests

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py")) # (this should return an error)
print(run_python_file("calculator", "nonexistent.py")) # (this should return an error)
'''