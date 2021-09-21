from behave import *

from kelpy import deployment
from kubernetes import config, client
from jinja2 import Environment, FileSystemLoader


@given(u"a deployment called {deployment_name} does not exist")
def step_impl(context, deployment_name):
    deployment.delete(context.k8s_v1_apps_client, deployment_name)


@when(u"the user attempts to retrieve the deployment {deployment_name}")
def step_impl(context, deployment_name):
    context.get_resp = deployment.get(context.k8s_v1_apps_client, deployment_name)


@then(u"None is returned instead of the deployment")
def step_impl(context):
    assert context.get_resp is None, "Did not return None"


@when(u"the deployment called {deployment_name} is created")
def step_impl(context, deployment_name):
    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
    )
    deployment_tmpl = env.get_template("deployment.j2")
    deployment_spec_file = deployment_tmpl.render(deployment_name=deployment_name)
    context.create_resp = deployment.create(
        context.k8s_v1_apps_client, deployment_spec_file
    )


@then(u"a valid deployment called whilrwind can be found")
def step_impl(context):
    assert (
        context.create_resp.status.replicas
        == context.create_resp.status.available_replicas
    )


@given(u"the deployment called {deployment_name} exists")
def step_impl(context, deployment_name):
    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
    )
    deployment_tmpl = env.get_template("deployment.j2")
    deployment_spec_file = deployment_tmpl.render(deployment_name=deployment_name)
    context.create_resp = deployment.create(
        context.k8s_v1_apps_client, deployment_spec_file
    )


@then(u"Results for the deployment fire are returned")
def step_impl(context):
    assert context.get_resp, "Should've returned a valid response"
