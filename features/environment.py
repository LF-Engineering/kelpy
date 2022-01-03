from behave import *
from kubernetes import config, client


def before_all(context):
    config.load_kube_config(context="minikube")
    context.k8s_v1_core_client = client.CoreV1Api()
    context.k8s_v1_apps_client = client.AppsV1Api()
    context.k8s_v1_batch_client = client.BatchV1Api()
