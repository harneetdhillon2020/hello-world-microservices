# Requirements
- Download Docker
- Download Minikube
- Download Python
- Download Git

# Running
1. Open Docker.
2. Clone the repository.
3. Build the Docker images:
   ```bash
   docker build -t <your-dockerhub-username>/hello-service:latest ./hello-service
   docker build -t <your-dockerhub-username>/world-service:latest ./world-service

4. Start Minicube 
    ```bash 
    minikube start


5. Update the `world-deployment.yaml` and `hello-deployment.yaml` files with your Docker Hub username for the image.

6. Build the docker images
    ```bash 
    docker build -t <your-dockerhub-username>/hello-service:latest -f hello-service/Dockerfile . 
    docker build -t <your-dockerhub-username>/world-service:latest -f world-service/Dockerfile .

7. Push the images
    ```bash 
    docker push <your-dockerhub-username>/hello-service:latest
    docker push <your-dockerhub-username>/world-service:latest

8. Apply the YAML files to your Kubernetes cluster:
    ```bash 
    kubectl apply -f hello-deployment.yaml
    kubectl apply -f world-deployment.yaml

9. verify deployment: 
    ```bash
    kubectl get deployments
    kubectl get pods
    kubectl get svc

10. Launch Services
    ```bash 
    minikube service hello-service 
    minikube service world-service 

11. Acccessing Endpoints<p>
type  ```/hello``` at the end of the url and you will see a "Hello" message <p>
type ```/world``` at the end of the url and you will see a "World" message


# Testing
1. Enable port forwarding on separate terminals
    ```bash 
    kubectl port-forward service/hello-service 5000:5000
    kubectl port-forward svc/world-service 5001:5001        
2. On a third terminal run 
    ```bash 
    python test.py 
3. It will return 
    ```bash
        Hello World

# Image Links 
Hello Service:
https://hub.docker.com/repository/docker/harneetdhillon5/hello-service/general

World Service
https://hub.docker.com/repository/docker/harneetdhillon5/world-service/general