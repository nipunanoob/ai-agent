import os
from google.genai import types

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

def get_files_info(working_directory, directory=None):
    working_path = os.path.abspath(working_directory)
    if os.path.isdir(working_path):
        if (directory == None):
            file_content_string = get_file_summary(working_path)
            return "Result for current directory:" + file_content_string
        else:
            full_path = os.path.abspath(os.path.join(working_path, directory))
            if not full_path.startswith(working_path):
                return f'Result for \'{directory}\' directory:\n    Error: Cannot list "{directory}" as it is outside the permitted working directory'
            if (not os.path.isdir(full_path)):
                return f'Error: "{directory}" is not a directory'
            file_content_string = get_file_summary(full_path)
            if full_path == working_path:
                return "Result for current directory:" + file_content_string
            else:
                return f"Result for '{directory}' directory:" + file_content_string
    else:
        return f'Error: Working directory does not exist'
    
def get_file_summary(path):
    directory_contents = os.listdir(path)
    output_string = ""
    for content in directory_contents:
        try:
            content_path = os.path.join(path, content)
            content_size = os.path.getsize(content_path)
            content_is_dir = os.path.isdir(content_path)
            output_string += f"\n - {content}: file_size={content_size}, is_dir={content_is_dir}"
        except:
            print(f"Error: Script unable to read {content} as it has no read permission")
    return output_string


    