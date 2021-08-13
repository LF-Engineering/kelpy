from behave import *

from kelpie import namespace
from kubernetes import config, client


@given(u"a namespace called rain does not exist")
def step_impl(context):
    namespace.delete(context.k8s_v1_core_client, "rain")


@when(u"the user attempts to retrieve the namespace rain")
def step_impl(context):
    try:
        context.response = namespace.get(context.k8s_v1_core_client, "rain")
        assert True
    except Exception as e:
        raise e


@then(u"None is returned")
def step_impl(context):
    if context.response is not None:
        assert False


@given(u"that a namespace called washington does not exist")
def step_impl(context):
    raise NotImplementedError(
        u"STEP: Given that a namespace called washington does not exist"
    )


@when(u"the user creates a namespace called washington")
def step_impl(context):
    raise NotImplementedError(
        u"STEP: When the user creates a namespace called washington"
    )


@then(u"results containing the washington namespace are returned")
def step_impl(context):
    raise NotImplementedError(
        u"STEP: Then results containing the washington namespace are returned"
    )


@given(u"a namespace called bread exists")
def step_impl(context):
    raise NotImplementedError(u"STEP: Given a namespace called bread exists")


@when(u"the user retrieves the namespace bread")
def step_impl(context):
    raise NotImplementedError(u"STEP: When the user retrieves the namespace bread")


@then(u"results for the namespace bread  are returned")
def step_impl(context):
    raise NotImplementedError(
        u"STEP: Then results for the namespace bread  are returned"
    )
