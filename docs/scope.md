# Scope du cours

- Connaître les caractéristiques d'un conteneur et découvrir Docker

- Installer et utiliser Docker

- Maîtriser la persistance des données avec Docker

- Utiliser Docker-Compose

- Maîtriser les notions réseaux de Docker


plus

- Dockerfile
- deployer une app dockerisée sur Azure

__________________________
--------------------------
Generalités
--------------------------



# Pourquoi docker?

- Docker c'est quoi ?
- A quoi ca sert
- premier containers et images
- linux 


> But : savoir faire tourner une image docker dans un container, se connecter au container, start, stop etc 


Docker is an open platform for developing, shipping, and running applications.

Docker est une platforme open source qui sert a developper, livrer et executer des applications 

https://docs.docker.com/get-started/docker-overview/

Docker provides the ability to package and run an application in a loosely isolated environment called a **container**.

The isolation and security lets you run many containers simultaneously on a given host. Containers are lightweight and contain everything needed to run the application, so you don't need to rely on what's installed on the host. You can share containers while you work, and be sure that everyone you share with gets the same container that works in the same way.

Docker provides tooling and a platform to manage the lifecycle of your containers:

*     Develop your application and its supporting components using containers.
*     The container becomes the unit for distributing and testing your application.
*     When you're ready, deploy your application into your production environment, as a container or an orchestrated service. This works the same whether your production environment is a local data center, a cloud provider, or a hybrid of the two.


Docker pour ne plus entendre: mais ca marche sur ma machine !

scenarios:
- multiples versions d'une appli (postgres, python, ...)

quand on a besoin de differents stacks ou differents environnements sur une machine 

par exemple : faire tourner un environnement de developpement de  staging et acceder a l'environnement de production

ou besoin de faire touner une application, sur plusieurs machines 

- autres devs
- VM en production 
- projet open source
- etc


__________________________
--------------------------
Setup local
--------------------------


# Install Docker Desktop

https://docs.docker.com/get-started/get-docker/


Installer docker desktop sur windows
https://gailloty.net/fr/post/docker-windows/


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
After the container is up and running, open your web browser and navigate to http://localhost:8080 to start using the RetroArch web player.

see also 2048, tetris, Chess, etc 





# Acceder au terminal dans windows et mac

WSL vs ...




# simple docker run from the command line 

Il y a equivalence entre les bouton Pull et Run dans ddocker desktop et la ligne de command dans le terminal

- docker pull
- docker run
- docker stop
- docker container ls 
- docker ps & docker ps -a

docekr help pour toute la liste des commaneds disponibles

pour supprimer 

- docker rm (containers)
- docker rmi (images)

you can also search for images with ```docker search```



## 1st container de bienvenue

```bash
docker run -d -p 8080:80 docker/welcome-to-docker
```

puis dans le navigateur: http://localhost:8080/


allez ensuite dans docker desktop > containers 
vous voyez 

- un nom : ce nom est généré aléatoirement. Il comporte toujours 2  parties
- un hash : identifiant unique du container
- image : L'image du container 
- status : running / exited ?
- port : 
- last started : date de start
- des actions : view image, copy docker run,  view files, stop, start, pause etc 




##  pull Alpine from the CLI

Alpine est une version plus legere de Linux que Ubuntu

Beaucoup des images python et autres sont construitres a partir de Alpine


Dans un terminal

```bash
docker run -i -t alpine /bin/bash
```

what happens?

docker 

* pull the ubuntu image 
* creates a container 
* a network interface to connect to it (assigning an IP address to the container)
* starts the container and executes /bin/bash

et voila vous avez ubuntu sur votre machine 

> command pour verifier la version de ubuntu

```bash
apt-get update && apt-get install -y lsb-release 
lsb_release -a
```

devrait retourner 

```bash
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 24.04 LTS
Release:	24.04
Codename:	noble
```

pour sortir 

```bash
exit
```
the container stops but isn't removed. You can start it again or remove it.

si vous runnez ```docker run -i -t ubuntu /bin/bash``` à nouveau vous etes instantanement dans ubuntu


De meme vous pouvez acceder au container dans Docker Desktop 
clicquez sur le nom du container et le tab terminal

### Les flags -i et -t

The flags -i and -t in the Docker run command serve specific purposes:

-i (Interactive):

Keeps STDIN open even if not attached
Allows you to interact with the container's shell


-t (TTY):

Allocates a pseudo-TTY (terminal)
Provides a terminal driver, enabling a more functional, interactive shell experience



When used together, -i -t (often combined as -it) allows you to:

Create an interactive shell session within the container
Have a fully functional terminal experience, including features like command history and line editing

This combination is commonly used when you want to run a container and immediately interact with its shell, as in your example where you're launching a bash shell in an Ubuntu container.

essayer 

```docker run ubuntu /bin/bash```
et avec ou sans -i et -t

# Recap : container vs image ?
- quelle difference entre un container et une image ?
- in docker what's the difference between a container and an image ?


Une image est un fichier immutable qui contient tout ce qui est necessaire pour runner une application

ex: ubuntu, ... l'app de bienvenue 

On peut construire sa propre image en écrivant un Dockerfile : specifier tout ce dont on a besoin

Un container est une instance d'une image en cours d'execution (running)

C'est un environnemen t d'execiution real time ou l'application run

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

__________________________
--------------------------
Linux - crash course
--------------------------

# Linux 

## distros

Ubuntu
Debian
Redhat
...

## why linux rules the world ?

so is docker always running linux OS ?
No you can also run other OSs : 

## crash course into linux

how to on the command line 
bash vs dos
permissions: chmod
sudo ...
top

* vim !!

### CLI and flags

help page 

### Install stuff on debian / ubuntu

sudo apt get
apt get update

exemple install git on ubuntu

start ubtunu docekr
get in the terminal 
run ... install git commands

# Clean up
Clean your docker host using the commands (in bash):

$ docker rm -f $(docker ps -a -q)


# Docker hub

Creer un compte 

# PWD Play with docker


Exercice 



https://training.play-with-docker.com/beginner-linux/


--- fin de l'intro

# How to build Your First Alpine Docker Image and Push it to DockerHub

https://dockerlabs.collabnix.com/beginners/building-your-first-alpine-container.html



__________________________
--------------------------
Docker files
--------------------------



https://dockerlabs.collabnix.com/presentation/docker_workshop_1.html#/70


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
https://dockerlabs.collabnix.com/presentation/docker_workshop_1.html#/110

WORKDIR

__________________________
--------------------------
Docker architecture
--------------------------


# Docker architecture

https://docs.docker.com/get-started/docker-overview/#docker-architecture

explain : https://docs.docker.com/get-started/images/docker-architecture.webp


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
https://www.coursera.org/learn/docker-for-the-absolute-beginner

project
https://www.coursera.org/projects/docker-for-absolute-beginners

# labs
https://dockerlabs.collabnix.com/

https://github.com/collabnix/dockerlabs/blob/master/beginners/README.md


play with docker
https://labs.play-with-docker.com/

