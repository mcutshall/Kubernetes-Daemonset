# AUT-1131
POC - Build a Kubernetes Daemonset to handle undeploying stale applications in the test environment

The python app prints info about current deployments. Output formatting is rough for now.


General steps:

1. Run 'sudo kubectl create -f daemonset-test.yaml'
2. Check daemonset status with 'sudo kubectl get daemonset'
3. Copy name of daemonset container after running 'sudo kubectl get pods'
4. Show output from python app in daemonset container with 'sudo kubectl logs <pod_name>'
