# -*- coding:utf-8 -*-
# 라이노 7에서의 구형 파이썬 2를 지원하기 위한 코드
import polyfill  # pylint:disable=C0411

# 이렇게 하위 아이템을 내보낸다고 작성하면
# 상위 모듈인 `logic`에서 직접 아이템을 불러들일 수 있다.
# 예를 들어, `from logic import say_hi`가 가능해진다.
from .sample_module import say_hi
