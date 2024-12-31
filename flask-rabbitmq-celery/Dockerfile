# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /code

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the default command for the web service
CMD ["flask", "run", "--host=0.0.0.0"]
