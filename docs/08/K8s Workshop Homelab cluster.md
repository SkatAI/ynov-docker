# Kubernetes Workshop for Docker Users

Duration: 4 hours (can be split into 2 sessions)

- [Kubernetes Workshop for Docker Users](#kubernetes-workshop-for-docker-users)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions (15 minutes)](#setup-instructions-15-minutes)
  - [Module 1: From Docker Compose to Kubernetes (45 minutes)](#module-1-from-docker-compose-to-kubernetes-45-minutes)
    - [Hands-on Exercise: Converting Docker Compose to Kubernetes](#hands-on-exercise-converting-docker-compose-to-kubernetes)
    - [Practice Tasks:](#practice-tasks)
  - [Module 2: Kubernetes Core Concepts (60 minutes)](#module-2-kubernetes-core-concepts-60-minutes)
    - [Interactive Exercises:](#interactive-exercises)
  - [Module 3: Configuration and State (45 minutes)](#module-3-configuration-and-state-45-minutes)
    - [Hands-on Projects:](#hands-on-projects)
  - [Module 4: Real-world Application (75 minutes)](#module-4-real-world-application-75-minutes)
    - [Final Project:](#final-project)
    - [Implementation Steps:](#implementation-steps)
  - [Debugging Section (30 minutes)](#debugging-section-30-minutes)
  - [Workshop Materials](#workshop-materials)
    - [Required Files:](#required-files)
    - [Student Resources:](#student-resources)
  - [Follow-up Projects](#follow-up-projects)
  - [Tips for Instructors](#tips-for-instructors)
- [homelab](#homelab)

## Prerequisites

- Docker and Docker Compose installed
- 8GB RAM minimum
- 20GB free disk space
- Basic command line knowledge
- Git installed

## Setup Instructions (15 minutes)

1. Install kubectl
2. Install Minikube or Kind
3. Start local cluster
4. Verify installation

## Module 1: From Docker Compose to Kubernetes (45 minutes)

### Hands-on Exercise: Converting Docker Compose to Kubernetes

Start with a familiar Docker Compose application:

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "80:80"
  redis:
    image: redis
```

Convert to equivalent Kubernetes manifests:

```yaml
# deployment-web.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: nginx
---
# service-web.yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  type: NodePort
  ports:
  - port: 80
  selector:
    app: web
```

### Practice Tasks

1. Deploy both versions
2. Compare commands and outputs
3. Identify key differences

## Module 2: Kubernetes Core Concepts (60 minutes)

### Interactive Exercises

1. **Pod Lifecycle**
   - Create a pod manually
   - Observe states
   - Delete and recreate

2. **Deployments**
   - Scale replicas
   - Update image versions
   - Rollback changes

3. **Services**
   - Create ClusterIP service
   - Expose with NodePort
   - Test connectivity

## Module 3: Configuration and State (45 minutes)

### Hands-on Projects

1. **ConfigMaps**
   - Create from files and literals
   - Mount as volumes
   - Use as environment variables

2. **Secrets**
   - Create manually
   - Use in pods
   - Best practices

3. **Persistent Storage**
   - Local volumes
   - PersistentVolumeClaims
   - StatefulSet basics

## Module 4: Real-world Application (75 minutes)

### Final Project

Build a multi-tier application with:

- Frontend (Nginx)
- Backend API (Node.js/Python)
- Database (MongoDB)
- Redis cache

### Implementation Steps

1. Start with Docker Compose version
2. Convert to Kubernetes manifests
3. Add health checks
4. Implement scaling
5. Configure persistence
6. Set up internal networking

## Debugging Section (30 minutes)

Common Issues and Solutions:

1. Pod startup failures
2. Service networking issues
3. Storage problems
4. Resource constraints

## Workshop Materials

### Required Files

- Sample applications
- Solution files
- Troubleshooting guide
- Commands cheatsheet

### Student Resources

- Workshop slides
- Exercise instructions
- Reference architecture diagrams
- Best practices guide

## Follow-up Projects

Independent exercises for students:

1. Add monitoring with Prometheus
2. Implement basic CI/CD
3. Configure horizontal pod autoscaling
4. Set up development namespaces

## Tips for Instructors

1. Pre-verify all installations
2. Have backup cluster ready
3. Prepare common error solutions
4. Set resource limits in Minikube

# homelab

--- Yes, you can create a Kubernetes cluster using your laptops as nodes. This is often called a "homelab" cluster. I'll explain how this typically works.

```bash
#!/bin/bash

# Prerequisites installation script for Ubuntu/Debian systems
# Run this on all nodes (both master and workers)

# Update system
apt-get update && apt-get upgrade -y

# Install Docker
apt-get install -y docker.io
systemctl enable docker
systemctl start docker

# Install required packages
apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# Add Kubernetes repo
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
add-apt-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
apt-get update

# Install Kubernetes components
apt-get install -y kubelet kubeadm kubectl
systemctl enable kubelet

# Disable swap (required for Kubernetes)
swapoff -a
sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

# On master node only:
# Initialize the cluster (run only on the master node)
# Replace 192.168.1.100 with your master node's IP
kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=192.168.1.100

# Set up kubectl access for your user
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config

# Install network plugin (Flannel in this example)
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# The kubeadm init command will output a join command for worker nodes
# It will look something like this:
# kubeadm join 192.168.1.100:6443 --token <token> --discovery-token-ca-cert-hash <hash>

```

Here's how you can set this up:

1. Choose one laptop as the master node (control plane)
2. Use the remaining laptops as worker nodes
3. Requirements for each laptop:
   - Minimum 2 CPU cores
   - 2GB RAM
   - Ubuntu/Debian recommended for beginners
   - Static IP addresses

Key setup steps:

1. Run the prerequisite installation script on all laptops
2. Initialize the master node
3. Join worker nodes to the cluster
4. Install a network plugin (like Flannel)

Important considerations:

- All laptops must be on the same network
- Ensure consistent network connectivity
- Use static IP addresses for reliability
- The master node needs slightly more resources

Would you like me to explain any specific part of the setup in more detail?
I'll show you how to set up static IP addresses on different operating systems.

```bash
# Ubuntu/Debian (Using Netplan)
# Save as /etc/netplan/01-network-manager-all.yaml

network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:  # Your network interface name (might be different)
      dhcp4: no
      addresses:
        - 192.168.1.100/24  # Your desired IP/subnet mask
      gateway4: 192.168.1.1  # Your router's IP
      nameservers:
          addresses: [8.8.8.8, 8.8.4.4]  # DNS servers

# Windows (PowerShell commands)
# Replace values in brackets with your settings
New-NetIPAddress -InterfaceAlias "Wi-Fi" -IPAddress 192.168.1.101 -PrefixLength 24 -DefaultGateway 192.168.1.1
Set-DnsClientServerAddress -InterfaceAlias "Wi-Fi" -ServerAddresses "8.8.8.8","8.8.4.4"

# macOS (Terminal commands)
# Replace values in brackets with your settings
networksetup -setmanual "Wi-Fi" 192.168.1.102 255.255.255.0 192.168.1.1
networksetup -setdnsservers "Wi-Fi" 8.8.8.8 8.8.4.4

# Example IP allocation plan for 10 laptops:
# Master Node: 192.168.1.100
# Worker Node 1: 192.168.1.101
# Worker Node 2: 192.168.1.102
# Worker Node 3: 192.168.1.103
# Worker Node 4: 192.168.1.104
# Worker Node 5: 192.168.1.105
# Worker Node 6: 192.168.1.106
# Worker Node 7: 192.168.1.107
# Worker Node 8: 192.168.1.108
# Worker Node 9: 192.168.1.109

```

Here's how to set up static IPs:

1. First, gather network information:
   - Your router's IP (usually 192.168.1.1 or 192.168.0.1)
   - Your subnet mask (usually 255.255.255.0)
   - Available IP range in your network

2. Best practices:
   - Reserve a block of IPs for your cluster
   - Keep them sequential for easier management
   - Document which IP is assigned to which laptop
   - Stay away from DHCP range used by your router

3. Before setting static IPs:
   - Note down your current network interface name
   - Backup existing network configuration
   - Have a keyboard/monitor ready in case of connectivity issues

4. After setting static IPs:
   - Test connectivity between all nodes
   - Verify internet access
   - Make sure you can ping all nodes from each other

Would you like me to explain how to find your current network settings on any particular operating system?

Let me explain the types of applications that benefit from a home Kubernetes cluster.

```yaml
# Example distributed application deployment
# Save as distributed-app.yaml

---
# Database Service
apiVersion: v1
kind: Service
metadata:
  name: mongodb
spec:
  ports:
    - port: 27017
  selector:
    app: mongodb
---
# Database Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongodb
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongodb
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      containers:
        - name: mongodb
          image: mongo:latest
          ports:
            - containerPort: 27017
          volumeMounts:
            - name: mongo-storage
              mountPath: /data/db
      volumes:
        - name: mongo-storage
          persistentVolumeClaim:
            claimName: mongo-pvc
---
# Backend API Service
apiVersion: v1
kind: Service
metadata:
  name: backend-api
spec:
  ports:
    - port: 3000
  selector:
    app: backend-api
---
# Backend API Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-api
spec:
  replicas: 3  # Multiple replicas for load balancing
  selector:
    matchLabels:
      app: backend-api
  template:
    metadata:
      labels:
        app: backend-api
    spec:
      containers:
        - name: backend-api
          image: your-backend-image:latest
          ports:
            - containerPort: 3000
---
# Frontend Service
apiVersion: v1
kind: Service
metadata:
  name: frontend
spec:
  type: LoadBalancer
  ports:
    - port: 80
  selector:
    app: frontend
---
# Frontend Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 2  # Multiple replicas for high availability
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
        - name: frontend
          image: your-frontend-image:latest
          ports:
            - containerPort: 80

```

Here are the types of applications that would benefit from such a setup:

1. Development/Testing Environments:
   - Microservices applications in development
   - CI/CD pipeline testing
   - Replica of production environments
   - A/B testing scenarios

2. Learning/Educational:
   - Learning DevOps practices
   - Training environments for teams
   - Experimenting with cloud-native technologies
   - Testing deployment strategies

3. Small Production Workloads:
   - Personal projects needing high availability
   - Small business applications
   - Internal tools
   - Hobby projects requiring scalability

4. Specific Application Examples:
   - Distributed web applications with:
     - Load-balanced frontend
     - Scalable backend API
     - Database with persistent storage
   - Machine learning pipelines:
     - Distributed training jobs
     - Model serving
   - Media processing:
     - Video transcoding
     - Image processing pipeline
   - IoT applications:
     - Data collection
     - Real-time processing
     - Sensor data aggregation

The main benefits of such a setup are:

1. High Availability:
   - Services run across multiple machines
   - Automatic failover
   - Load balancing

2. Resource Utilization:
   - Better use of available hardware
   - Flexible resource allocation
   - Easy scaling

3. Learning:
   - Hands-on experience with container orchestration
   - Understanding distributed systems
   - Practice with real-world scenarios

Would you like me to elaborate on any of these use cases or show you how to deploy a specific type of application?

Yes, absolutely! We can set up monitoring across all nodes using Prometheus and node-exporter to collect metrics.

```yaml
# Create a monitoring namespace
apiVersion: v1
kind: Namespace
metadata:
  name: monitoring

---
# DaemonSet to run node-exporter on every node
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      containers:
      - name: node-exporter
        image: prom/node-exporter:latest
        ports:
        - containerPort: 9100
        volumeMounts:
        - name: proc
          mountPath: /host/proc
          readOnly: true
        - name: sys
          mountPath: /host/sys
          readOnly: true
      volumes:
      - name: proc
        hostPath:
          path: /proc
      - name: sys
        hostPath:
          path: /sys

---
# Service to expose node-exporter metrics
apiVersion: v1
kind: Service
metadata:
  name: node-exporter
  namespace: monitoring
spec:
  selector:
    app: node-exporter
  ports:
  - port: 9100
    targetPort: 9100

---
# ConfigMap for Prometheus configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: monitoring
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    scrape_configs:
      - job_name: 'node-exporter'
        kubernetes_sd_configs:
          - role: endpoints
            namespaces:
              names:
                - monitoring
        relabel_configs:
          - source_labels: [__meta_kubernetes_service_name]
            regex: node-exporter
            action: keep

---
# Prometheus Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      containers:
      - name: prometheus
        image: prom/prometheus:latest
        ports:
        - containerPort: 9090
        volumeMounts:
        - name: config
          mountPath: /etc/prometheus/
      volumes:
      - name: config
        configMap:
          name: prometheus-config

---
# Service to expose Prometheus
apiVersion: v1
kind: Service
metadata:
  name: prometheus
  namespace: monitoring
spec:
  type: NodePort
  selector:
    app: prometheus
  ports:
  - port: 9090
    targetPort: 9090
    nodePort: 30900

```

This setup will collect various metrics from each laptop/node, including:

1. System Metrics:
   - CPU usage
   - Memory utilization
   - Disk I/O
   - Network traffic
   - System load
   - Process statistics

2. Node-specific Information:
   - Number of running containers
   - Network interface statistics
   - File system usage
   - System uptime
   - Hardware temperature (if available)

To implement this:

1. Deploy the monitoring stack:

```bash
kubectl apply -f monitoring-setup.yaml
```

2. Access the metrics:
   - Prometheus UI: <http://any-node-ip:30900>
   - Query metrics using PromQL

Common useful metrics to monitor:

```promql
# CPU Usage per node
100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory usage per node
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# Disk usage
100 - ((node_filesystem_avail_bytes * 100) / node_filesystem_size_bytes)

# Network traffic
rate(node_network_receive_bytes_total[5m])
```

Would you like me to:

1. Show how to set up a visualization dashboard with Grafana?
2. Explain how to create custom metrics for your specific needs?
3. Demonstrate how to set up alerts based on these metrics?
