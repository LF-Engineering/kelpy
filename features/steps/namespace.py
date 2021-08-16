from behave import *

from kelpy import namespace
from kubernetes import config, client


@given(u"a namespace called {namespace_name} does not exist")
def step_impl(context, namespace_name):
    namespace.delete(context.k8s_v1_core_client, namespace_name)


@when(u"the user attempts to retrieve the namespace rain")
def step_impl(context):
    context.get_rain_resp = namespace.get(context.k8s_v1_core_client, "rain")


@then(u"None is returned")
def step_impl(context):
    assert context.get_rain_resp is None, "Did not return None"


@when(u"a namespace called washington is created")
def step_impl(context):
    context.create_washington_resp = namespace.create(
        context.k8s_v1_core_client, "washington"
    )


@then(u"results containing the washington namespace are returned")
def step_impl(context):
    assert context.create_washington_resp.status.phase == "Active"


@given(u"a namespace called bread exists")
def step_impl(context):
    context.create_bread_resp = namespace.create(
            context.k8s_v1_core_client, "bread"
            )


@when(u"the user retrieves the namespace bread")
def step_impl(context):
    context.get_bread_resp = namespace.get(context.k8s_v1_core_client, "bread")


@then(u"results for the namespace bread  are returned")
def step_impl(context):
    assert context.get_bread_resp is None, "Did not return None"

