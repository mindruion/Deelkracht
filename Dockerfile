# pull official base image
FROM python:3.7-slim
# set work directory
WORKDIR /code

# install psycopg2 dependencies
RUN apt-get update \
  && apt-get -y --no-install-recommends install \
     gcc g++ curl gettext vim git g++ \
     # python depencies
     python3-dev python3-setuptools \
     # Pandas dependcies
     libblas3 libblas-dev liblapack3 liblapack-dev gfortran \
     # turicreate deps
     libgconf-2-4 \
     # Postgres
     libpq-dev libzbar-dev libmagic1\
     # Geoip Database
     libmaxminddb0 libmaxminddb-dev libsasl2-dev python-dev libldap2-dev libssl-dev libpoppler-cpp-dev\
  && apt-get clean


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /code/

RUN pip install psycopg2-binary
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn
RUN pip install python-magic==0.4.15
COPY . /code/
