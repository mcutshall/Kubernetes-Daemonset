# AUT-1131
POC - Build a Kubernetes Daemonset to handle undeploying stale applications in the test environment

The python app prints info about current deployments. Output formatting is rough for now.


General steps:

1. Create new role and role binding for system user
```
      sudo kubectl create -f role-resource-access.yaml
      
      sudo kubectl create -f rolebinding-resource-access.yaml
```
2. Build the docker image locally
```
      sudo docker build -f Dockerfile -t daemonset-python:latest .
 ```     
3. Create the daemonset
```
      sudo kubectl create -f daemonset-test.yaml
```     
4. Check daemonset status
```
      sudo kubectl get daemonset
```      
5. Show output of python app in daemonset container
```
      sudo kubectl get pods  <-- copy name of daemonset pod
      
      sudo kubectl logs <pod_name>
```

Configuring Age Limit:

The age limit of a deployment can be configured by passing a command line argument in the Dockerfile. 

Default is 60 minutes.

Example:
```
      CMD ["python3", "/app/check-deployments.py", "120"]
```
This will set the ageLimit variable to 120 minutes.
