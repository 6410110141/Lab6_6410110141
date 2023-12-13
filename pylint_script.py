# pylint_script.py

import subprocess
import sys

def run_pylint():
    """
    Run Pylint on Python files in the current directory.
    """
    try:
        subprocess.run(["pylint", "--load-plugins", "pylint.extensions.multiprocessing", "."], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running pylint: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pylint()
