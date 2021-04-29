# Your Dockerfile contents go here!
FROM python:3.8.2

WORKDIR /wallet-app

COPY ./src .

CMD ["python", "wallet.py"]