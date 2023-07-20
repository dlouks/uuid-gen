FROM python:3.9

WORKDIR /app

COPY main.py .

COPY requirements.txt .

RUN pip3.9 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--reload"]
  