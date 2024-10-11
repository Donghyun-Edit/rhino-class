# -*- coding:utf-8 -*-
# 라이노 7에서의 구형 파이썬 2를 지원하기 위한 호환 코드
from __future__ import division, absolute_import
import polyfill  # pylint:disable=C0411

# 이와 같이 하위 아이템을 내보낼 수 있다.
# 이를 통해 외부에서 `from logic import say_hi`로
# 불러들이는 것이 가능해진다.
from .sample_module import say_hi, draw_pentagon
