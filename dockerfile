# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD ["python", "main.py"]
