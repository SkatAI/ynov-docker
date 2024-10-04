# dockerisation d'une API

<https://chatgpt.com/c/66fd4de1-7264-800e-8344-fd187e6528cd>

Here's a walkthrough of creating a simple Dockerfile for an API service using a trivial Python app. The app will use `Flask`, a minimal web framework, to serve a simple "Hello, World!" API.

### Step 1: Create the Python App

First, let's create a simple Python file (`app.py`) with a basic Flask app:

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

This app exposes a single route (`/`) that returns "Hello, World!" when accessed.

### Step 2: Create a Requirements File

Flask is required to run the Python app, so create a `requirements.txt` file to define the dependencies:

```txt
Flask==2.1.1
```

### Step 3: Write the Dockerfile

Next, create a `Dockerfile` to build and run this Python app inside a Docker container.

```Dockerfile
# Dockerfile

# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Make port 5000 available to the world outside this container
EXPOSE 5000

# Step 6: Define environment variable
ENV FLASK_APP=app.py

# Step 7: Run the application
CMD ["python", "app.py"]
```

### Explanation of the Dockerfile

1. **Base Image (`FROM python:3.9-slim`)**:
   - We are using a lightweight official Python image based on version 3.9.

2. **Working Directory (`WORKDIR /app`)**:
   - This sets the working directory inside the container to `/app`, where the app's files will be placed.

3. **Copy Files (`COPY . /app`)**:
   - This command copies all the files from your current directory on the host (where the Dockerfile resides) into the `/app` directory inside the container.

4. **Install Dependencies (`RUN pip install`)**:
   - The `RUN` command installs the dependencies listed in the `requirements.txt` file inside the container.

5. **Expose Port (`EXPOSE 5000`)**:
   - This tells Docker that the container will be listening on port 5000, where Flask runs by default.

6. **Environment Variable (`ENV FLASK_APP`)**:
   - This sets an environment variable so Flask knows which file to use as the main app when running.

7. **Run the App (`CMD`)**:
   - The `CMD` command specifies the command that should be run when the container starts. In this case, it runs the Python script to start the Flask app.

### Step 4: Build and Run the Docker Image

To build the Docker image, navigate to the directory with the `Dockerfile` and run:

```bash
docker build -t simple-flask-app .
```

This creates a Docker image named `simple-flask-app`.

To run the container, use:

```bash
docker run -p 5000:5000 simple-flask-app
```

Now, your Flask app will be accessible at `http://localhost:5000` and will return "Hello, World!" when accessed.

### Key Docker Concepts Covered

1. **`FROM`**: Defines the base image.
2. **`WORKDIR`**: Sets the working directory inside the container.
3. **`COPY`**: Copies files from the host machine to the container.
4. **`RUN`**

changer le code => besoin ed rebuild l'image
ca fait vite beaucoup d'image

To avoid rebuilding the Docker image every time you change the code, you can mount your local code directory into the running Docker container. This way, any changes made to the code are immediately reflected inside the container, without needing to rebuild the image.

## Volume

Here's how you can do it:

### Step 1: Modify the Docker Run Command

You can use Docker’s **volume mounting** feature to mount your local code into the container. This allows you to develop locally and see the changes without rebuilding the image.

Assuming your project directory looks like this:

```
/project
  |-- app.py
  |-- requirements.txt
  |-- character_prompts.json
  |-- .env
  |-- Dockerfile
```

Run the container with the `-v` option to mount the current directory (`$(pwd)` on Linux/Mac, `%cd%` on Windows) to the `/app` directory inside the container:

```bash
docker run -p 8501:8501 --env-file .env -v $(pwd):/app gpt-character-app
```

- `-v $(pwd):/app`: This mounts the current working directory on your host machine to `/app` in the container.
- Now any changes you make to `app.py` or other files in the directory will be instantly reflected in the container.

### Step 2: Ensure Auto-reloading with Streamlit

Streamlit has an auto-reload feature, but we need to ensure it works inside the Docker container. Streamlit automatically watches for changes to files in the working directory and reloads the app.

If you don't see this behavior, make sure the Streamlit configuration is correct:

1. **Add a `config.toml` file (optional)**: You can create a Streamlit config file in your project folder to ensure auto-reloading is enabled.

   Create a `.streamlit/config.toml` file:

   ```toml
   [server]
   headless = true
   reload = true
   ```

This will ensure that Streamlit watches for file changes and reloads the app automatically.

### Step 3: Running the Container in Development Mode

1. **Build the image** (you only need to do this once or when dependencies change):

    ```bash
    docker build -t gpt-character-app .
    ```

2. **Run the container with volume mounting** to reflect code changes without rebuilding:

    ```bash
    docker run -p 8501:8501 --env-file .env -v $(pwd):/app gpt-character-app
    ```

This approach will let you work on your app code without having to rebuild the Docker image, providing a faster development experience.
