from kubernetes.client.exceptions import ApiException


def create(client, name, namespace_manifest=None):
    """Create a namespace if it doesn't exist, if it does, return False.

    :core_v1_api: The core V1 API object.
    :name: The name of the namespace.
    :returns: True on creation, False if it already exists.

    """

    if namespace_manifest is None:
        namespace_manifest = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {"name": name, "resourceversion": "v1"},
        }

    try:
        client.create_namespace(body=namespace_manifest)
    except ApiException as e:
        # If the namespace already exists, return False.
        if e.reason == "Conflict":
            return False

        raise e

    return True


def get(client, name):
    field_selector = "metadata.name={0}".format(name)

    response = client.list_namespace(field_selector=field_selector)

    if len(response.items) == 1:
        return response

    return None
