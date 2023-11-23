#!/bin/bash

echo "🔨 Building the Docker image..."

docker build -t product-catalog-service:latest .

docker run -d -p 8080:8080 -e FLASK_ENV=testing product-catalog-service

echo "🚀 The product-catalog-service Flask app is now running."
echo "🌐 You can access it by opening a web browser and entering:"
echo "   🌍 http://localhost:8080"
echo "   or"
echo "   🌐 http://YOUR_SERVER_IP:8080 (if accessing remotely)"
