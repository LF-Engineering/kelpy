from behave import *

from kelpy import cronjob
from kubernetes import config, client
from jinja2 import Environment, FileSystemLoader


@when("the CronJob called {cronjob_name} is created")
@given("the CronJob called {cronjob_name} exists")
def step_impl(context, cronjob_name):
    cronjob_namespace = "default"

    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
    )
    cronjob_tmpl = env.get_template("cronjob.j2")
    cronjob_spec_file = cronjob_tmpl.render(
        cronjob_name=cronjob_name, cronjob_namespace=cronjob_namespace
    )
    context.create_resp = cronjob.create(
        context.k8s_v1_batch_client, cronjob_spec_file, cronjob_namespace
    )


@when("the user attempts to retrieve the CronJob {cronjob_name}")
def step_impl(context, cronjob_name):
    context.get_resp = cronjob.get(context.k8s_v1_batch_client, cronjob_name)


@given("a CronJob called {cronjob_name} does not exist")
def step_impl(context, cronjob_name):
    cronjob.delete(context.k8s_v1_batch_client, cronjob_name)


@then("None is returned instead of the CronJob")
def step_impl(context):
    assert context.get_resp is None, "Did not return None"


@then("Results for the CronJob {cronjob_name} are returned")
def step_impl(context, cronjob_name):
    assert context.get_resp, "Should've returned a valid response"


@then("a valid CronJob called {cronjob_name} can be found")
def step_impl(context, cronjob_name):
    assert context.create_resp, f"Should've found {cronjob_name} CronJob"
