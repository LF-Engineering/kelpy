from behave import *

from kelpy import deployment
from kubernetes import config, client
from jinja2 import Environment, FileSystemLoader


@given(u'A deployment called {deployment_name} does not exist')
def step_impl(context, deployment_name):
    deployment.delete(context.k8s_v1_apps_client, deployment_name)


@when(u'the deployment called whilrwind is created')
def step_impl(context):
    env = Environment(
            loader = FileSystemLoader('./templates'),   
            trim_blocks=True, 
            lstrip_blocks=True
            )
    deployment_tmpl = env.get_template('deployment.j2')
    deployment_spec_file = deployment_tmpl.render(deployment_name = "whilrwind")
    context.create_whilrwind_resp = deployment.create(context.k8s_v1_apps_client, deployment_spec_file)


@then(u'a valid deployment called whilrwind can be found')
def step_impl(context):
    print(context.create_whilrwind_resp.status.replicas)
    assert context.create_whilrwind_resp.status.replicas == context.create_whilrwind_resp.status.available_replicas
