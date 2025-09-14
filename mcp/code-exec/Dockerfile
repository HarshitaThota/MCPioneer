FROM python:3.11-slim
WORKDIR /app
RUN pip install fastapi uvicorn
COPY server.py .
EXPOSE 7002
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7002"]
