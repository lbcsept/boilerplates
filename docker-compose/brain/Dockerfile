# Use the official Python image (slim variant for smaller size)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y wakeonlan ethtool

# Copy the Flask application
COPY . .

# Expose the port Flask runs on (default: 5000)
EXPOSE 4999

# Run the Flask app
# CMD ["gunicorn", "--bind", "0.0.0.0:4999", "--workers", "4", "--threads", "2", "src.api:app"]
CMD ["PYTHONPATH=`pwd`/..", "gunicorn", "--bind", "0.0.0.0:4999", "src.api:app"]
# CMD ["cd", "brain", "gunicorn", "--bind", "0.0.0.0:4999", "src.api:app"]
# CMD ["gunicorn", "--bind", "0.0.0.0:4999", "app:src.api"]
# CMD ["gunicorn", "--bind", "0.0.0.0:4999", "src.api:toto"]