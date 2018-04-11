FROM node:latest as builder

COPY . /usr/local/vue-flask

RUN git -C /usr/local/vue-flask clean -fdx  && make -C /usr/local/vue-flask/ prod

FROM python:3

COPY --from=builder /usr/local/vue-flask /usr/local/vue-flask

ENV prometheus_multiproc_dir /var/lib/prometheus

RUN pip install -r /usr/local/vue-flask/requirements.txt && \
    mkdir -pv ${prometheus_multiproc_dir}

CMD gunicorn --chdir /usr/local/vue-flask/app api:app \
    --log-level info --pythonpath /usr/local/vue-flask \
    --workers 3 --bind 0.0.0.0:80
