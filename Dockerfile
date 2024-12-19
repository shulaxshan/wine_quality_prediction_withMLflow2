FROM python:3.9-slim-bullseye

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

# Expose the default port (optional, if your app listens on a specific port)
EXPOSE 8080

CMD ["python3", "app.py"]