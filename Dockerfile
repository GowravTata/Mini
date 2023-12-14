FROM python:alpine

WORKDIR /app

COPY . .
ENV PYTHONPATH=~/app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ['python','run.py']