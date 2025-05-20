FROM ubuntu:noble

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        git \
        git-lfs \
        ssh \
        sudo \
        unzip \
        wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN adduser ubuntu sudo

RUN mkdir -p /project/tgm4-konoha-hololive && chown -R ubuntu:ubuntu /project

COPY --from=ghcr.io/astral-sh/uv:0.7.4 /uv /uvx /bin/
ENV UV_PROJECT_ENVIRONMENT /project/.venv

USER ubuntu
WORKDIR /project/tgm4-konoha-hololive

ADD pyproject.toml uv.lock /project/tgm4-konoha-hololive

RUN uv sync --locked

ENV PATH="/project/.venv/bin:$PATH"