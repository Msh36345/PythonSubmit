FROM python:3.10-slim

LABEL maintainer="msh36345@gmail.com"
LABEL description="run naive bayes v2 client"

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8090


CMD ["uvicorn", "Server:app", "--host", "0.0.0.0", "--port", "8090"]