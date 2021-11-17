import datetime
import pytz
import time
import sys
from datetime import timezone, timedelta
from kubernetes import client, config

def list_pods(api):
    config.load_incluster_config()

    v1 = client.AppsV1Api()
    namespace = 'default'
    ret = v1.list_namespaced_pod(namespace)

    for i in ret.items:
        print("%s\t%s\t%s" %(i.metadata.name, i.metadata.namespace, i.status.pod_ip))

def list_deployments(api):
    config.load_incluster_config()

    v1 = client.AppsV1Api()
    namespace = 'default'
    ret = v1.list_namespaced_deployment(namespace)

    print("{:<15} {:<15} {:<10}" . format('NAME', 'NAMESPACE', 'IMAGE'))
    for i in ret.items:
        print("{:<15} {:<15} {:<10}" . format(i.metadata.name, i.metadata.namespace, i.spec.template.spec.containers[0].image))

def check_deployment(api, ageLimit):
    config.load_incluster_config()
    v1 = client.AppsV1Api()
    namespace = 'default'

    ret = v1.list_namespaced_deployment(namespace)

    today = datetime.datetime.now(timezone.utc)
    for i in ret.items:
        name = i.metadata.name
        timestamp = i.metadata.creation_timestamp
        print("Creation timestamp: %s" %(timestamp))

        age = today - timestamp
        print("Age: %s" %(age))
        print("Age in seconds: %s" %(age.total_seconds()))
        print("Age in minutes: %s" %(age / timedelta(minutes=1)))

        print("ageLimit: %s" %(ageLimit))
        #age = age / timedelta(minutes=1)
        #if(age >= ageLimit):
        #    delete_deployment(api, name)

def delete_deployment(api, dep_name):
    response = api.delete_namespaced_deployment(
        name = dep_name,
        namespace = "default",
        body = client.V1DeleteOptions(
            propagation_policy = "Foreground",
            grace_period_seconds = 5
        ),
    )
    print("\n[INFO] deployment %s deleted." %(name))

def check_pods(api, name):
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    namespace = "default"

    ret = v1.list_namespaced_pod(namespace)
    for i in ret.items:
        if name in i.metadata.name:
            delete_pods(i.metadata.name)

def delete_pods(name):
    api = client.CoreV1Api()
    resp = api.delete_namespaced_pod(
        name = name,
        namespace = "default",
        pretty = 'False'
    )

def hello_world():
    print("Hello World!")

def main():
    config.load_incluster_config()
    apps_v1 = client.AppsV1Api()
    ageLimit = 0

    if(len(sys.argv) != 2):
        ageLimit = 60
    else:
        ageLimit = sys.argv[1]

    while(True) :
        list_deployments(apps_v1)
        check_deployment(apps_v1, ageLimit)
        hello_world()
        #check_pods(apps_v1, "sv-nfs")
        time.sleep(30)

if __name__ == "__main__":
    main()
