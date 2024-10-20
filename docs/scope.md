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
| 04.01 | intro | ✅  |
| 04.02 | optimizing, layers, cache, subtleties, choosing images | ✅  |
| 04.03 | Dockerfile workshop 2: Question app with OpenAI | ✅  |
|-------|-----------------------|----------|
| 05.01 | Quick Recap on day 1 and 2: Dockerfiles | ⚙️⚙️ |
| 05.02 | Docker Compose | ⚙️⚙️ |
| 05.03 | Demo: Nginx, SQLite, Vue | - |
| 05 | exemples: airflow | - |
| 05 | exercice: wordpress, PostgreSQL | - |
|-------|-----------------------|----------|
| 05 | CI/CD, github actions | - |
| 06 | Workshop on Docker compose : bot discord | - |
| 06 | exit ticket | - |
|-------|-----------------------|----------|
| 07 | recap | - |
|-------|-----------------------|----------|
| 08 | projet | - |

Faire tourner plusieurs containers avec docker composer a partir d'un fichier `compose.yaml`

- overview docker compose
- cas d'utilisation et benefices
- elements du `compose.yaml`: services, network, volumes
- commandes CLI et flags
- demo : nginx, sqlite, vue
- exercice : wordpress, postgresql: ecrire le compose.yaml et le faire tourner
- suite: déploiement, secrets, config, restart
- exemples: Minecraft, airflow,
- integration dans un pipeline CI/CD
- projet : bot discord

## Maybe

| 04 | multi stage builds, | - |

## Ideas

- lifecycle : <https://training.play-with-docker.com/beginner-linux/> ... exercice ... mysql
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

Docker to serve LLM

- <https://towardsdatascience.com/reducing-the-size-of-docker-images-serving-llm-models-b70ee66e5a76>

## Docker Hub

Il y a des milliers d'images dispo sur Docker hub
par exemple

- itzg/minecraft-server: pour lancer un server minecraft
- pytorch/pytorch, tensorflow/tensorflow : pour du deep learning
- wordpress : pour un blog wordpress
- pythontelegrambot/python-telegram-bot : developping bots for telegram
- homeassistant/home-assistant : Raspberry Pi home automation (IoT)
- ethereum/client-go, openethereum/openethereum: run full Ethereum nodes

## classic games server on your local

docker pull antoine13/retroarch-web-games

docker-compose up -d
After the container is up and running, open your web browser and navigate to <http://localhost:8080> to start using the RetroArch web player.

see also 2048, tetris, Chess, etc

## Docker architecture

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
