# Scope du cours

- Connaître les caractéristiques d'un conteneur et découvrir Docker

- Installer et utiliser Docker

- Maîtriser la persistance des données avec Docker

- Utiliser Docker-Compose

- Maîtriser les notions réseaux de Docker

## En détail

| session | workshop / cours  topic | status |
|-------|-----------------------|----------|
| 01.01 | intro cours + quizz | ✅ |
| 01.02 | why docker + motivation + images, containers | ✅  |
| 01.03 | Install + hello world | - |
| 01.04 | docker run: images and containers, ports, hash strings | ✅ |
|-------|-----------------------|----------|
| 02.01 | recap et intro | ✅ |
| 02.02 | run ubuntu in a container + linux| ✅ |
| 02.03 | linux| ✅ |
| 02 | lab on basic docker commands + linux avec Ubuntu | ✅ |
|-------|-----------------------|----------|
| 03.01 | recap 1st day | ✅ |
| 03.02 | TD alpine + linux + images | ✅ |
| 03.03 | Publish on Docker hub | ✅ |
| 03.04 | dockerfiles | ✅ |
| 03.05 | build an API python : requirements.txt, .gitignore, VOLUME | ✅ |
|-------|-----------------------|----------|
| 04 | intro | ✅  |
| 04 | optimizing, layers, cache, subtleties, choosing images | ✅  |
| 04 | Dockerfile workshop 2: Question app with OpenAI | proof read |
|-------|-----------------------|----------|
| 04 | multi stage builds, | - |
| 05 | Big recap on day 1 and 2 | - |
| 05 | Dockerfile workshop 3 | - |
| 05 | Docker compose | - |
| 06 | Workshop on Docker compose | - |
| 06 | Docker compose II: more advanced  | - |
| 06 | Workshop on Docker compose II | - |
|-------|-----------------------|----------|
| 07 | recap | - |
|-------|-----------------------|----------|
| 08 | projet | - |

## Ideas

- show some karhoo Dockerfiles and ask them to live comment

- lifecycle : <https://training.play-with-docker.com/beginner-linux/> ... exercice ... mysql
- data persistence;  containers are ephemeral and stateless
- dockerignore
- deploy on Azure: <https://learn.microsoft.com/en-us/azure/developer/python/tutorial-deploy-python-web-app-azure-container-apps-02?tabs=azure-cli%2Ccreate-database-psql>

## Posts and sources

- multi stage builds
what is the advantage of multi-stage builds over docker compose
see <https://claude.ai/chat/dfdf46cb-7a51-4f3f-9650-2de92e4ec424>

- CI/CD

- deployer une app dockerisée sur Azure
  - <https://medium.com/@dmosyan/pros-and-cons-of-azure-app-service-for-containers-81f4ca1fbf85>
- Docker secrets
  - <https://medium.com/@younusraza909/docker-secrets-beginners-guide-73f0b60764aa>

- Reducing image size, build time
  - <https://medium.com/datamindedbe/how-we-reduced-our-docker-build-times-by-40-afea7b7f5fe7>

- choosing the right base image
  - <https://medium.com/@arif.rahman.rhm/choosing-the-right-python-docker-image-slim-buster-vs-alpine-vs-slim-bullseye-5586bac8b4c9>

- hashing ou encryption
  - <https://iorilan.medium.com/a-basic-question-in-security-interview-how-do-you-store-passwords-in-the-database-676c125cff64>

### Use cases

Containeriser une base de donnée

- postgres <https://medium.com/@nathaliafriederichs/setting-up-a-postgresql-environment-in-docker-a-step-by-step-guide-55cbcb1061ba>
- mysql <https://medium.com/towards-data-engineering/dockerize-your-databases-a-step-by-step-guide-to-mysql-containerization-8dc2deabeebd>

Docker to server LLM

- <https://towardsdatascience.com/reducing-the-size-of-docker-images-serving-llm-models-b70ee66e5a76>

__________________________
--------------------------

Docker containers vs VMs
--------------------------

<https://www.docker.com/blog/docker-myths-debunked/>

Docker containers are often mistaken for virtual machines (VMs), but the technologies operate quite differently. Unlike VMs, Docker containers don’t include an entire operating system (OS). Instead, they share the host operating system kernel, making them more lightweight and efficient. VMs require a hypervisor to create virtual hardware for the guest OS, which introduces significant overhead. Docker only packages the application and its dependencies, allowing for faster startup times and minimal performance overhead.

By utilizing the host operating system’s resources efficiently, Docker containers use fewer resources overall than VMs, which need substantial resources to run multiple operating systems concurrently. Docker’s architecture efficiently runs numerous isolated applications on a single host, optimizing infrastructure and development workflows. Understanding this distinction is crucial for maximizing Docker’s lightweight and scalable potential.

However, when running on non-Linux systems, Docker needs to emulate a Linux environment. For example, Docker Desktop uses a fully managed VM to provide a consistent experience across Windows, Mac, and Linux by running its Linux components inside this VM.

see <https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2OyPjmh9VqKMVuajPk0fEQ.jpeg>

see also

<https://medium.com/datadriveninvestor/docker-f0b8df21f003>

__________________________
--------------------------

Setup local
--------------------------

# Install Docker Desktop

