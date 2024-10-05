# -*- coding:utf-8 -*-

import os


class Path(str):
    """
    파일 시스템 경로를 나타낸다.
    운영체제에 상관 없이 파일 경로를 다룰 수 있게 해 준다.

    이 클래스는 Python 3에 존재하는 `pathlib.Path` 클래스의 단순화된 버전이다.
    Python 2.7에는 `pathlib` 모듈이 없기 때문에 필요하다.

    기능:
    - 경로 결합
    - 부모 디렉토리 및 이름 가져오기
    - 경로 존재 여부 확인
    - 파일 여부 및 디렉토리 여부 확인
    """

    # `open`, `os.walk`, `os.makedirs` 등
    # 파이썬 2.7의 많은 내장 함수들은 경로를 `str`로 받는다.
    # `str`을 상속받음으로써 이 클래스 인스턴스는 `str`처럼 행동한다.

    def __init__(self, path):
        # type: (str) -> None
        self._path = os.path.abspath(path)

    def __str__(self):
        # type: () -> str
        return self._path

    def __repr__(self):
        # type: () -> str
        return "Path({})".format(self._path)

    def __div__(self, other):
        # type: (str) -> Path
        return Path(os.path.join(self._path, other))

    @property
    def parent(self):
        # type: () -> Path
        return Path(os.path.dirname(self._path))

    @property
    def name(self):
        # type: () -> str
        return os.path.basename(self._path)

    def exists(self):
        # type: () -> bool
        return os.path.exists(self._path)

    def is_file(self):
        # type: () -> bool
        return os.path.isfile(self._path)

    def is_dir(self):
        # type: () -> bool
        return os.path.isdir(self._path)


# # 사용 예
# p = Path('/home/user/documents')

# print("경로:", p)  # 출력: /home/user/documents
# print("부모 디렉토리:", p.parent)  # 출력: /home/user
# print("이름:", p.name)  # 출력: documents
# print("존재 여부:", p.exists())  # 출력: [존재 여부]
# print("파일 여부:", p.is_file())  # 출력: [파일 여부]
# print("디렉토리 여부:", p.is_dir())  # 출력: [폴더 여부]

# p2 = p / 'file.txt'
# print("결합된 경로:", p2)  # 출력: /home/user/documents/file.txt
