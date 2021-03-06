from elasticsearch import Elasticsearch
import json
from glob import glob


def file_to_str(filename):
    with open(filename, "rt",encoding='utf-8',errors='ignore') as source:
        lines = "".join(source.readlines())
    return lines


es = Elasticsearch([{"host": "0.0.0.0", "port": 9200}])

IDX = 'mydocs'
TYPE = 'markdown'


def load(location):
    tot = 0
    try:
        res = es.count(index=IDX)
        tot = res['count']
        print("We have {} Records already ".format(tot))

    except Exception as err:
        print("Index does not exist")
        es.indices.create(index=IDX, ignore=400)
        tot = 0

    for file in glob(location,recursive=True):
        print("" + file)
        lines = file_to_str(file)
        doc = {}
        doc['text'] = lines

        try:
            es.index(index=IDX, doc_type=TYPE, id=tot, body=json.dumps(doc, ensure_ascii=False))
            print("Loaded Document {}".format(tot))
            tot = tot + 1
        except Exception as err:
            print("Error {} deteced doc not loaded".format(str(err)))

def check():
    # count the matches
    count = es.count(index=IDX, doc_type=TYPE, body={"query": {"match_all": {}}})
    print("We have {} documents".format(count))

def search():
    # now we can do searches.
    count = es.count(index=IDX, doc_type=TYPE, body={"query": {"match_all": {}}})
    print("Ok. I've got an index of {0} documents. Let's do some searches...".format(count['count']))
    while True:
        try:
            query = input("Enter a search: ")
            result = es.search(index=IDX, doc_type=TYPE, body={"query": {"match": {"text": query.strip()}}})
            if result.get('hits') is not None and result['hits'].get('hits') is not None:
                print(result['hits']['hits'])
            else:
                print({})
        except(KeyboardInterrupt):
            break

#search()
try:
  print("Please Enter the file spec of the Markdown files to Index")
  print("i.e. /User/tim/Public/*")
  location=input("File Specification ")
  load(location)
except(KeyboardInterrupt):
  pass
print("\n\n\n")
print("Open a Web Browser to http://0.0.0.0.0:5000 to Start Searching")
