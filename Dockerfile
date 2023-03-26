FROM python:3.10-slim-buster

# Install system dependencies
RUN apt-get update
RUN apt-get -y install --no-install-recommends git gcc make libpq-dev python3-dev
RUN rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

# Change working directory
WORKDIR /app

# Install python dependecies
ADD ./requirements.txt /app
ADD ./requirements /app/requirements

RUN pip install --no-cache-dir --timeout=180 -r requirements.txt

ADD . /app/
ENTRYPOINT ["make", "-f", "/app/Makefile"]
CMD ["run-server"]
