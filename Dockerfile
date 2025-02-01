# Use an official Python runtime as the base image
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port that the Django app will run on
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Run Django's migration and then start the development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
