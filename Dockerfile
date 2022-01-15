FROM bitnami/python:3.8

RUN mkdir hmgqls

COPY . /hmgqls
WORKDIR /hmgqls

RUN pip install gunicorn
RUN pip install -r requirements.txt
#CMD ["gunicorn", "-w 4", "server:app"]
CMD gunicorn -b 0.0.0.0:8191 -w 2 --threads 2 server:app

