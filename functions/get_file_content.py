import os

MAX_CHARS = 10000

def get_file_content(working_directory='./calculator', file_path=None):
    joined_path = os.path.join(working_directory, file_path)
    
    if not os.path.isfile(os.path.abspath(joined_path)):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    elif not os.path.abspath(joined_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    else: 
        string_concat = "pass"
        with open(joined_path, "r") as f:
            string_concat = f.read(MAX_CHARS)
        if len(string_concat) == MAX_CHARS:
            string_concat += f"[...File \"{file_path}\" truncated at 10000 characters]"
        return string_concat


'''
test.py 

print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
'''