FROM python:3.11

WORKDIR /code

RUN pip install "poetry==1.5.1"

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root

COPY . .