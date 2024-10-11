# -*- coding:utf-8 -*-
# Compatibility code for Python 2 in Rhino 7
from __future__ import division, absolute_import
import polyfill  # pylint:disable=C0411,W0611

import os
import importlib
import sys
from typing import Optional
from pathlib import Path

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
                prepend_startlines(reload_folder / subdir / filename)
                print(module_name)
                # 중복 리로드 막기
                if module_name in sys.modules:
                    continue
                try:
                    # pylint:disable=undefined-variable
                    reload(importlib.import_module(module_name))  # type: ignore
                except Exception:  # pylint:disable=broad-exception-caught
                    pass


def prepend_startlines(filepath):
    # type: (Path) -> None

    # 라이노 8의 신형 파이썬 3에서는 호환성 코드가 필요 없다.
    if sys.version_info.major >= 3:
        return

    # 파이썬 2 이하에서는 모든 파일에 호환성 코드를 작성한다.
    with open(filepath, "rb") as file:
        filelines = file.read().decode("utf-8").split("\n")
        filelines = [l.strip("\r") for l in filelines]

    # 이미 잘 추가되어 있다면 신경 쓰지 않는다.
    expected_start_lines = [
        "# -*- coding:utf-8 -*-",
        "# Compatibility code for Python 2 in Rhino 7",
        "from __future__ import division, absolute_import",
        (
            "import polyfill  # pylint:disable=C0411"
            if filepath.name == "__init__.py"
            else "import polyfill  # pylint:disable=C0411,W0611"
        ),
        "",
    ]
    line_count = len(expected_start_lines)
    if filelines[:line_count] == expected_start_lines:
        return

    # 호환성 코드를 파일에 추가한다.
    freshlines = expected_start_lines + filelines
    with open(filepath, "wb") as file:
        file.write("\n".join(freshlines).encode("utf-8"))


def reload_modules(trigger):
    # type: (bool) -> None

    if Rhino.Runtime.HostUtils.RunningAsRhinoInside:  # type: ignore
        return

    if not trigger:
        return

    perform_reload()
