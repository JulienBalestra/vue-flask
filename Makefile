CWD=$(shell pwd)
ENV=$(CWD)/env

default: dev $(ENV)

$(ENV):
	virtualenv -p python3 $(ENV)
	$(ENV)/bin/pip install -r requirements.txt


clean:
	rm -Rf $(ENV) || true
	make -C app/static clean

dev:
	make -C app/static dev

prod:
	make -C app/static prod


check:
	PYTHONPATH=$(CWD) $(ENV)/bin/python -m unittest discover app/

run: $(ENV) prod
	$(ENV)/bin/gunicorn --chdir app api:app --log-level debug