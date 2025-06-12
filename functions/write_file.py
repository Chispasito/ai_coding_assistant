import os

def write_file(working_directory, file_path, content):
    joined_path = os.path.join(working_directory, file_path)
    
    # if not os.path.isfile(os.path.abspath(joined_path)):
        # return f'Error: File not found or is not a regular file: "{file_path}"'
    if not os.path.abspath(joined_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    else: 
        string_concat = "Cannot read"
        with open(joined_path, "w+") as f:
            f.write(content)
            string_concat = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        return string_concat


'''
test.py
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
'''