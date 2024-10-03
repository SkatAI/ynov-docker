# Docker hub

## que se passe til quand on publie une image sur Docker Hub

1. What pushing an image really does:

   When you push an image, Docker client sends the image layers to Docker Hub. An image is composed of multiple layers, each representing a change in the filesystem. Docker uses a content-addressable storage system, meaning each layer is identified by a hash of its contents.

2. What's stored on Docker Hub:

   - Image Layers: Docker Hub stores the individual layers that make up your image. These layers contain the file system changes and metadata.
   - Image Manifest: This is a JSON file that describes the image, including the layers it's composed of and other metadata.
   - Image Config: This contains runtime configuration for the image, like environment variables, exposed ports, and the default command to run.

3. Is the whole image executable on Docker Hub?

   No, Docker Hub doesn't execute your image. It's just a storage and distribution service. The image becomes executable when it's pulled and run on a machine with Docker installed.

4. More things made available:

   - Tags: You can have multiple tags for the same image, allowing version control.
   - README: If your repository has a README.md file, it's displayed on the Docker Hub page.
   - Description: You can add a short and full description to your repository.
   - Collaborators: You can add users who can push to your repository.

5. Does Docker Hub run some process?

   Docker Hub doesn't run your container or execute your image. However, it does perform some processes:
   - Image scanning (for supported plans): Checks for known vulnerabilities.
   - Webhooks: Can trigger actions when an image is pushed.
   - Automated Builds: Can build images automatically from source code repositories (GitHub/Bitbucket).

When someone wants to use your image:

1. They pull it from Docker Hub using `docker pull skatai/ynov-docker:v1`.
2. Docker client downloads the necessary layers.
3. The image is reconstructed on their local machine.
4. They can then run a container from this image using `docker run skatai/ynov-docker:v1`.

In essence, Docker Hub acts as a centralized repository for storing and distributing Docker images, but the actual execution of these images happens on the machines where they're pulled and run.
