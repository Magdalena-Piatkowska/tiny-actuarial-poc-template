# Requirements

This project requires installed on your OS:

- docker
- makefile command
- python 3.12 (if running directly on local machine)


# Initial setup

### Using Docker:
1. Run command ```make build``` to build the project image
2. Run command ```make up``` to start the Docker container

### Directly on local machine:
1. Create a virtual environment
2. Activate the virtual environment
3. Run command ```pip install poetry``` to install the Poetry package manager
4. Run command ```poetry install``` to install dependencies using Poetry
5. Run command ```make dev``` to run the project directly on local machine


# How to run the project

### Using Docker:
- Run command ```make up``` to start the Docker container

### Directly on local machine:
- Run command ```make dev``` to run the project directly on local machine


# Other useful commands
- Run command ```make test``` to execute all existing tests
- Run command ```make format``` to format the code using black
- Run command ```make check``` to perform type checking using mypy


# TO-DO

- finish setting up README.md
- add infra
- add pipelines