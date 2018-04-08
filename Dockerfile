FROM python:3.6-stretch
MAINTAINER Sylvestre <sylvestre.gug@gmail.com>

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN \
  apt-get clean && \
  apt-get -q update && \
  apt-get install -y build-essential nodejs

RUN pip install pipenv

ENV SRC_DIR /usr/src

COPY Pipfile Pipfile.lock ${SRC_DIR}/

WORKDIR ${SRC_DIR}

ENV PYTHONUNBUFFERED 1
ENV PATH $PATH:/usr/src/app/node_modules/.bin
RUN node -v
RUN npm -v

RUN npm install -g yarn
RUN which yarn

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN pipenv install --system && rm -rf /root/.cache/pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./ /usr/src/app/

RUN useradd wagtail
RUN chown -R wagtail /usr/src/app/
USER wagtail

EXPOSE 8000
CMD exec gunicorn alsace.wsgi:application --bind 0.0.0.0:8000 --workers 3
