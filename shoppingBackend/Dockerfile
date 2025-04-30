FROM python:3.12-slim

WORKDIR /app

COPY ./shoppingBackend/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./shoppingBackend /app/

EXPOSE 8000

CMD ["fastapi", "dev", "main.py"]