FROM python:3.10-slim

RUN apt update && apt install -y python3-dev build-essential libpq-dev default-libmysqlclient-dev

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests/

WORKDIR /src
CMD ["python", "gpt/main.py"]
