import os
import time

def display_loading():
    print("Loading...")

def run_main_py():
    run_folder = "Run"
    main_py = "main.py"
    
    # Check if the 'Run' folder exists
    if os.path.exists(run_folder) and os.path.isdir(run_folder):
        os.chdir(run_folder)  # Change the current working directory to 'Run'
        
        # Check if 'main.py' exists in the 'Run' folder
        if os.path.exists(main_py) and os.path.isfile(main_py):
            print(f"Running {main_py} in {run_folder}")
            os.system(f"python {main_py}")
        else:
            print(f"Error: {main_py} not found in {run_folder}")
    else:
        print(f"Error: {run_folder} folder not found")

if __name__ == "__main__":
    display_loading()
    time.sleep(2)  # Simulate a loading delay (you can adjust this value)
    run_main_py()
