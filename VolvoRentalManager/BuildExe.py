import PyInstaller.__main__
import shutil
import os


"""
This class builds Volvo Manager application and copies configuration file and icon to the same directory.
"""


pyinstaller_args = [
    'main.py',
    '--name=Volvo Manager',
    '--onefile',
    '--windowed',
    '--noconfirm',
    '--clean',
    '--icon=machine_logo.ico',
    '--collect-all', 'cryptography',
    '--collect-all', 'oracledb',
]

PyInstaller.__main__.run(pyinstaller_args)


def copy_file_to_dist(filename):
    source = filename
    destination = os.path.join('dist', filename)
    if os.path.exists(source):
        shutil.copyfile(source, destination)
        print("Copied.")
    else:
        print("File not found.")


copy_file_to_dist('config.json')
copy_file_to_dist('machine_logo.ico')