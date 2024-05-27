# -*- coding: utf-8 -*-
import os, pathlib, shutil, py_compile


root_dir = pathlib.Path(__file__).resolve().parent
build_dir = root_dir.joinpath("build")
if __name__ == "__main__":
    # copy requirements file
    shutil.copyfile(str(root_dir.joinpath("requirements.txt")), str(build_dir.joinpath("requirements.txt")))

    # copy apps directory
    apps_dir = build_dir.joinpath("apps")
    if apps_dir.exists():
        shutil.rmtree(str(apps_dir))

    shutil.copytree(str(root_dir.joinpath("apps")), str(apps_dir))

    # remove __pycache__ directories
    for cache_dir in apps_dir.glob("**/__pycache__"):
        shutil.rmtree(cache_dir)

    # compile .py to .pyc
    for py_file in apps_dir.glob("**/*.py"):
        py_compile.compile(str(py_file), str(py_file) + "c")
        os.remove(str(py_file))

    py_compile.compile(str(root_dir.joinpath("server.py")), str(build_dir.joinpath("server.pyc")))
