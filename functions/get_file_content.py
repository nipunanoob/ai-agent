import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specified file within the working directory, truncated to a maximum of 10,000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory. File access is restricted to files within the working directory. The content is truncated to a maximum of 10,000 characters.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    if os.path.isdir(working_path):
        abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
        if not abs_file_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            #Read file content and return content as string
            MAX_CHARS = 10000
            try:
                with open(abs_file_path, "r") as f:
                    file_content_string = f.read()
                    count_chars = len(file_content_string)
                    trunc_file_content_string = file_content_string[:MAX_CHARS]
                if count_chars > MAX_CHARS:
                    trunc_file_content_string += '\n[...File "{file_path}" truncated at 10000 characters]'
            except:
                return f'Error: File could not be read : "{file_path}'
            return trunc_file_content_string
    else:
        return f'Error: Working directory does not exist'