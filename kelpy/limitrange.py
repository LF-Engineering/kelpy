import yaml

from kubernetes.client.exceptions import ApiException


def create(client, spec, namespace="default"):
    body = yaml.safe_load(spec)

    try:
        response = client.create_namespaced_limit_range(namespace, body)
    except ApiException as e:
        if e.reason == "Conflict":
            return False
        raise e
    return response


def get(client, name, namespace="default"):
    try:
        response = client.read_namespaced_limit_range(name, namespace)
    except ApiException as e:
        if e.reason == "Not Found":
            return None
        raise e

    return response


def delete(client, name, namespace="default"):
    try:
        response = client.delete_namespaced_limit_range(name, namespace)
    except ApiException as e:
        if e.reason == "Not Found":
            return False
        raise e
    return response
