setup a Database
and

# Volumes

<https://medium.com/@jdgb.projects/understanding-volumes-in-docker-f21dea4457b5>

Docker volumes are a way to persist data generated and used by Docker containers.

excellent walkthrough creating a volume for a mysql database
creating a container using that volume
connecting to the db ...
rm container
create anothe one with same colume
and checking volume is there

## Bind Mounts

Bind Mounts
In bind mounts, the file/directory on the host machine is mounted into the container. By contrast, when using a Docker volume, a new directory is created within Docker’s storage directory on the Docker host and the contents of the directory are managed by Docker.
.5
