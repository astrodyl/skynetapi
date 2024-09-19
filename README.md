# SkynetAPI
A Python library for interacting with the Skynet API. 

Skynet (https://skynet.unc.edu) is a global, robotic telescope network
used by tens-of-thousands of students and researchers.

The intent of this library is to provide an easy-to-use interface that
doesn't require any knowledge of how to interact with the API. No need
to understand the endpoints, methods, or handling responses. 

A request is as simple as:

```python
from skynetapi import ObservationRequest

obs = ObservationRequest(token='1234').get(obs_id=9999)

print(obs.id, obs.name)  # output: 9999, 'example-name'
```

## Documentation
For usage details, see: https://astrodyl.gitbook.io/astrodyl-docs/software-docs/skynetapi \
For API details, see: https://astrodyl.gitbook.io/astrodyl-docs/skynet-docs/api-endpoints

## Installation

### Using PIP
Activate your virtual environment and navigate to the root directory of this repo and
run:

```shell
pip install -e .
```

If successful, the last line of the output will say: `Successfully installed skynetapi`.
You can delete the repo after installation if you do not wish to make any modifications.

### From Source
To build from source, you will need the Python module `build`. Activate your virtual
environment and run:

```shell
pip install build
python -m build
```

This will create a Python wheel (`skynetapi/dist/skynetapi-0.1.0-py2.py3-none-any.whl`)
that can be installed using PIP.

```shell
pip install dist/skynetapi-0.1.0-py2.py3-none-any.whl
```

Note that there is already a Python wheel included with the repo in the `dist/` directory.