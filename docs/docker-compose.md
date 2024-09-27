
# Chapter: Docker Compose - Managing Multi-Container Applications

## Links and tutorials

bon exemple de hello world avec docker compose
<https://medium.com/@jdgb.projects/hello-world-with-docker-c310d1486058>

see also

<https://medium.com/@mrubel.documents/module-06-becoming-a-docker-virtuoso-docker-compose-practice-aa70152ebdca>

## 1. Introduction to Docker Compose

- What is Docker Compose?
- Why use Docker Compose?
- How Docker Compose relates to Docker

## 2. Docker Compose File

- docker-compose.yml file structure
- YAML syntax basics
- Key components: version, services, networks, volumes

## 3. Basic Docker Compose Commands

- docker-compose up
- docker-compose down
- docker-compose ps
- docker-compose logs

## 4. Defining Services

- Service configuration options
- Specifying images
- Building images from Dockerfiles
- Port mapping
- Environment variables

## 5. Networking in Docker Compose

- Default network
- Creating custom networks
- Connecting services to networks

## 6. Managing Data with Volumes

- Defining and using named volumes
- Bind mounts in Docker Compose

## 7. Environment Variables and Composition

- Using .env files
- Variable substitution in docker-compose.yml

## 8. Practical Example: Building a Web Application Stack

- Creating a multi-container application (e.g., Python web app + Redis)
- Writing the docker-compose.yml file
- Building and running the application
- Making changes and redeploying

## 9. Docker Compose in Development vs Production

- Using Compose for local development
- Considerations for production use

## 10. Advanced Topics

    - Extending services with multiple Compose files
    - Scaling services
    - Compose command for swarm mode

## 11. Best Practices and Common Pitfalls

    - Compose file organization
    - Version control for Compose files
    - Avoiding common mistakes

## 12. Hands-on Exercise

    - Create a multi-container application using Docker Compose
    - Include a web server, application server, and database
    - Practice starting, stopping, and scaling the application

## 13. Summary and Next Steps

    - Recap of key concepts
    - Resources for further learning
    - Preview of upcoming topics (e.g., Docker Swarm, Kubernetes)
