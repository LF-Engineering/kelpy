from kubernetes.client.exceptions import ApiException


def list(client, label_selector, namespace="default"):
    try:
        response = client.list_namespaced_pod(
            namespace=namespace, label_selector=label_selector
        )
    except ApiException as e:
        if e.reason == "Not Found":
            return None
        raise e

    return response
