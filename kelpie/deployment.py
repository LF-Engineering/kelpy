import yaml
from kubernetes.client.exceptions import ApiException


def create(client, spec, namespace="default"):
    body = yaml.safe_load(spec)

    try:
        response = client.create_namespaced_deployment(namespace, body)
    except ApiException as e:
        # If the object already exists, return False.
        if e.reason == "Conflict":
            return False
        raise e

    return response


def get(client, name, namespace="default"):
    try:
        response = client.read_namespaced_deployment(name, namespace)
    except ApiException as e:
        if e.reason == "Not Found":
            return None
        raise e

    return response


def pod_selector(client, name, namespace="default"):

    response = get(client, name, namespace)

    if response:
        if response.status.available_replicas > 0:
            labels = response.spec.selector.match_labels
            label_selector = ",".join(
                "%s=%s" % (key, val) for (key, val) in labels.items()
            )
            return label_selector

    return None
