FROM python:3

ADD basket_api /app/basket_api
COPY Pipfile* /app/
COPY entrypoint.sh /app/

WORKDIR /app/

RUN pip3 install pipenv
RUN pipenv install
ENTRYPOINT pipenv run gunicorn --bind 0.0.0.0:5000 basket_api.api:app