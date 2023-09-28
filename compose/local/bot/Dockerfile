# Use a Python base image
FROM python:3.11-alpine

# Install bot dependencies
RUN pip install --upgrade pip
COPY requirements /requirements
RUN pip install -r /requirements/local.txt

# Set the working directory
WORKDIR /app

# Run the bot script
CMD ["python", "bot.py"]
