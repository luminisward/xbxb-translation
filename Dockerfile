FROM python:3.7-alpine
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir gunicorn
COPY xb2translation xb2translation

EXPOSE 8000
CMD [ "gunicorn", "--bind=0.0.0.0", "--workers=3", "xb2translation.app:app" ]
