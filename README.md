# deployment

## Building and Running the Application
### The application is currently accessible at:
```
http://ryan.zorran.tech
```
### Docker
To build and push the Docker containers, run the following commands within the deployment folder.

Backend
```bash
cd server
docker build -t <your-dockerhub-username>/pokemon-server:latest .
docker push <your-dockerhub-username>/pokemon-server:latest .
```

Frontend
```bash
cd client
docker build -t <your-dockerhub-username>/pokemon-client:latest
docker push <your-dockerhub-username>/pokemon-client:latest
```

For example, I used the following docker images:

Backend
```bash
docker build -t morganandrus/ryan-backend:latest .
docker push morganandrus/ryan-backend:latest
```

Frontend
```bash
docker build -t morganandrus/ryan-frontend:latest .
docker push morganandrus/ryan-frontend:latest
```

### Kubernetes
Run the following in the deployment folder. 

```bash
cd kube
kubectl apply -f .
```

Optionally, you can change the yaml files to use your created Docker images. 