import os
import subprocess
import importlib.util
import inspect

from utils import paths

def run_methods(file_path):
    error_count = 0
    try:
        spec = importlib.util.spec_from_file_location("module_name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        methods = inspect.getmembers(module, inspect.isfunction)

        if not methods:
            return
        
        for method_name, method in methods:
            try:
                method()
            except Exception as e:
                error_count += 1
                print(f"Error running method {method_name}:\n{str(e)}\n")
                
    except Exception as e:
        print(f"Failed to run methods from {file_path}:\n{str(e)}\n")
    
    return error_count


def run_tests_in_directory(package_name):
    for root, _, files in os.walk(paths.get_main_path("core/" + package_name)):
        for file in files:
            if file.endswith(".py"):
                
                if file == "__init__.py": continue
                
                file_path = os.path.join(root, file)
                print(f"Testing {file_path}")
                
                # error_count = run_methods(file_path)
                
                # if error_count == 0:
                #     print("Testing successful")
                # else:
                #     print(f"{error_count} Error/s in {file_path}")
                
                try:
                    result = subprocess.run(['python', file_path], capture_output=True, text=True)
                    if result.returncode != 0:
                        print(f"Error in {file_path}:\n{result.stderr}\n")
                    else:
                        print("Testing successful")
                except Exception as e:
                    print(f"Failed to run {file_path}:\n{str(e)}\n")

if __name__ == "__main__":
    run_tests_in_directory("modules")
    run_tests_in_directory("utils")