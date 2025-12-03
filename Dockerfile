FROM python:3.12-slim

# Prevents Python from writting .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Set work directory
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    nano \
    && apt-get clean

# Install python dependencies
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Copy project
COPY . /app/

# Collect static + media files
RUN mkdir -p /app/staticfiles
RUN mkdir -p /app/media

# Collect static files
RUN python manage.py collectstatic --noinput

# Gunicorn start command
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
