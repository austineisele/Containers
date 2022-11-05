FROM python:3-alpine3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-app.py", "--host=0.0.0.0"]