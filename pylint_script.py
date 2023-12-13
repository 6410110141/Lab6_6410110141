# pylint_script.py

import os
import subprocess

def run_pylint():
    python_files = " ".join([file for file in os.listdir() if file.endswith(".py")])
    pylint_command = f"pylint {python_files}"

    try:
        subprocess.run(pylint_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running pylint: {e}")
        exit(1)

if __name__ == "__main__":
    run_pylint()
