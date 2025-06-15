import os

def get_files_info(working_directory, directory=None):
    working_directory = "ai_coding_assistant"
    joined_dir = os.path.join(working_directory, directory)
    
    if not os.path.isdir(os.path.abspath(joined_dir)):
        return f'Error1: "{directory}" is not a directory'
    elif not os.path.abspath(joined_dir).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else: 
        string_concat = ""
        dir_list = os.listdir(joined_dir)
        for i in range(len(dir_list)):
            string_concat += "-" + str(dir_list[i]) + ": file_size=" + \
            str(os.path.getsize(os.path.join(joined_dir, dir_list[i]))) + " bytes, " + \
            "is_dir=" + str(os.path.isdir(os.path.join(joined_dir, dir_list[i])))
            if not i == len(dir_list) -1:
                string_concat += "\n"
        return string_concat