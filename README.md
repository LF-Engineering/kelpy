# Kelpy

![quality-control](https://github.com/LF-Engineering/kelpy/actions/workflows/qc.yml/badge.svg)

A light-weight helper library to simplify common Kubernetes operations and help keep code [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

While the official Kubernetes library provides users with everything required to work with the Kubernetes APIs, it
does so in a very basic way and is not designed to replicate the convenience of `kubectl`. For example, creating
a namespace that exists would usually raise a "Conflict" exception, whereas Kelpy will just return `False`.

Without Kelpy:

```python

from kubernetes import config, client
from kubernetes.client.exceptions import ApiException

config.load_kube_config()
core_v1 = client.CoreV1Api()


namespace_spec = {
    "apiVersion": "v1",
    "kind": "Namespace",
    "metadata": {"name": name, "resourceversion": "v1"},
}

try:
    response = client.create_namespace(body=namespace_spec)
except ApiException as e:
    if e.reason == "Conflict":
        print("I cannot create something that already exists.")

```

With Kelpy:

```python
from kelpy import namespace
from kubernetes import config, client

config.load_kube_config()
core_v1 = client.CoreV1Api()


if namespace.create(core_v1, name=namespace_name) is False:
    print("A namespace could not be created as it already exists")
```

Kelpy is designed to complement the official Kubernetes Python library and by no means replace it, ideally, just making it easier to use.


## Developing

To get started with the project, ensure you're running Python 3.9+ then run:

```
$ make setup
$ ./.venv/bin/activate
```
## Tests

### Functional

The functional tests using [behave](https://behave.readthedocs.io) can be executed
by running `make functional-tests`.

These tests leverage [minikube](https://minikube.sigs.k8s.io/docs/) so please
make sure you have minikube running and configured correctly.
