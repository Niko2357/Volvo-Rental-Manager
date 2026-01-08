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


def copy_to_dist(path, is_folder=False):
    destination = os.path.join('dist', path)
    if os.path.exists(path):
        if is_folder:
            if os.path.exists(destination):
                shutil.rmtree(destination)
            shutil.copytree(path, destination)
            print(f"Folder {path} copied to dist.")
        else:
            shutil.copyfile(path, destination)
            print(f"File {path} copied to dist.")
    else:
        print(f"Source {path} not found!")


copy_to_dist('config.json')
copy_to_dist('machine_logo.ico')
copy_to_dist('Database/Data', is_folder=True)
