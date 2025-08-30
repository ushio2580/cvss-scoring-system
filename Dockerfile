FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Change to backend directory and set Python path
WORKDIR /app/backend
ENV PYTHONPATH=/app/backend

# Expose port
EXPOSE $PORT

# Start the application with proper command format
CMD gunicorn app:app --bind 0.0.0.0:$PORT --workers 1
