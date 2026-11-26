ARG PYTHON_VERSION=3.14.3
FROM python:${PYTHON_VERSION}-slim as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
COPY app/ .
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser
# Expose the port that the application listens on.
EXPOSE 8000
# Run the application.
CMD ["python","app/main.py"]
