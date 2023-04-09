import os
import sys
import shutil
import subprocess
import atexit
from importlib import import_module


cwd = os.path.dirname(os.path.realpath(__file__)) + '/packages'


def clean():
    if os.path.exists(cwd):
        shutil.rmtree(cwd)


def require(name):
    atexit.register(clean)
    if not os.path.exists(cwd):
        os.mkdir(cwd)

    subprocess.run(['pip', 'install', '--no-cache-dir', name, '-t', cwd])
    sys.path.insert(0, cwd)

    return import_module(name)


clean()
