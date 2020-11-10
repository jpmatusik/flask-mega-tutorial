FROM python:3.8.6-slim as base

ENV PYTHONUNBUFFERED=1 \
    PROJECT_DIR=/app \
    POETRY_VERSION=1.1.4 \
    POETRY_HOME=/opt/poetry \
    VIRTUAL_ENV=/opt/venv \
    DEBIAN_FRONTEND=noninteractive \
    TINI_VERSION=v0.19.0

# uses TINI_VERSION
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/local/bin/tini
COPY docker/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh && \
    chmod +x /usr/local/bin/tini


FROM base as builder

ENV PATH "$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get upgrade -y && apt-get install --no-install-recommends -y curl
# uses POETRY_VERSION and POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --no-modify-path

RUN python -m venv $VIRTUAL_ENV

WORKDIR $PROJECT_DIR
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-root


FROM base as development

ENV PATH "$POETRY_HOME/bin:$PATH"

COPY --from=builder $PROJECT_DIR $PROJECT_DIR
COPY --from=builder $POETRY_HOME $POETRY_HOME
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

WORKDIR $PROJECT_DIR
RUN poetry install --no-root

COPY . .

EXPOSE 5000

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["flask", "run", "-h", "0.0.0.0"]
