import subprocess


MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch', '-M', 'main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
subprocess.call(['git', 'tag', "{{ cookiecutter.project_version }}")


print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")
