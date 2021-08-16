from kubernetes.client.exceptions import ApiException


def create(client, name, namespace_spec=None):
    """Create a namespace if it doesn't exist, if it does, return False.

    :core_v1_api: The core V1 API object.
    :name: The name of the namespace.
    :returns: True on creation, False if it already exists.

    """

    if namespace_spec is None:
        namespace_spec = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {"name": name, "resourceversion": "v1"},
        }

    try:
        response = client.create_namespace(body=namespace_spec)
    except ApiException as e:
        # If the namespace already exists, return False.
        if e.reason == "Conflict":
            return False
        raise e

    return response


def get(client, name):
    field_selector = "metadata.name={0}".format(name)

    response = client.list_namespace(field_selector=field_selector)

    if len(response.items) == 1:
        return response

    return None


def delete(client, name):
    try:
        response = client.delete_namespace(name)
    except ApiException as e:
        if e.reason == "Not Found":
            return False
        raise e

    return response
