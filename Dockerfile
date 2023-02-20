# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7.9

ADD requirements.txt .

RUN python3 -m pip install Cython && \
    python3 -m pip install -Ur requirements.txt

WORKDIR /app
ADD src /app

CMD ["python","app.py"]