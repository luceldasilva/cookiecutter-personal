import os
import subprocess


MESSAGE_COLOR = "\x1b[44m"
YML_COLOR = "\x1b[38;5;190m	"
RESET_ALL = "\x1b[0m"
PROJECT = "{{ cookiecutter.project_slug }}"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch', '-M', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
subprocess.call(['git', 'tag', "{{ cookiecutter.project_version }}"])


print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")

print('Entering the project folder')
os.chdir(os.path.join(os.getcwd(), str(PROJECT)))
print("Now that we are in the project, copy and paste into the terminal to install the dependencies. If you prefer, you can use mamba instead of conda.")
print(f"{YML_COLOR}conda env create --file environment.yml{RESET_ALL}")