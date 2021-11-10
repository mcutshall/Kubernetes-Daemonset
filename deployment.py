import datetime
import pytz
from kubernetes import client, config

#DEPLOYMENT_NAME = "sv-kubernetes-example"

def list_pods(api):
    config.load_kube_config()

    v1 = client.CoreV1Api()
    #ret = v1.list_pod_for_all_namespaces(watch=False)
    namespace = 'default'
    ret = v1.list_namespaced_pod(namespace)

    for i in ret.items:
        print("%s\t%s\t%s" %(i.metadata.name, i.metadata.namespace, i.status.pod_ip))

def list_deployments(api):
    config.load_kube_config()

    v1 = client.CoreV1Api()
    #ret = v1.list_deployment_for_all_namespaces(watch=False)
    namespace = 'default'
    ret = v1.list_namespaced_deployment(namespace)

    print("{:<15} {:<15} {:<10}" . format('NAME', 'NAMESPACE', 'IMAGE'))
    for i in ret.items:
        print("{:<15} {:<15} {:<10}" . format(i.metadata.name, i.metadata.namespace, i.spec.template.spec.containers[0].image))
        #print("%s\t\t%s\t%s" %(i.metadata.name, i.metadata.namespace, i.spec.template.spec.containers[0].image))

def check_deployment(api):
    config.load_kube_config()
    api = client.AppsV1Api()

    ret = v1.list_deployment_for_all_namespaces(watch=False)
    api_instance = kubernetes.client.AppsV1Api(apt_client)

    name = ''
    namespace = ''
    pretty = 'false'

    for i in ret.items:
        resp = api_instance.read_namespaced_deployment_status(name, namespace, pretty=pretty)
        if(resp.status.conditions.status == False):
            delete_deployment(api, name)


def delete_deployment(api, dep_name):
    response = api.delete_namespaced_deployment(
        #name = DEPLOYMENT_NAME,
        name = dep_name,
        namespace = "default",
        body = client.V1DeleteOptions(
            propagation_policy = "Foreground",
            grace_period_seconds = 5
        ),
    )
    print("\n[INFO] deployment %s deleted." %(DEPLOYMENT_NAME))


def hello_world():
    print("Hello World!")


def main():
    #config.load_kube_config()
    #apps_v1 = client.AppsV1Api()

    #list_deployments(apps_v1)
    #check_deployment(apps_v1)

    hello_world()

if __name__ == "__main__":
    main()
