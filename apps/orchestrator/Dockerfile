FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ../../sim /app/sim
COPY ../../agents /app/agents
COPY ../../configs /app/configs
COPY main.py settings.py ./
VOLUME ["/artifacts"]
CMD ["python", "main.py"]
