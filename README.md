# Docker for ElasticSearch and Flask Data Retreival

This project is to Demo 2 Docker Containers, which work together

  - es. An ElasticSearch container. Which saves the data on a Volume.
  - py. A python3 Flask App that presents a Web Page and searches the Elastic Search data

This is one of the first multi-container projects I have created, an interesting and informative way to play with Docker at home.

## Purpose

I have a large collection of Markdown documents, in fact I am now finding a slight issues in tracking down some items I know are in the documents.

What I need is a search Engine ... Oh .... Elasticsearch that will do nicely.

But I do not like reading JSON output (even using jq), I would like some nice HTML output - usually I would use CherryPy, but recently I am exploring like with Python-Flask.

## Design

I have Purposefully created 2 containers, one for the ElasticSearch the other to handle the Flask.

To manage the orchestration for building and running, I am wrapping the Dockerfile's with Docker-Compose; 

# Requirements

  - Docker
  - Some Markdown files (Only format supported at the moment)

## Installing

Initially you just need to pull this project from git

### Building

Use the command

    docker-compose up --build

And that should be it !!

### Stopping

You can either stop each individual container or use docker-compose

    docker-compose down

### Detached Mode

When you are happy that the process is working well, there is probably no need to look at the screen. So run the processes with *detached* mode.

    docker-composer up -d

# Adding some Data

Obviously the container(s) need to be running, so assuming they are - on the host machine you will need to run the **LoadData.py** script. This has a few requirements

These requirements can be met using

   pip install --upgrade flask wtforms elasticsearch markdown

Now we can run the **LoadData.py** script.

## LoadData.py

When you enter a filespec please use a full path, not ~/ - and add the woldcard of the filespec you want to add.

# Querying

Open a WebBrowser to http://0.0.0.0:5000

Enter the text, and press query.
