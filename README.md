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

    git pull https://github.com/timseed/Do_ES_Fl.git
    cd Do_ES_Fl
    docker-compose up --build -d

And thats it :)

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


## From a Client in a traditional manner.

Obviously the container(s) need to be running, so assuming they are - on the host machine you will need to run the **LoadData.py** script. This has a few requirements

These requirements can be met using

   pip install --upgrade flask wtforms elasticsearch markdown

Now we can run the **LoadData.py** script.

### LoadData.py

When you enter a filespec please use a full path, **not ~/** - and add the wildcard of the filespec you want to add.

## Using a the ADD REST API

The flask project has an *add* API point, which is
To "Push" a document into the Index you need to do This
```bash
curl -H "Content-type: application/octet-stream" \
     -X POST http://127.0.0.1:5000/add \
    --data-binary @file_to_load
```
Should you want to push lots of documents then a small script like this would work well on a Linux host

```bash
find $PATH_TO_SEARCH -name *.md | xargs -i -t \
     curl -H "Content-type: application/octet-stream" \
     -X POST http://127.0.0.1:5000/add \
      --data-binary @{}
```

On a mac the Xargs command is a little different becoming

```bash
find $PATH_TO_SEARCH -name *.md | xargs -I {} -t \
     curl -H "Content-type: application/octet-stream" \
     -X POST http://127.0.0.1:5000/add \
     --data-binary @{}
```


# Querying

Open a WebBrowser to http://0.0.0.0:5000

Enter the text, and press query.

# Help

There is some help available via the Flask Web server at http://0.0.0.0.0:5000/
