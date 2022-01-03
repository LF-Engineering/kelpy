from behave import *

from kelpy import job
from kubernetes import config, client
from jinja2 import Environment, FileSystemLoader


@given("a Job called {job_name} does not exist")
def step_impl(context, job_name):
    job.delete(context.k8s_v1_batch_client, job_name)


@given("the Job called {job_name} exists")
@when("the Job called {job_name} is created")
def step_impl(context, job_name):
    job_namespace = "default"

    env = Environment(
        loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True
    )
    job_tmpl = env.get_template("job.j2")
    job_spec_file = job_tmpl.render(job_name=job_name, job_namespace=job_namespace)
    context.create_resp = job.create(
        context.k8s_v1_batch_client, job_spec_file, job_namespace
    )


@when("the user attempts to retrieve the Job {job_name}")
def step_impl(context, job_name):
    context.get_resp = job.get(context.k8s_v1_batch_client, job_name)


@then("None is returned instead of the Job")
def step_impl(context):
    assert context.get_resp is None, "Did not return None"


@then("a valid Job called {job_name} can be found")
def step_impl(context, job_name):
    assert context.create_resp, f"Should've found {job_name} Job"


@then("Results for the Job {job_name} are returned")
def step_impl(context, job_name):
    assert context.get_resp, "Should've returned a valid response"