<https://docs.docker.com/get-started/get-docker/>

Installer docker desktop sur windows
<https://gailloty.net/fr/post/docker-windows/>

__________________________
--------------------------

Travailler avec Docker Desktop
--------------------------

## Installer une image depuis docker desktop

dans la search bar : Ubuntu

une liste de plusieurs images apparait

Une image est un gros fichier qui permet de faire tourner une application, un OS, un service etc ...

Donc l'image Ubuntu permet de lancer un environnement Ubuntu

## lancer l'image ?

cela cree un container

## Docker Hub

Il y a des milliers d'images dispo sur Docker hub
par exemple

- itzg/minecraft-server: pour lancer un server minecraft
- pytorch/pytorch, tensorflow/tensorflow : pour du deep learning
- wordpress : pour un blog wordpress
- pythontelegrambot/python-telegram-bot : developping bots for telegram
- homeassistant/home-assistant : Raspberry Pi home automation (IoT)
- ethereum/client-go, openethereum/openethereum: run full Ethereum nodes

# classic games server on your local

docker pull antoine13/retroarch-web-games

docker-compose up -d
After the container is up and running, open your web browser and navigate to <http://localhost:8080> to start using the RetroArch web player.

see also 2048, tetris, Chess, etc

# Acceder au terminal dans windows et mac

WSL vs ...

# simple docker run from the command line

Il y a equivalence entre les bouton Pull et Run dans docker desktop et la ligne de commande dans le terminal

- docker pull
- docker run
- docker stop
- docker container ls
- docker ps & docker ps -a

docker help pour toute la liste des commandes disponibles

pour supprimer

- docker rm (containers)
- docker rmi (images)

you can also search for images with ```docker search```

## 1st container de bienvenue

```bash
docker run -d -p 8080:80 docker/welcome-to-docker
```

puis dans le navigateur: <http://localhost:8080/>

allez ensuite dans docker desktop > containers
vous voyez

- un nom : ce nom est généré aléatoirement. Il comporte toujours 2  parties
- un hash : identifiant unique du container
- image : L'image du container
- status : running / exited ?
- port :
- last started : date de start
- des actions : view image, copy docker run,  view files, stop, start, pause etc

# Recap : container vs image ?

- quelle difference entre un container et une image ?
- in docker what's the difference between a container and an image ?

Une image est un fichier immutable qui contient tout ce qui est necessaire pour runner une application

ex: ubuntu, ... l'app de bienvenue

On peut construire sa propre image en écrivant un Dockerfile : specifier tout ce dont on a besoin

Un container est une instance d'une image en cours d'execution (running)

C'est un environnement d'execiution real time ou l'application run

On peut se connecter a un container en cours d'execution

En resumé:

An **image** is a blueprint, while a **container** is a running instance of that image.

# ports

dans l'exemple

```bash
docker run -d -p 8080:80 docker/welcome-to-docker
```

on accède a l'application dans localhost:8080

le parametre -p 8080:80 map le port interne du container 80 vers le port externe 8080

le port 80 interne est defini dans l'image

regarder dans Docker Desktop
cliquer sur l'image
on voit la liste de commande qui a servi a creer l'image

Ligne 12: Expose 80

notez aussi les from Alpine, nginx

enfin le flag -d : detach

si on run ubuntu avec -d

on a un container qui run
mais comment y acceder

avec la commande attach

docker ps
docker ebf686e6f2eb attach

# Nginx

un mot sur NGINX

# Ecosysteme docker

- Docker hub
- github
- local
- cloud

# Recap

image
docker commands : ps, run, pull, rm ....
containers

flags: -i -t -p -d

# Clean up

Clean your docker host using the commands (in bash):

$ docker rm -f $(docker ps -a -q)

# Docker hub

Creer un compte

# PWD Play with docker

Exercice

<https://training.play-with-docker.com/beginner-linux/>

--- fin de l'intro

# How to build Your First Alpine Docker Image and Push it to DockerHub

<https://dockerlabs.collabnix.com/beginners/building-your-first-alpine-container.html>

__________________________
--------------------------

Docker files
--------------------------

<https://dockerlabs.collabnix.com/presentation/docker_workshop_1.html#/70>

Layers

Create an image with GIT Installed

docker build

setup the environment
from images
add and install what's needed

open ports
then copy your local files : cOPY
then run somme command : CMD, RUN

Entrypoint
<https://dockerlabs.collabnix.com/presentation/docker_workshop_1.html#/110>

WORKDIR

__________________________
--------------------------

Docker architecture
--------------------------

# Docker architecture

<https://docs.docker.com/get-started/docker-overview/#docker-architecture>

explain : <https://docs.docker.com/get-started/images/docker-architecture.webp>

Docker architecture

Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface. Another Docker client is Docker Compose, that lets you work with applications consisting of a set of containers.

- deamon
- client
- desktop
- registries
- objects
- images
- containers
- and other things

# resources

Coursera
<https://www.coursera.org/learn/docker-for-the-absolute-beginner>

project
<https://www.coursera.org/projects/docker-for-absolute-beginners>

# labs

<https://dockerlabs.collabnix.com/>

<https://github.com/collabnix/dockerlabs/blob/master/beginners/README.md>

play with docker
<https://labs.play-with-docker.com/>
