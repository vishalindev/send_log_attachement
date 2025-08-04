# Use a minimal Python image
FROM python:3.10-alpine

# Install required packages for yagmail (includes SSL & email support)
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt ./
COPY send_log_attachment.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "send_log_attachment.py"]