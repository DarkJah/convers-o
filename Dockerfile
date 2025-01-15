FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]