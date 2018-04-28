CWD=$(shell pwd)
ENV=venv
MONITORING_STATE?=prometheus_multiproc_dir/

default: dev $(ENV)

$(ENV):
	virtualenv -p python3 $(ENV)
	$(ENV)/bin/pip install -r requirements.txt

clean:
	$(RM) -R $(ENV)
	make -C app/static clean

dev:
	make -C app/static dev

prod:
	make -C app/static prod

check:
	PYTHONPATH=$(CWD) $(ENV)/bin/python -m unittest discover app/

run: $(ENV) prod
	prometheus_multiproc_dir=$(MONITORING_STATE) $(ENV)/bin/gunicorn --chdir app api:app --log-level debug --pythonpath $(CWD)

image:
	docker build -t julienbalestra/vue-flask:latest .
