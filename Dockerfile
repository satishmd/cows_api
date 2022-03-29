FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /cows
WORKDIR /cows
ADD requirements.txt /cows/
RUN pip install -r requirements.txt
ADD . /cows/