from behave import *

from kelpie import namespace
from kubernetes import config, client


@when(u"the create function is invoked")
def step_impl(context):
    raise NotImplementedError(u"STEP: When the create function is invoked")


@then(u"a new namespace is created")
def step_impl(context):
    raise NotImplementedError(u"STEP: Then a new namespace is created")


@when(u"a user tries to retrieve a namespace that doesn't exist None is returned.")
def step_impl(context):

    config.load_kube_config(context="minikube")
    core_v1 = client.CoreV1Api()

    missing_namespace = namespace.get(
        core_v1, name="2c300d4a-deb8-3dd9-af7d-90bb4b36d30b"
    )

    if missing_namespace:
        assert False
    else:
        assert True
