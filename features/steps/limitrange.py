from behave import *

from kelpy import limitrange
from kubernetes import config, client
from jinja2 import Environment, FileSystemLoader


@when("the limitrange called {limitrange_name} is created")
@given("the limitrange called {limitrange_name} exists")
def step_impl(context, limitrange_name):
    limitrange_namespace = "default"

    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
    )

    limitrange_tmpl = env.get_template("limitrange.j2")
    limitrange_spec_file = limitrange_tmpl.render(
        limitrange_name=limitrange_name, limitrange_namespace=limitrange_namespace
    )
    context.create_resp = limitrange.create(
        context.k8s_v1_core_client, limitrange_spec_file, limitrange_namespace
    )


@when("the user attempts to retrieve the limitrange {limitrange_name}")
def step_impl(context, limitrange_name):
    context.get_resp = limitrange.get(context.k8s_v1_core_client, limitrange_name)


@given("a limitrange called {limitrange_name} does not exist")
def step_impl(context, limitrange_name):
    limitrange.delete(context.k8s_v1_core_client, limitrange_name)


@then("None is returned instead of the limitrange")
def step_impl(context):
    assert context.get_resp is None, "Did not return None"


@then("Results for the limitrange {limitrange_name} are returned")
def step_impl(context, limitrange_name):
    assert context.get_resp, "Should've returned a valid response"


@then("a valid limitrange called {limitrange_name} can be found")
def step_impl(context, limitrange_name):
    assert context.create_resp, f"Should've found {limitrange_name} limitrange"
