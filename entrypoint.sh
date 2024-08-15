#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Starting the server..."
uvicorn config.asgi:application --host 0.0.0.0 --port 8000