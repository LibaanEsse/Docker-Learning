
FROM python:3.12-slim
WORKDIR /app


RUN pip install --no-cache-dir flask redis

COPY . .
CMD ["python", "count.py"] 


