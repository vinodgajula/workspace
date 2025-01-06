Here's a comprehensive list of useful Kubernetes and Docker commands for your README file, tailored to managing your Flask application with Kubernetes and Docker Desktop:

---

## **Useful Commands for Kubernetes and Docker**

### **General Kubernetes Commands**
1. **Check the current Kubernetes context:**
   ```bash
   kubectl config current-context
   ```
2. **Switch Kubernetes context (e.g., Docker Desktop):**
   ```bash
   kubectl config use-context docker-desktop
   ```
3. **View all resources in the namespace:**
   ```bash
   kubectl get all
   ```
4. **Delete all resources in the namespace:**
   ```bash
   kubectl delete all --all
   ```

---

### **Managing Deployments**
1. **Apply a YAML file (create or update resources):**
   ```bash
   kubectl apply -f deployment.yaml
   ```
2. **Delete a deployment:**
   ```bash
   kubectl delete deployment flask-app
   ```
3. **Scale a deployment:**
   ```bash
   kubectl scale deployment flask-app --replicas=3
   ```
4. **Restart pods in a deployment:**
   ```bash
   kubectl rollout restart deployment flask-app
   ```

---

### **Managing Pods**
1. **List all pods:**
   ```bash
   kubectl get pods
   ```
2. **Describe a specific pod (for debugging):**
   ```bash
   kubectl describe pod <pod-name>
   ```
3. **View logs of a specific pod:**
   ```bash
   kubectl logs <pod-name>
   ```
4. **Delete all pods matching a label:**
   ```bash
   kubectl delete pod -l app=flask-app
   ```

---

### **Managing Services**
1. **List all services:**
   ```bash
   kubectl get services
   ```
2. **Describe a specific service:**
   ```bash
   kubectl describe svc flask-service
   ```
3. **Port forward a service to local machine:**
   ```bash
   kubectl port-forward svc/flask-service 8080:80
   ```

---

### **Debugging**
1. **Check events of a pod:**
   ```bash
   kubectl describe pod <pod-name>
   ```
2. **Check the logs of a pod:**
   ```bash
   kubectl logs <pod-name>
   ```
3. **Check service connectivity using `curl`:**
   ```bash
   curl http://localhost:<port>
   ```

---

### **Docker Commands**
1. **Build the Docker image:**
   ```bash
   docker build -t flask-app:latest .
   ```
2. **List Docker images:**
   ```bash
   docker images
   ```
3. **Save a Docker image to a file:**
   ```bash
   docker save -o flask-app.tar flask-app:latest
   ```
4. **Load a Docker image from a file:**
   ```bash
   docker load < flask-app.tar
   ```
5. **Run the container locally (for testing):**
   ```bash
   docker run -p 5000:5000 flask-app:latest
   ```

---

### **Deployment Workflow**
1. **Build and load the Docker image:**
   ```bash
   docker build -t flask-app:latest .
   docker save -o flask-app.tar flask-app:latest
   docker load < flask-app.tar
   ```
2. **Apply the Kubernetes configuration:**
   ```bash
   kubectl apply -f deployment.yaml
   ```
3. **Verify pods and services:**
   ```bash
   kubectl get pods
   kubectl get services
   ```
4. **Access the application:**
   - Check the `EXTERNAL-IP` of the service:
     ```bash
     kubectl get services
     ```
   - Access via `http://localhost:<service-port>` (for Docker Desktop).

kubectl scale deployment flask-app --replicas=0
