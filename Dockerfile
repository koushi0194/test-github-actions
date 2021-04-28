# Your Dockerfile contents go here!
FROM python:3.8.2

WORKDIR /age-app

COPY . ./app

CMD ["python", "wallet.py"]