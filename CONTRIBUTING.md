# Contributing to AGridable

First of all, thank you for taking the time to contribute to the project! We love having you here 😄

## Table of Contents

- [Getting started](#getting-started)
- [Testing](#testing)
- [Submitting a change](#submitting-a-change)
- [Style guide](#style-guide)
  - [Code](#code)
  - [Docstrings](#docstrings)
- [Raising a bug](#raising-a-bug)
- [Requesting a feature](#requesting-a-feature)
- [I need more help!](#i-need-more-help)

## Getting started

First, `cd` to the location where you want to store the AGridable repo and clone it using the command:

```bash
git clone https://github.com/Electrify-Video-Partners/AGridable.git
```

`cd` to the `AGridable` folder and install AGridable in editable mode using the command (it's recommended that you install the library in a virtual environment):

```bash
pip install -e .
```

Then install the `dev` extras:

```bash
pip install .[dev]
```

## Testing

You can run the unit tests using the command (while in the AGridable folder):

```bash
pytest
```

## Submitting a change

You can submit a change by raising a [pull-request](https://github.com/paypal/AGridable/pulls) and assigning the reviewer as James Laidler.

Please ensure that, before raising a pull-request:

- You merge your branch into the `development` branch, not the `main` branch (as the `development` branch is used for staging changes before they are merged with the `main` branch).
- Commit messages are concise and informative.
- A comment is added to your PR giving a summary of the changes and why they were made.
- Your contribution conforms to the [Style guide](#style-guide).
- Your code has been profiled thouroughly to ensure runtime is optimised.
- Unit tests are added/extended.
- Unit test coverage is 100%.
- Docstrings are added/updated in the [numpy](https://numpydoc.readthedocs.io/en/latest/format.html) format, using the same style as the existing docstrings.

**Note:** when a pull-request is raised, the `Build` workflow will run, which ensures that unit tests, doctests and notebook tests all successfully run on multiple versions of Python. If the `Build` fails, the merge will also fail - if this happens, please consult the logs in the [Actions](https://github.com/paypal/AGridable/actions) area of the repo to see where the `Build` has failed.

## Style guide

### Code

Python code should follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) convention. It's recommended that you install [autopep8](https://pypi.org/project/autopep8/) before contributing, which will ensure that your code follows the PEP 8 convention.

### Docstrings

Docstrings should follow the [numpy](https://numpydoc.readthedocs.io/en/latest/format.html) format. Each class docstring should include an example.

## Raising a bug

You can raise a bug in the [Issues](https://github.com/Electrify-Video-Partners/AGridable/issues) area of the repo.

## Requesting a feature

You can request a new feature in the [Issues](https://github.com/Electrify-Video-Partners/AGridable/issues) area of the repo.

## I need more help

If you have any other queries or questions, feel free to contact James Laidler:

- [Email](james.a.laidler@gmail.com)
- [Linkedin](https://www.linkedin.com/in/james-laidler-430571a7)
