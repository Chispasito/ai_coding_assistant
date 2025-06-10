import os
def get_files_info(working_directory, directory=None):
    # print(os.listdir(os.path.join(working_directory, directory)))
    # print(os.path.abspath(os.path.join(working_directory, directory)))
    
    joined_dir = os.path.join(working_directory, directory)
    
    if not os.path.isdir(os.path.abspath(joined_dir)):
        return f'Error1: "{directory}" is not a directory'
    elif not os.path.abspath(joined_dir).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else: 
        string_concat = ""
        for i in os.listdir(joined_dir):
            string_concat += "-" + str(i) + ": file_size=" + \
            str(os.path.getsize(os.path.join(joined_dir, i))) + " bytes, " + \
            "is_dir=" + str(os.path.isdir(os.path.join(joined_dir, i))) + "\n"
        return string_concat