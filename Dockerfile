# Lightweight Python image
FROM python:3.13-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY main.py ./

# Expose and run
EXPOSE 8080
CMD ["python", "main.py"]
