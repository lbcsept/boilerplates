# Use the official Python image (slim variant for smaller size)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y wakeonlan ethtool inetutils-ping

# Copy the Flask application
# COPY . .
COPY ./src/ /app/src


# Set PYTHONPATH to the current directory
ENV PYTHONPATH=/app/

# Verify the structure exists
RUN ls -la /app/

# Expose the port Flask runs on (default: 5000)
EXPOSE 4999

# Run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:4999", "src.api:app"]
