FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install pipenv \
  && pipenv lock --keep-outdated --requirements > requirements.txt \
  && pip3 install -r requirements.txt

CMD python3 src/main.py