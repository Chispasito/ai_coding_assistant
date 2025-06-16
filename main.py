import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *

function_map = {
    "get_file_content": get_file_content, 
    "get_files_info": get_files_info, 
    "run_python_file": run_python_file, 
    "write_file": write_file
}

def call_function(function_call_part, verbose=False):
    try:
        return function_map[function_call_part.name](**function_call_part.args)
    except Exception as e:
        return e

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    model_name = "gemini-2.0-flash-001"
    client = genai.Client(api_key=api_key)

    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative toworking directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """    
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Lists file content in the specified directory along, constrained to 10,000 characters.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to get file content from, relative to the working directory. If not provided, get file content in the working directory itself.",
                ),
            },
        ),
    )

    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes to file in specified directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to write content to, relative to the working directory. If not provided, write to file in the working directory itself.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="the actual content to write"
                ),
            },
        ),
    )

    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Runs python file in specified directory",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to run python file from, relative to the working directory. If not provided, run file in the working directory itself.",
                ),
            },
        ),
    )

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,schema_get_file_content, schema_write_file, schema_run_python_file,
        ]
    )

    config_setup=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)

    if len(sys.argv) <= 1:
        print("Failure 1: No arguments")
        sys.exit(1)

    user_prompt = sys.argv[1]
    
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=config_setup,
    )
    
    if len(sys.argv) > 2 and "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}\n"
              f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
              f"Response tokens: {response.usage_metadata.cached_content_token_count}"
        )

    if response.function_calls and len(response.function_calls) > 0:
        # print("function calls ---: ", response.function_calls)
        for function_call_part in response.function_calls:
            if len(sys.argv) > 2 and "--verbose" in sys.argv:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            print(call_function(function_call_part))
    print(response.text)

main()