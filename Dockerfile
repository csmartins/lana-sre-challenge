FROM python:3

WORKDIR /app/
COPY Pipfile* /app/
RUN pip3 install pipenv
RUN pipenv install

ADD basket_api /app/basket_api

ENTRYPOINT pipenv run gunicorn --bind 0.0.0.0:5000 basket_api.api:app