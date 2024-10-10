# -*- coding:utf-8 -*-
# 라이노 7에서의 구형 파이썬 2를 지원하기 위한 호환 코드
from __future__ import division, absolute_import
import polyfill  # pylint:disable=C0411,W0611

from pathlib import Path

# 이 상수 값은 이 모듈이 `ROOT_DIR` 기준으로
# `develop/constants.py`의 상대 경로를 가진다는 전제로 작성되었다.
ROOT_DIR = Path(__file__).parent.parent
