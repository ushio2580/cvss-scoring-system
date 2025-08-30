#!/bin/bash

echo "🚀 Setting up CVSS Scoring System..."

# Create virtual environment for backend
echo "📦 Setting up Python backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Copy environment file
cp env.example .env
echo "✅ Backend setup complete!"

# Setup frontend
echo "📦 Setting up React frontend..."
cd ../frontend
npm install
echo "✅ Frontend setup complete!"

# Return to root
cd ..

echo "🎉 Setup complete!"
echo ""
echo "To start the application:"
echo "1. Backend: cd backend && source venv/bin/activate && python run.py"
echo "2. Frontend: cd frontend && npm run dev"
echo ""
echo "Or use Docker Compose:"
echo "docker-compose up"
