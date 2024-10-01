FROM python:3.12

WORKDIR /project

ENV PYTHONPATH "${PYTHONPATH}:/project"

# Install Poetry skip virtual env in docker as unneeded
RUN pip install poetry==1.7 && \
    poetry config virtualenvs.create false

# Copy poetry.lock* so dependencies only get rebuilt if they are changed
COPY ./pyproject.toml ./poetry.lock* /project/

# Install dependencies
RUN poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
