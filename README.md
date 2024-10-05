# 라이노 개발 환경

## 개발 환경 구축

VScode에서 터미널 명령어는 `Ctrl+J`로 실행 가능하다.

### 파이썬 준비

[파이썬](https://www.python.org/) 3.9 이상의 버전을 설치한다.

### `poetry` 준비

`poetry`는 가상환경과 패키지 관리를 자동화해 주는 의존성 관리 도구다. 프로젝트 폴더의 `pyproject.toml`이라는 파일에 적힌 그대로 파이썬 환경을 구축하는 것을 돕는다.

```bash
pip install pipx
python -m pipx ensurepath
pipx install poetry
```

변경된 시스템 Path를 VScode가 인식하도록 하기 위해서는 VScode를 한 번 껐다 켜 주어야 한다.

### 파이썬 패키지 설치

```bash
poetry install
```

### VScode에서 Python interpreter를 가상환경 경로로 지정

VScode 창에서 `Ctrl+Shift+P`로 `Python: Select Interpreter` 명령어를 실행하고, `poetry`로 생성된 가상환경 경로의 파이썬을 선택한다.

## 실행 방법

기본적으로 `runner.ghx` 파일을 실행했을 때, 그래스호퍼에서 `GhPython Script` 컴포넌트들이 `logic/` 폴더 내부의 파이썬 모듈들을 `import`하여 사용하는 구조다.

만약 macOS를 사용 중이라면, 해당 저장소 폴더를 라이노의 탐색 경로에 추가해야 한다. macOS 라이노는 Windows 라이노와 달리, 열고 있는 `.ghx` 파일이 포함된 폴더의 경로를 파이썬의 `sys.path`에 추가하지 않기 때문이다. 탐색 경로를 추가하려면, 라이노에서 `EditPythonScript` 명령어를 실행한 후, `Tools`메뉴에서 `Options` 창을 열고 `Module Search Paths`에 이 저장소의 폴더 경로를 입력하면 된다.