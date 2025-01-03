# Don't Remove Credit @Rajdev21_bot
# Subscribe YouTube Channel For Amazing Bot @raj_dev21
# Ask Doubt on telegram @raj_dev21

FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /raj-Post-Search-Bot
WORKDIR /raj-Post-Search-Bot
COPY . /raj-Post-Search-Bot
CMD gunicorn app:app & python3 main.py
