FROM python:3.12-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc libpq-dev \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www

COPY requirements.txt .

RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python -c "import os, urllib.parse as u; url=os.environ.get('DATABASE_URL'); p=u.urlparse(url); print('DB_USER=', p.username); print('DB_HOST=', p.hostname); print('DB_NAME=', p.path); print('DB_PASSWORD_LENGTH=', len(p.password or ''))" && flask db upgrade && flask seed all && gunicorn app:app