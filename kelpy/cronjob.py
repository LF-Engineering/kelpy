import yaml
from kubernetes.client.exceptions import ApiException
from kubernetes import watch


def create(client, spec: str, namespace: str = "default", timeout=100):
    """Create a CronJob.

    :batch_v1_api: The Batch V1 API object.
    :spec: A valid CronJob YAML manifest.
    :namespace: The namespace of the CronJob.
    :timeout: Timeout in seconds to wait for object creation/modification

    :returns: True on creation, False if it already exists.
    """
    body = yaml.safe_load(spec)

    try:
        response = client.create_namespaced_cron_job(namespace, body)
    except ApiException as e:
        # If the object already exists, return False.
        if e.reason == "Conflict":
            return False
        raise e

    name = body["metadata"]["name"]
    if get(client, name, namespace) is None:
        w = watch.Watch()
        for event in w.stream(
            client.list_cron_job_for_all_namespaces, timeout_seconds=timeout
        ):
            if (
                (event["type"] == "ADDED" or event["type"] == "MODIFIED")
                and event["object"].kind == "CronJob"
                and event["object"].metadata.name == response.metadata.name
                and event["object"].metadata.namespace == response.metadata.namespace
            ):
                break

    return response


def get(client, name: str, namespace: str = "default"):
    """Get a CronJob if it does exist, if it doesn't, return None.

    :batch_v1_api: The Batch V1 API object.
    :name: The name of the CronJob.
    :namespace: The namespace of the CronJob.

    :returns: CronJob if it does exist, None if it doesn't exist.
    """
    field_selector = "metadata.name={0}".format(name)

    response = client.list_namespaced_cron_job(namespace, field_selector=field_selector)

    if len(response.items) == 1:
        return response

    return None


def delete(client, name: str, namespace: str = "default", timeout=100):
    """Delete a CronJob if it does exist, if it doesn't, return False.

    :batch_v1_api: The Batch V1 API object.
    :name: The name of the CronJob.
    :namespace: The namespace of the CronJob.
    :timeout: Timeout in seconds to wait for object deletion

    :returns: Batch API Response if it does exist, False if it doesn't exist.
    """
    try:
        response = client.delete_namespaced_cron_job(name, namespace)
    except ApiException as e:
        if e.reason == "Not Found":
            return False
        raise e

    if get(client, name, namespace) is not None:
        w = watch.Watch()
        for event in w.stream(
            client.list_cron_job_for_all_namespaces, timeout_seconds=timeout
        ):
            if (
                event["type"] == "DELETED"
                and event["object"].metadata.name == name
                and event["object"].metadata.namespace == namespace
            ):
                break

    return response
