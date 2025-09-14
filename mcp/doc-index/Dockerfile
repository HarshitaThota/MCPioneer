FROM python:3.11-slim
WORKDIR /app
RUN pip install fastapi uvicorn
COPY server.py .
COPY ../../data/knowledge /data
EXPOSE 7001
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7001"]
