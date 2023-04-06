FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --only=main
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "nfc_check.server:app"]
