FROM python:3.12-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc libpq-dev \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www

COPY requirements.txt .

RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD flask db upgrade && flask seed all && gunicorn app:app