FROM python:3.9-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY ./app/requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY ./app .


RUN chown -R appuser:appgroup /app


USER appuser


EXPOSE 8000


CMD ["python", "main.py"]
