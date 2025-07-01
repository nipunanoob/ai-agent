import os

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

def get_files_content(working_directory, file_path):
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
            with open(abs_file_path, "r") as f:
                file_content_string = f.read()
                count_chars = len(file_content_string)
                trunc_file_content_string = file_content_string[:MAX_CHARS]
            if count_chars > MAX_CHARS:
                trunc_file_content_string += '\n[...File "{file_path}" truncated at 10000 characters]'
            return trunc_file_content_string

    