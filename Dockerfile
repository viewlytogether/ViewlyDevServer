FROM python:alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /git_bot

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

