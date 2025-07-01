import os
import subprocess
from google.genai import types

schema_run_python = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python script located within the working directory. The script must be accessible within the working directory for security.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the python file to execute, relative to the working directory. Execution is restricted to files within the working directory.",
            ),
        },
    ),
)


def run_python_file(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    if os.path.isdir(working_path):
        abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
        if not abs_file_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        elif not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        else:
            TIMEOUT = 30
            try:
                completed_process = subprocess.run(["python", abs_file_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=30)
                stdout = completed_process.stdout
                stderr = completed_process.stderr
                if completed_process.returncode != 0:
                    return f'Error: Process exited with code {completed_process.returncode}'
                elif stdout == None and stderr == None:
                    return f'No output produced'
                else:
                    output = f'STDOUT: {stdout}\nSTDERR: {stderr}'
                    return output
            except Exception as e:
                return f"Error: executing Python file: {e}"

    else:
        return f'Error: Working directory does not exist'

run_python_file("calculator","main.py")