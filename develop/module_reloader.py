import os
import importlib
import sys
from typing import Optional

import Rhino

from .constants import ROOT_DIR


# 성능 최적화를 위해 재로딩할 폴더를 제한한다.
# `ROOT_DIR`의 바로 아래 폴더만을 적어야 한다.
RELOAD_FOLDERS = ["logic", "develop"]


def get_module_name(subdir, file_name):
    # type: (str, str) -> Optional[str]
    parent = subdir.replace(str(ROOT_DIR) + os.sep, "").replace(os.sep, ".")
    if not file_name.endswith(".py"):
        return None
    if file_name == "__init__.py":
        return parent
    base_name = file_name.replace(".py", "")
    return "{}.{}".format(parent, base_name)


def perform_reload():
    # type: () -> None

    to_delete = []
    for module_name in sys.modules:
        if any(module_name.startswith(f) for f in RELOAD_FOLDERS):
            to_delete.append(module_name)
    for module_name in to_delete:
        del sys.modules[module_name]

    for reload_folder in (ROOT_DIR / f for f in RELOAD_FOLDERS):
        for subdir, _, filenames in os.walk(reload_folder):
            for filename in filenames:
                module_name = get_module_name(subdir, filename)
                if module_name is None:
                    continue
                print(module_name)
                # 중복 리로드 막기
                if module_name in sys.modules:
                    continue
                try:
                    importlib.reload(importlib.import_module(module_name))
                except Exception:  # pylint:disable=broad-exception-caught
                    pass


def reload_modules(trigger):
    # type: (bool) -> None

    if Rhino.Runtime.HostUtils.RunningAsRhinoInside:  # type: ignore
        return

    if not trigger:
        return

    perform_reload()
