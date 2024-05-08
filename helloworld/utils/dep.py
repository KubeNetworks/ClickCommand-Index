from importlib import import_module
import subprocess
import sys


def check_and_install(package: str):
    try:
        module = import_module(package)
        print(f"{package} version {module.__path__} is already installed.")
    except ImportError:
        print(f"{package} is not installed. Attempting to install...")
        try:
            index_url = "https://pypi.tuna.tsinghua.edu.cn/simple"  # 指定pip的镜像源
            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--index-url",
                    index_url,
                    package,
                ]
            )
            print(f"{package} installed successfully using index-url: {index_url}")
        except Exception as e:
            print(f"Error installing {package}: {e}")
            sys.exit(1)
