FROM python:3.12-slim
LABEL org.opencontainers.image.source="https://github.com/i-fyod/devops-ci-app"
LABEL org.opencontainers.image.description="Isolated educational Flask CI application"
RUN useradd --system --create-home --uid 10001 app
WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ app/
USER app
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--access-logfile", "-", "app.missing:app"]
