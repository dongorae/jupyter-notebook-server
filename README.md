# 주피터 노트북 서버 세팅

- 주피터 노트북을 로컬이 아닌 외부에서 접속 시 몇가지 세팅이 필요하다.
- 파이썬 및 주피터 노트북이 설치되어있다고 가정한다.

1. config 파일 생성

    - `jupyter notebook --generate-config` 명령어 실행한다.
    - 이렇게 하면 `~/.jupyter/jupyter_notebook_config.py` 파일이 생성된다.
    - 이 파일 안에는 서버 세팅에 대한 설정 사항이 명시 된 파일이다.

2. 서버 세팅

    - 직접 `jupyter_notebook_config.py` 내용을 수정하거나 간단히 세팅을 하고싶다면 setting.py 또는 setting,ipynb 파일을 실행한다.

3. 주피터 노트북 실행
    - 주피터 노트북를 실행 할 위치에 가서 `jupyter notebook` 실행