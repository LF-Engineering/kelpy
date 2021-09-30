import yaml
from kubernetes.client.exceptions import ApiException
from kubernetes import watch


def create(client, spec, namespace="default", timeout=100):
    body = yaml.safe_load(spec)

    try:
        response = client.create_namespaced_deployment(namespace, body)
    except ApiException as e:
        # If the object already exists, return False.
        if e.reason == "Conflict":
            return False
        raise e

    w = watch.Watch()
    for event in w.stream(
        client.list_deployment_for_all_namespaces, timeout_seconds=timeout
    ):
        if (
            event["type"] == "ADDED"
            and event["object"].metadata.name == response.metadata.name
            and event["object"].status.available_replicas
            and event["object"].status.replicas
            == event["object"].status.available_replicas
        ):
            break

    return response


def get(client, name, namespace="default"):
    try:
        response = client.read_namespaced_deployment(name, namespace)
    except ApiException as e:
        if e.reason == "Not Found":
            return None
        raise e

    return response


def update(client, name, body, namespace="default", timeout=100):
    try:
        response = client.patch_namespaced_deployment(name, namespace, body)
    except ApiException as e:
        if e.reason == "Conflict":
            return False
        raise e

    w = watch.Watch()
    for event in w.stream(
        client.list_deployment_for_all_namespaces, timeout_seconds=timeout
    ):
        if (
            event["type"] == "ADDED"
            and event["object"].metadata.name == response.metadata.name
            and event["object"].status.available_replicas
            and event["object"].status.replicas
            == event["object"].status.available_replicas
        ):
            break

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


def delete(client, name, namespace="default", wait_for_timeout=180):
    try:
        response = client.delete_namespaced_deployment(name, namespace)
    except ApiException as e:
        if e.reason == "Not Found":
            return False
        raise e

    w = watch.Watch()
    for event in w.stream(
        client.list_deployment_for_all_namespaces, timeout_seconds=wait_for_timeout
    ):
        if (
            event["type"] == "DELETED"
            and event["object"].metadata.name == name
            and event["object"].metadata.namespace == namespace
        ):
            break
    return response
