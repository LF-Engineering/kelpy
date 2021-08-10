import yaml
from kubernetes.client.exceptions import ApiException


def create(client, spec, namespace="default"):
    body = yaml.safe_load(spec)

    try:
        client.create_namespaced_deployment(namespace, body)
    except ApiException as e:
        # If the object already exists, return False.
        if e.reason == "Conflict":
            return False
        raise e

    return True


def get(client, name, namespace="default"):
    try:
        response = client.read_namespaced_deployment(name, namespace)
    except ApiException as e:
        if e.reason == "Not Found":
            return None
        raise e

    return response


def pod_selector(client, name, namespace="default"):

    resp = get(client, name, namespace)

    if resp:
        if resp.status.available_replicas > 0:
            labels = resp.spec.selector.match_labels
            label_selector = ",".join(
                "%s=%s" % (key, val) for (key, val) in labels.items()
            )
            return label_selector

    return None
