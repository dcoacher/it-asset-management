# Python Slim Image
FROM python:3.12-slim

#Setting Working Directory
WORKDIR /cicd

# Copying Python dependencies file
COPY requirements.txt .

# Installation Python dependencies from the copied earlier file
RUN pip install -r requirements.txt

# Copying all required files
COPY . .

# Running Pytest
RUN pytest
CMD ["python","main.py"]

