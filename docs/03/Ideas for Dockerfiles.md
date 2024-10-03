## Plan

4. Docker volumes and data persistence:
Create exercises that involve using named volumes, bind mounts, and tmpfs mounts. Have students set up a stateful application (like a database) and demonstrate data persistence across container restarts.

=> database

1. Multi-stage builds:
Have students create a Dockerfile that uses multi-stage builds to compile a simple application (e.g., in Go or C++) and then copy only the binary into a minimal production image. This illustrates how to create smaller, more secure production images.

faut y passer

8. Optimizing Docker images:
Create a workshop focused on reducing image size and improving build times. This could include exercises on choosing appropriate base images, minimizing layers, and using .dockerignore files effectively.

5. Docker security:
Guide students through implementing security best practices such as running containers with non-root users, using read-only filesystems, and limiting container resources. Include an exercise on scanning images for vulnerabilities.

pas mal ça

10. Docker health checks and auto-healing:
Guide students through implementing health checks in their Dockerfiles and Docker Compose files. Show how to set up auto-healing containers that restart automatically when they become unhealthy.

6. Continuous Integration/Continuous Deployment (CI/CD) with Docker:
Set up a simple CI/CD pipeline using GitHub Actions or GitLab CI that builds a Docker image, runs tests inside a container, and deploys to a staging environment.

super ça, si on a le temps. au moins en demo ?

7. Docker Swarm or Kubernetes basics:
While this might be beyond the scope of a Docker-focused course, an introduction to container orchestration could be valuable. Have students set up a simple Docker Swarm or Kubernetes cluster and deploy a scalable application.

9. Debugging Docker containers:
Prepare scenarios where students need to troubleshoot common issues in Docker containers, such as networking problems, resource constraints, or application errors. Teach them how to use Docker commands for debugging.

trop difficile a demo

Would you like me to elaborate on any of these workshop ideas or suggest some specific exercises for any of them?

3. Docker networking:
Set up a workshop where students create custom bridge networks, connect containers to multiple networks, and experiment with container-to-container communication. This could include exercises on port mapping and using Docker DNS.
