FROM python:3.7-slim

# install the packages
RUN pip install --no-cache --upgrade pip \
    && pip install --no-cache notebook pandas

# install db
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y sqlite3

# create user with a home directory
ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}

USER root
RUN chown -R ${NB_UID} ${HOME}
# copy all content to home directory and make the files owned by the created user
COPY . ${HOME}
USER ${NB_USER}

# create database for task_review
RUN cat Task_Review.sql | sqlite3 taskReviewDatabase.db

