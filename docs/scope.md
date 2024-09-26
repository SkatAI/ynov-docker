# Scope du cours

- Connaître les caractéristiques d'un conteneur et découvrir Docker

- Installer et utiliser Docker

- Maîtriser la persistance des données avec Docker

- Utiliser Docker-Compose

- Maîtriser les notions réseaux de Docker

plus

- Dockerfile
- deployer une app dockerisée sur Azure

| session | workshop / cours  topic |
|-------|--------------------------------------------------|
| 01.01 | intro cours + quizz |
| 01.02 | why docker + motivation + images, containers |
| 01.03 | Install + hello world |
| 01.04 | docker run: images and containers, ports, hash strings |
| 02 | recap images, containers |
| 02 | run ubuntu in a container + linux|
| 02 | workshop on basic docker commands |
|-------|--------------------------------------------------|
| 03 | recap 1st day |
| 03 | dockerfiles |
| 03 | main commands, data persistence |
| 03 | workshop on docker files |
| 04 | more commands in Dockerfile |
| 04 | layers |
| 04 | Dockerfile workshop 2 |
|-------|--------------------------------------------------|
| 05 | Big recap on day 1 and 2 |
| 05 | Dockerfile workshop 3 |
| 05 | Docker compose |
| 06 | Workshop on Docker compose |
| 06 | Docker compose II: more advanced  |
| 06 | Workshop on Docker compose II |
|-------|--------------------------------------------------|
| 07 | recap |
| 07 | let's build an app and productionize it |

__________________________
--------------------------

Generalités
--------------------------

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