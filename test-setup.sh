#!/bin/bash

echo "🧪 Testing CVSS System Setup..."

# Test backend
echo "📦 Testing Backend..."
cd backend
if [ -d "venv" ]; then
    echo "✅ Virtual environment exists"
    source venv/bin/activate
    python -c "import flask; print('✅ Flask installed')"
    python -c "import sqlalchemy; print('✅ SQLAlchemy installed')"
else
    echo "❌ Virtual environment not found. Run setup.sh first"
    exit 1
fi

# Test frontend
echo "📦 Testing Frontend..."
cd ../frontend
if [ -d "node_modules" ]; then
    echo "✅ Node modules exist"
    npm list --depth=0 | grep -E "(react|vite|typescript)" | head -5
else
    echo "❌ Node modules not found. Run setup.sh first"
    exit 1
fi

echo "🎉 Setup test completed successfully!"
echo ""
echo "To start the application:"
echo "1. Backend: cd backend && source venv/bin/activate && python run.py"
echo "2. Frontend: cd frontend && npm run dev"
echo ""
echo "Or use Docker: docker-compose up"
