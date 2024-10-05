# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Expose the Streamlit default port
EXPOSE 8501

# Environment variable to avoid running as root
# ENV STREAMLIT_SERVER_RUN_ON_DEVICE=0

# Start the app
CMD ["streamlit", "run", "app.py", "--logger.level", "debug"]

