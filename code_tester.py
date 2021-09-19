import os
import subprocess
import sys

# set this to the path where your folders are
FOLDER_PATH = r"/home/kobu/Documents/FIMUNI/IB111/"

# you can add more ignore files
# files with extension .py that you dont want to test SHOULD be added
IGNORE_LIST = [os.path.basename(__file__)]

# set this accordingly to you machine, usually "python" or "python3"
PYTHON_ALIAS = "python3"

# advanced users only: change this if you are saving the script as a bash alias
FOLDER_ARGUMENT_INDEX = 1


class Colors:
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    WARNING = "\033[93m"


def main(filepath):
    for file in sorted(os.listdir(filepath)):
        if file in IGNORE_LIST:
            continue
        if not file.endswith(".py"):
            continue

        p = subprocess.Popen(
            [PYTHON_ALIAS, f"{filepath}/{file}"],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        output, error = p.communicate()

        if error:
            result = f"{Colors.FAIL}{error.decode().split()[-1]} -> {file} FAILED!{Colors.ENDC}"
        else:
            result = f"{Colors.OKBLUE}{file} passed{Colors.ENDC}"

        if output:
            result += (
                f"  ({Colors.WARNING}WARNING: detected print statements{Colors.ENDC})"
            )

        print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(FOLDER_PATH + sys.argv[FOLDER_ARGUMENT_INDEX])
    else:
        print("Pass a folder for testing")
