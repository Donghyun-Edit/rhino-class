# -*- coding:utf-8 -*-

"""
파이썬 3에 존재하는 라이브러리들을 흉내내어 그 기능들을
파이썬 2.7 기반의 Rhino IronPython에서도 비슷하게 사용하기 위한 모듈이다.
이 모듈은 가장 밑단에서 파이썬 버전 간 차이를 채우는 역할만 하도록,
기능을 최대한 적게 유지하는 것이 좋다.

현재 구현된 가짜 모듈은 다음과 같다.

- `typing`: 파이썬 3.5에서 추가된 타입 힌트를 지원하는 모듈
- `typing_extensions`: 파이썬 3.5에서 추가된 타입 힌트 확장 모듈
- `enum`: 파이썬 3.4에서 추가된 열거형을 지원하는 모듈
- `pathlib`: 파이썬 3.4에서 추가된 파일 경로를 다루는 모듈
"""

import os
import sys
import abc


# 현재 불러들여진 모듈들 중 `polyfill`을 제거한다.
# `import polyfill` 선언을 할 때,
# 이 모듈이 새롭게 다시 불러들여지도록 하기 위함이다.
del sys.modules["polyfill"]

# `sys.path`에 Polyfill 모듈 디렉토리를 추가한다.
# 파이썬 3에서 유용하지만,
# 파이썬 2에서는 존재하지 않는 일부 내장 라이브러리들의
# 가짜 버전을 Import할 수 있도록 해 준다.
major_version = sys.version_info[0]
if major_version == 2:
    polyfill_dir = os.path.dirname(__file__)
    if polyfill_dir not in sys.path:
        sys.path.append(polyfill_dir)

# 파이썬 2.7에서 모듈은 존재하지만,
# 일부 구현되지 않은 기능을 몽키패치한다.
abc.ABC = object  # Abstract base class 타입 체킹
