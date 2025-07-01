from functions.run_python  import run_python_file

def main():
    # Test reading main.py
    result1 = run_python_file("calculator", "main.py")
    print(result1)
    
    # Test reading tests.py
    result2 = run_python_file("calculator", "tests.py")
    print(result2)

    # Test reading ../main.py which will raise an error
    result3 = run_python_file("calculator", "../main.py")
    print(result3)

    # Test reading nonexistent.py which will raise an error
    result4 = run_python_file("calculator", "nonexistent.py")
    print(result4)

if __name__ == "__main__":
    main()