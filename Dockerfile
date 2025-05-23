FROM bitnami/python:3.13.3

RUN mkdir hmgqls
RUN pip install gunicorn

COPY ./requirements.txt /hmgqls/requirements.txt
RUN pip install -r /hmgqls/requirements.txt

COPY . /hmgqls
WORKDIR /hmgqls

ENTRYPOINT [ "sh", "/hmgqls/entrypoint.sh" ]
