# -*- coding:utf-8 -*-
import polyfill  # pylint: disable=C0411,W0611

import clr  # pylint: disable=import-error

# pylint: disable=wrong-import-position
clr.AddReference("System.Core")

# pylint: disable=wrong-import-order
import os
import time
from typing import Any

import System
import scriptcontext as sc
from Grasshopper.Kernel import GH_FileWatcher
from Grasshopper.Kernel import GH_FileWatcherEvents

from .module_reloader import perform_reload, RELOAD_FOLDERS


WATCHER_KEY = "module_watcher"
RELOAD_TIME_KEY = "module_watcher_reloaded_at"


class ModuleWatcher:
    def __init__(self):
        # type: () -> None
        self.watcher_list = []
        self.collect_watcher_list()

    def collect_watcher_list(self):
        # type: () -> None
        for reload_folder in RELOAD_FOLDERS:
            self.watcher_list.append(self.create_python_watcher(str(reload_folder)))
            for subdir, dirs, _ in os.walk(reload_folder):
                for d in dirs:
                    dir_name = subdir + os.sep + d
                    self.watcher_list.append(self.create_python_watcher(dir_name))

    def dispose(self):
        # type: () -> None
        for w in self.watcher_list:
            w.Dispose()

    def create_python_watcher(self, dir_name):
        # type: (str) -> Any
        return GH_FileWatcher.CreateDirectoryWatcher.Overloads[  # type: ignore
            System.String,
            System.String,
            GH_FileWatcherEvents,
            GH_FileWatcher.FileChanged,  # type: ignore
        ](
            dir_name,
            "*.py",
            GH_FileWatcherEvents.All,
            lambda *args: self.reload_all(),
        )

    def reload_all(self):
        # type: () -> None
        reloaded_at = sc.sticky[RELOAD_TIME_KEY]
        current_time = time.time()

        # 1초 내의 재시도는 무시한다.
        if current_time < reloaded_at + 1:
            return

        perform_reload()

        sc.sticky[RELOAD_TIME_KEY] = time.time()


def watch_modules(enable):
    # type: (bool) -> None

    sc.sticky[RELOAD_TIME_KEY] = time.time()

    if not enable and WATCHER_KEY in sc.sticky:
        print("Module watcher is disabled")
        sc.sticky[WATCHER_KEY].dispose()
        del sc.sticky[WATCHER_KEY]

    if enable and WATCHER_KEY not in sc.sticky:
        sc.sticky[WATCHER_KEY] = ModuleWatcher()
        print("Module watcher is enabled")
