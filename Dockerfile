FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for better caching
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set working directory to backend
WORKDIR /app/backend

# Expose port
EXPOSE $PORT

# Start the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]
