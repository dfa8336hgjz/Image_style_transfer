import subprocess
import sys

def is_module_installed(module_name):
    try:
        __import__(module_name)
        print(f"{module_name} is installed.")
        return True
    except ImportError:
        print(f"{module_name} is not installed.")
        return False


def install(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
    print(f"Successfully installed {module_name}")
    

def check_modules(module_name):
    check = True
    for i in module_name:
        if not is_module_installed(i):
            try:
                install(i)
            except subprocess.CalledProcessError as e:
                print(f"Error installing {i}. Check if the module name is correct and try again.")
                print(f"Error details: {e}")
                check = False     
    return check