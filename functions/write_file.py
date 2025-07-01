import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file within the working directory. The file must be accessible within the working directory for security.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory. File access is restricted to files within the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the specified file.",
            ),
        },
    ),
)


def write_file(working_directory, file_path, content):
    working_path = os.path.abspath(working_directory)
    if os.path.isdir(working_path):
        abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
        if not abs_file_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        try:
            with open(abs_file_path,"w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except:
            return f'Error: Could not write to "{file_path}"'
    else:
        return f'Error: Working directory does not exist'