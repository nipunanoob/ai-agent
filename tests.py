import unittest
from functions.get_files_info import get_files_info, get_files_content

class TestAIAgent(unittest.TestCase):
    def test_get_files_info_directory_path(self):
        expected = f"Result for current directory:\n - main.py: file_size=575, is_dir=False\n - tests.py: file_size=1342, is_dir=False\n - lorem.txt: file_size=20074, is_dir=False\n - pkg: file_size=4096, is_dir=True"
        actual = get_files_info("calculator",".")
        self.assertEqual(expected, actual)
    
    def test_get_files_info_path_subdirectory_path(self):
        expected = f"Result for 'pkg' directory:\n - __pycache__: file_size=4096, is_dir=True\n - calculator.py: file_size=1737, is_dir=False\n - render.py: file_size=766, is_dir=False"
        actual = get_files_info("calculator","pkg")
        self.assertEqual(expected, actual)
    
    def test_get_files_info_path_does_not_exist(self):
        expected = f"Result for '/bin' directory:\n    Error: Cannot list \"/bin\" as it is outside the permitted working directory"
        actual = get_files_info("calculator","/bin")
        self.assertEqual(expected, actual)

    def test_get_files_info_path_outside_working_directory(self):
        expected = f"Result for '../' directory:\n    Error: Cannot list \"../\" as it is outside the permitted working directory"
        actual = get_files_info("calculator","../")
        self.assertEqual(expected, actual)
    
    def test_get_files_content_outside_working_directory(self):
        expected = f'Error: Cannot read "/bin/cat" as it is outside the permitted working directory'
        actual = get_files_content("calculator", '/bin/cat')
        self.assertEqual(expected, actual)
        print(actual)
    
    
    def test_get_files_content_filepath_does_not_exist(self):
        expected = f'Error: File not found or is not a regular file: "fake.py"'
        actual = get_files_content("calculator","fake.py")
        self.assertEqual(expected, actual)


    def test_get_files_content_filepath_does_exist(self):
        actual = get_files_content("calculator","main.py")
        print(actual)


    def test_get_files_content_filepath_inside_subdirectory_does_exist(self):
        actual = get_files_content("calculator","pkg/calculator.py")
        print(actual)


    
if __name__ == "__main__":
    unittest.main()