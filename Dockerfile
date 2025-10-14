FROM python:3.9-alpine AS base

RUN addgroup -S appgroup && adduser -S appuser -G appgroup


RUN apk add --no-cache build-base libffi-dev openssl-dev \
  && rm -rf /var/cache/apk/*

WORKDIR /app


COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY app/ ./app


RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

CMD ["python", "-m", "app.main"]
