import os
import subprocess


MESSAGE_COLOR = "\x1b[44m"
YML_COLOR = "\x1b[38;5;190m"
OS_COLOR = "\x1b[42m"
INFO_COLOR = "\x1b[38;5;219m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch', '-M', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', '(init) 🎉 Begin a project'])
subprocess.call(['git', 'tag', "{{ cookiecutter.project_version }}"])

print(f"{INFO_COLOR}Please enter the project folder with this command.{RESET_ALL}")
print(f"{OS_COLOR}cd { os.getcwd() }{RESET_ALL}")
print(f"{INFO_COLOR}And then, copy and paste into the terminal to install the dependencies. If you prefer, you can use mamba instead of conda.{RESET_ALL}")
print(f"{YML_COLOR}conda env create --file environment.yml{RESET_ALL}")
print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")
