FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt 

RUN pip install --upgrade pip

RUN pip install -r requirements.txt 

COPY . .

EXPOSE 80

CMD ["python", "app.py"]