FROM python:3.10.18-bookworm

WORKDIR /app

RUN pip install --upgrade pip wheel "poetry==1.6.1"

RUN poetry config virtualenvs.create false  

COPY pyproject.toml poetry.lock ./

RUN poetry install 

COPY . .

RUN chmod +x prestart.sh

ENV PYTHONPATH=/app
ENTRYPOINT ["./prestart.sh"]
