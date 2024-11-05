# Reading Kubernetes

Kubernetes is an orchestrator of containerized cloud-native microservices apps.” We now know this means: Kubernetes deploys and manages applications that are packaged as containers and can easily scale, self-heal, and be updated.

Orchestrator is jargon for a system that deploys and manages applications.

 Kubernetes can:
• Deploy applications
• Scale them up and down based on demand
• Self-heal them when things break
• Perform zero-downtime rolling updates and rollbacks

## Cloud native

Cloud-native applications possess cloud-like features such as auto-scaling, self-healing, automated updates, rollbacks, and more.
Simply running a regular application in the public cloud does not make it cloud-native.

1. It abstracts infrastructure (such as AWS)
2. It simplifies moving applications between clouds

### K8s History

The word Kubernetes originates from the Greek word for helmsman or the person who steers a ship. You can see this in the logo, which is a ship’s wheel.

Some of the original engineers wanted to call Kubernetes Seven of Nine after the famous Borg drone from the TV series Star Trek Voyager. Copyright laws wouldn’t allow this, so they gave the logo seven spokes as a subtle reference to Seven of Nine.

You’ll often see it shortened to K8s and pronounced as “kates”. The number 8 replaces the eight characters between the “K” and the “s”.

### CRI

Kubernetes project created the container runtime interface (CRI) to make the runtime layer pluggable.

This means you can pick and choose the best runtimes for your needs.  better isolation, others provide better performance.

Kubernetes 1.24 finally removed support for Docker as a runtime as it was bloated and overkill for what Kubernetes needed.

Since then, most new Kubernetes clusters ship with `containerd` (pronounced “container dee”) as the default runtime.

Fortunately, `containerd` is a stripped-down version of Docker optimized for Kubernetes, and it fully supports applications containerized by Docker. In fact, Docker, `containerd`, and Kubernetes all work with images and containers that implement the Open Container Initiative (OCI)2 standards.

## 40k feet view

Kubernetes is both of the following:

- A cluster
- An orchestrator

## Kubernetes: Cluster

A Kubernetes cluster is one or more nodes providing CPU, memory, and other resources for use by applications.

Kubernetes supports two node types:

- Control plane nodes
- Worker nodes

**Control plane** nodes implement the Kubernetes intelligence,
every cluster needs at least one.
However, you should have three or five for high availability (HA).

Every **control plane** node runs every **control plane** service.

These include the **API server**, the **scheduler**, and the **controllers** that implement cloud-native features such as self- healing, autoscaling, and rollouts.

Worker nodes are for running user applications.

The control plane is a collection of system services that implement the brains of Kubernetes.

It exposes the API, schedules tasks, implements self-healing, manages scaling operations, and more.


## The API server

The API server is the front end of Kubernetes, and all requests to change and query the state of the cluster go through it. Even internal control plane services communicate with each other via the API server.
It exposes a RESTful API over HTTPS, and all requests are subject to authentication and authorization.

Deploying or updating an app follows this process:

1. Describe the requirements in a YAML configuration file
2. Post the configuration file to the API server
3. The request will be authenticated and authorized
4. The updates will be persisted in the cluster store
5. The updates will be scheduled to the cluster

## Cluster Store

The **cluster store** holds the desired state of all applications and cluster components and is the only stateful part of the control plane.
It’s based on the etcd distributed database, and most Kubernetes clusters run an etcd replica on every control plane node for HA.

Kubernetes clusters run an etcd replica on every control plane node for HA.

## controllers

controllers  implement a lot of the cluster intelligence.

- The Deployment controller
- The StatefulSet controller
- The ReplicaSet controller

## Scheduler

The scheduler watches the API server for new work tasks and assigns them to healthy worker nodes.


## worker nodes

**kubelet** is the main Kubernetes agent and handles all communication with the cluster.

It performs the following key tasks:
• Watches the API server for new tasks
• Instructs the appropriate runtime to execute tasks
• Reports the status of tasks to the API server


## Pods

Kubernetes runs containers, VMs, Wasm apps, and more. However, they all have to be wrapped in Pods to run on Kubernetes.
We’ll cover Pods shortly, but for now, think of them as a thin wrapper that abstracts different types of tasks so they can run on Kubernetes.

## Courier analogy / la poste

Couriers allow you to ship books, clothes, food, electrical items, and more, so long as you use their approved packaging and labels. Once you’ve packaged and labeled your goods, you hand them to the courier for delivery. The courier then handles the complex logistics of which planes and trucks to use, secure hand-offs to local delivery hubs, and eventual delivery to the customer. They also provide services for tracking packages, changing delivery details, and attesting successful delivery. All you have to do is package and label the goods.

Running apps on Kubernetes is similar. Kubernetes can run containers, VMs, Wasm apps and more, so long as you wrap them in Pods. Once wrapped in a Pod, you give the app to Kubernetes, and Kubernetes runs it. This includes the complex logistics of choosing appropriate nodes, joining networks, attaching volumes, and more. Kubernetes even lets you query apps and make changes.


Most couriers offer additional services such as insurance for the goods you’re shipping, signature and photographic proof of delivery, express delivery services, and more. All of these add value to the service.

Again, Kubernetes is similar. It implements controllers that add value, such as ensuring the health of apps, automatically scaling when demand increases, and more.


controler > pods > application (containers)


• The container wraps the app and provides dependencies
• The Pod wraps the container so it can run on Kubernetes
• The Deployment wraps the Pod and adds self-healing, scaling, and more

You post the Deployment (YAML file) to the API server as the desired state of the application, and Kubernetes implements it.


The declarative model and desired state are at the core of how Kubernetes operates. They operate on three basic principles:
• Observed state
• Desired state
• Reconciliation

Observed state is what you have, desired state is what you want, and reconciliation is the process of keeping observed state in sync with desired state.
Terminology: We use the terms actual state, current state, and observed state to mean the same thing — the most up-to-date view of the cluster.

the declarative model works like this:
1. You describe the desired state of an application in a YAML manifest file
2. You post the YAML file to the API server
3. It gets recorded in the cluster store as a record of intent
4. A controller notices the observed state of the cluster doesn’t match the new desired state
5. The controller makes the necessary changes to reconcile the differences
6. The controller keeps running in the background, ensuring observed state matches desired state



The most common way of posting **manifest** YAML files to Kubernetes is with the `kubectl` command-line utility.


Once authenticated and authorized, the configuration is persisted to the cluster store as a record of intent.
At this point, the observed state of the cluster doesn’t match your new desired state. A controller will notice this and begin the process of reconciliation. This will involve making all the changes described in the YAML file and is likely to include scheduling
2: Kubernetes principles of operation 21
new Pods, pulling images, starting containers, attaching them to networks, and starting application processes.
Once reconciliation is completed, observed state will match desired state, and every- thing will be OK. However, the controllers keep running in the background, ready to reconcile any future differences.
It’s important to understand that what we’ve described is very different from the traditional imperative model:
• The imperative model requires complex scripts of platform-specific commands to achieve an end-state
• The declarative model is a simple platform-agnostic way of describing an end state


The atomic unit of scheduling in the VMware world is the virtual machine (VM). In the Docker world, it’s the container. In Kubernetes, it’s the Pod.
Yes, Kubernetes runs containers, VMs, Wasm apps, and more. But they all need to be wrapped in Pods.