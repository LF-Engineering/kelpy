# Kelpie

A light-weight helper library to simplify common Kubernetes operations and help keep code [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

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
