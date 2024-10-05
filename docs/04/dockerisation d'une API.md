
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
