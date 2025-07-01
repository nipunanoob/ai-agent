import os

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