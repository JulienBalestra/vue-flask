# Vue-Flask

Quick web Dashboard / REST API with Prometheus monitoring



![preview](docs/preview.png)


## Stack

* Backend
    * Flask
    * Gunicorn

* Frontend
    * VueJS
    * Bootstrap


## Use

### Requirements

* npm
* python3
* virtualenv
* docker (optional)


#### Setup

    make
    
#### Testing
    
    
    make check
   
    
#### Gunicorn foreground
    
    
    make run
    

#### Build and run the docker container

    make image # optional
    docker run -it --rm julienbalestra/vue-flask:latest
    
#### Observe prometheus metrics

    curl http://${endpoint}/metrics
    
### Structure
    
    
    tree
    .
    |-- Dockerfile
    |-- Makefile
    |-- README.md
    |-- app
    |   |-- __init__.py
    |   |-- api.py
    |   |-- monitoring.py
    |   |-- static
    |   |   |-- Makefile
    |   |   |-- css
    |   |   |   `-- index.css
    |   |   |-- js
    |   |   |   `-- app.js
    |   |   |-- media
    |   |   |   |-- flask.png
    |   |   |   `-- vuejs.png
    |   |   `-- package.json
    |   |-- templates
    |   |   `-- index.html
    |   `-- tests
    |       |-- __init__.py
    |       `-- test_api.py
    |-- docs
    |   `-- preview.png
    `-- requirements.txt
    
    8 directories, 15 files
