FROM python:3
MAINTAINER michallee104@126.com

ENV LANG C.UTF-8

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir  -r requirements.txt && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py collectstatic --no-input

EXPOSE 8081 8081
