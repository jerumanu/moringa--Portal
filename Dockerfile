# Use an official Python runtime as the base image
FROM python:3.9.6-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
COPY . /app
WORKDIR /app

# Update package repositories and install dependencies
RUN python3 -m venv /opt/venv
RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# Copy the requirements file
COPY requirements.txt .

# Install project dependencies
RUN /opt/venv/bin/pip install --upgrade pip && \
/opt/venv/bin/pip install --no-cache-dir -r requirements.txt && \
chmod +x entrypoint.sh

CMD [ "/app/entrypoint.sh" ]
# Copy the project files into the container
COPY . .

# Expose the port that the Django development server will run on (default: 8000)
# EXPOSE 8000

# Start the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
