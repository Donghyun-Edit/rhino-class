# 라이노 개발 환경

## 개발 환경 구축

VScode에서 터미널 명령어는 `Ctrl+J`로 실행 가능하다.

### 파이썬 준비

[파이썬](https://www.python.org/) 3.9 이상의 버전을 설치한다. 또한, [Poetry](https://python-poetry.org/docs)가 설치되지 않았다면 준비해 놓는다.

아래 터미널 명령어로 시스템이 준비되었는지 확인이 가능하다.

```bash
python --version
poetry --version
```

### 파이썬 패키지 설치

```bash
poetry install
```

### VScode에서 Python interpreter를 가상환경 경로로 지정

VScode 창에서 `Ctrl+Shift+P`로 `Python: Select Interpreter` 명령어를 실행하고, `poetry`로 생성된 가상환경 경로의 파이썬을 선택한다. 해당 파이썬은 라이노에 설치된 파이썬과는 다르지만, VScode 에디터에서 자동완성 및 코드 검사 등의 편의기능을 제공한다.

만약 Poetry로 생성된 가상환경이 Interpreter 목록에 없다면, 아래 터미널 명령어에서 나오는 경로를 직접 추가한다.

```bash
poetry env info --path
```

## 코드 작성 방법

본인이 테스트하고 싶은 코드나 수업에서 나온 내용은 `logic` 모듈 내부에 작성하면 된다. 필요하다면 `.py` 파일들을 더 만들 수도 있다.

`logic` 이외의 폴더들은 보다 빠른 개발을 위한 도우미 모듈이므로 수정을 피하는 것이 좋다.

> 파이썬에서는 `.py` 확장자를 가진 파일이 바로 모듈이며, `__init__.py` 파일을 담고 있는 폴더도 모듈로 취급된다.

## 실행 방법

기본적으로 `runner.ghx` 파일을 실행했을 때, 그래스호퍼에서의 파이썬 컴포넌트들이 `logic` 폴더 내부의 파이썬 모듈들을 `import`하여 사용하는 구조다.

## 브랜치

해당 저장소는 목적에 따라 다른 Git 브랜치로 코드를 관리한다.

- `main`: 라이노 8을 위한 시작 템플릿
- `rhino-seven`: 라이노 7을 위한 시작 템플릿
- `exercise`: 각종 예제 및 연습 코드