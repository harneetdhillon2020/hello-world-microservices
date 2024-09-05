# Assignment 1: Hello World Microservice
## Requirements
- Download Docker
- Download Minikube
- Download Python
- Download Flask
- Download Git

## Running
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
    ```bash
        image: <your-dockerhub-username>/hello-service:latest


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

9. Verify deployment: 
    ```bash
    kubectl get deployments
    kubectl get pods
    kubectl get svc
10. Response:
    ```bash 
    harneet@Harneets-MacBook-Pro hello-world-microservices % kubectl get deployments
    NAME               READY   UP-TO-DATE   AVAILABLE   AGE
    hello-deployment   1/1     1            1           2d2h
    world-deployment   1/1     1            1           2d2h
    harneet@Harneets-MacBook-Pro hello-world-microservices %     kubectl get pods
    NAME                                READY   STATUS    RESTARTS      AGE
    hello-deployment-7b56c65ddd-m99qb   1/1     Running   1 (37s ago)   2d2h
    world-deployment-59598fdf45-5vj69   1/1     Running   1 (37s ago)   2d2h
    harneet@Harneets-MacBook-Pro hello-world-microservices %     kubectl get svc
    NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
    hello-service   NodePort    10.102.34.154    <none>        5000:30793/TCP   2d2h
    kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP          2d2h
    world-service   NodePort    10.111.127.213   <none>        5001:30128/TCP   2d2h


11. Launch Services On Separate Terminals
    ```bash 
    minikube service hello-service 
    minikube service world-service 

12. Response:
    ```bash
        harneet@Harneets-MacBook-Pro hello-world-microservices %     minikube service hello-service 
    |-----------|---------------|-------------|---------------------------|
    | NAMESPACE |     NAME      | TARGET PORT |            URL            |
    |-----------|---------------|-------------|---------------------------|
    | default   | hello-service |        5000 | http://192.168.49.2:30793 |
    |-----------|---------------|-------------|---------------------------|
    🏃  Starting tunnel for service hello-service.
    |-----------|---------------|-------------|------------------------|
    | NAMESPACE |     NAME      | TARGET PORT |          URL           |
    |-----------|---------------|-------------|------------------------|
    | default   | hello-service |             | http://127.0.0.1:49702 |
    |-----------|---------------|-------------|------------------------|
    🎉  Opening service default/hello-service in default browser...
    ❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.

    harneet@Harneets-MacBook-Pro hello-world-microservices % minikube service world-service
    |-----------|---------------|-------------|---------------------------|
    | NAMESPACE |     NAME      | TARGET PORT |            URL            |
    |-----------|---------------|-------------|---------------------------|
    | default   | world-service |        5001 | http://192.168.49.2:30128 |
    |-----------|---------------|-------------|---------------------------|
    🏃  Starting tunnel for service world-service.
    |-----------|---------------|-------------|------------------------|
    | NAMESPACE |     NAME      | TARGET PORT |          URL           |
    |-----------|---------------|-------------|------------------------|
    | default   | world-service |             | http://127.0.0.1:49768 |
    |-----------|---------------|-------------|------------------------|
    🎉  Opening service default/world-service in default browser...
    ❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.


    

12. Acccessing Services<p>
type  ```/hello``` at the end of the hello service url and you will see a "Hello" message <p>
type ```/world``` at the end of the  world service url and you will see a "World" message



## Testing With Port Forwarding
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

## Image Links 
Hello Service:
https://hub.docker.com/repository/docker/harneetdhillon5/hello-service/general

World Service
https://hub.docker.com/repository/docker/harneetdhillon5/world-service/general