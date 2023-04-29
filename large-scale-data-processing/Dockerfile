
# Use official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .

# Set environment variables
ENV PYSPARK_PYTHON=python3
ENV PATH=$PATH:/usr/local/spark/bin

# Download and install Spark
RUN curl https://downloads.apache.org/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz | tar -zx && \
    mv spark-3.1.1-bin-hadoop3.2 /usr/local/spark

# Set the entrypoint to start the master script
ENTRYPOINT ["python", "src/master.py"]
