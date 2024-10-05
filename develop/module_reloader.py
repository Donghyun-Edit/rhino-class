# -*- coding:utf-8 -*-

import os
import importlib
import sys

import Rhino

from .constants import ROOT_DIR


# 성능 최적화를 위해 재로딩할 폴더 제한
RELOAD_FOLDERS = [
    ROOT_DIR / "logic",
    ROOT_DIR / "develop",
]


def get_module_name(subdir, file_name):
    # type: (str, str) -> str
    base_name = subdir.replace(str(ROOT_DIR) + os.sep, "").replace(os.sep, ".")
    return base_name + "." + file_name.replace(".py", "")


def perform_reload():
    # type: () -> None

    to_delete = []
    for module_name in sys.modules:
        if any(module_name.startswith(f.name) for f in RELOAD_FOLDERS):
            to_delete.append(module_name)
    for module_name in to_delete:
        del sys.modules[module_name]

    for reload_folder in RELOAD_FOLDERS:
        for subdir, _, files in os.walk(reload_folder):
            for f in files:
                if not f.endswith(".py") or f == "__init__.py":
                    continue
                module_name = get_module_name(subdir, f)
                print(module_name)
                # 중복 리로드 막기
                if module_name in sys.modules:
                    continue
                try:
                    # pylint: disable=undefined-variable
                    reload(importlib.import_module(module_name))  # type: ignore
                except Exception:  # pylint: disable=broad-exception-caught
                    pass


def reload_modules(run):
    # type: (bool) -> None

    if Rhino.Runtime.HostUtils.RunningAsRhinoInside:
        return

    # `run`이 거짓일 때 실행하는 것은 버튼을 '놓는 순간' 실행되도록 하기 위함임
    if run:
        return

    perform_reload()
