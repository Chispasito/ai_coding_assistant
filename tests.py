# from subdirectory.filename import function_name
from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *

def call_function(function_call_part, verbose=False):
    function_map = {"get_file_content": get_file_content, "get_files_info": get_files_info, "run_python_file": run_python_file, "write_file": write_file}
    return 

# print(get_files_info("calculator", "."))
# print(get_files_info("calculator", "pkg"))
# print(get_files_info("calculator", "/bin"))
# print(get_files_info("calculator", "../"))

# print(get_file_content("calculator", "main.py"))
# print(get_file_content("calculator", "pkg/calculator.py"))
# print(get_file_content("calculator", "/bin/cat"))

# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

# print(run_python_file("calculator", "main.py"))
# print(run_python_file("calculator", "tests.py"))
# print(run_python_file("calculator", "../main.py")) # (this should return an error))
# print(run_python_file("calculator", "nonexistent.py")) # (this should return an error))