FROM python:3.8.6-slim as base

ENV PYTHONUNBUFFERED=1 \
    PROJECT_DIR=/flask_mega_tutorial \
    POETRY_VERSION=1.1.4 \
    POETRY_HOME=/opt/poetry \
    VIRTUAL_ENV=/opt/venv \
    DEBIAN_FRONTEND=noninteractive \
    TINI_VERSION=v0.19.0

# uses TINI_VERSION
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini

FROM base as builder

ENV PATH "$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential libpq-dev
# uses POETRY_VERSION and POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --no-modify-path

RUN python -m venv $VIRTUAL_ENV

WORKDIR $PROJECT_DIR
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-root


FROM base as development

ENV FLASK_ENV development
ENV PATH "$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y libpq5

COPY --from=builder $PROJECT_DIR $PROJECT_DIR
COPY --from=builder $POETRY_HOME $POETRY_HOME
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

WORKDIR $PROJECT_DIR
RUN poetry install --no-root

COPY docker/app-entrypoint.sh /usr/local/bin/app-entrypoint.sh
COPY docker/migration-entrypoint.sh /usr/local/bin/migration-entrypoint.sh
RUN chmod +x /usr/local/bin/app-entrypoint.sh && \
    chmod +x /usr/local/bin/migration-entrypoint.sh

COPY . .

ENTRYPOINT ["app-entrypoint.sh"]
CMD ["flask", "run", "-h", "0.0.0.0"]


FROM base as production

ENV FLASK_ENV production

RUN apt-get update && apt-get install --no-install-recommends -y libpq5

COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV
COPY flask_mega_tutorial $PROJECT_DIR

COPY docker/app-entrypoint.sh /usr/local/bin/app-entrypoint.sh
RUN chmod +x /usr/local/bin/app-entrypoint.sh
WORKDIR /
ENTRYPOINT ["app-entrypoint.sh"]
CMD ["flask", "run", "-h", "0.0.0.0"]
