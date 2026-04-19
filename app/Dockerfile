FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the static folder and the app
COPY static/ ./static/
COPY helloworld.py .

EXPOSE 80

CMD ["python", "helloworld.py"]

