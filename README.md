# Docker for ElasticSearch and Flask Data Retreival

This project is to Demo 2 Docker Containers, which work together

  - es. An ElasticSearch container. Which saves the data on a Volume.
  - py. A python3 Flask App that presents a Web Page and searches the Elastic Search data


# Requirements

  - Docker
  - Some Markdown files (Only format supported at the moment)

## Installing

Initially you just need to pull this project from git

### Building

Use the command

   docker-compose up --build

And that should be it !!


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
