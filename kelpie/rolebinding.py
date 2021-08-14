import yaml
from kubernetes.client.exceptions import ApiException


def create(client, spec, namespace="default"):
    body = yaml.safe_load(spec)

    try:
        response = client.create_namespaced_role_binding(namespace, body)
    except ApiException as e:
        # If the object already exists, return False.
        if e.reason == "Conflict":
            return False
        raise e

    return response


def get(client, name, namespace="default"):
    try:
        response = client.read_namespaced_role_binding(name, namespace)
    except ApiException as e:
        if e.reason == "Not Found":
            return None
        raise e

    return response
