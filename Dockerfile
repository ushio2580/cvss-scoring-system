FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Change to backend directory
WORKDIR /app/backend

# Expose port
EXPOSE $PORT

# Start the application using wsgi.py
CMD gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 1
