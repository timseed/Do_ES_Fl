from flask import Flask, render_template, flash, request, Markup
from flask import jsonify
from wtforms import Form, validators, StringField
from elasticsearch import Elasticsearch
import markdown
import json

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = StringField('Name:', validators=[validators.required()])


class esq(object):

    def __init__(self,node="es_doc",port=9200):
        self.es=Elasticsearch([{"host": node, "port": port}])
        self.IDX = 'mydocs'
        self.TYPE = 'markdown'

    def search(self,text_value=""):
        # now we can do searches.
        rv={}
        if len(text_value)>0:
            try:

                result = self.es.search(index=self.IDX,
                                        doc_type=self.TYPE,
                                        body={"query": {"match": {"text": text_value.strip()}}})
                if result.get('hits') is not None and result['hits'].get('hits') is not None:
                    for h in result['hits']['hits']:
                        #Convert from Markdown to HTML
                        content = Markup(markdown.markdown(h["_source"]['text']))
                        rv[h['_id']]=content
                else:
                    flash("None")
            except Exception as err:
                flash("Err {}".format(str(err)))
            return rv

    def count(self):
        try:
            cnt = self.es.count(index=self.IDX,
                              doc_type=self.TYPE,
                              body={"query": {"match_all": {}}})
            return cnt["count"]

        except Exception as err:
            print("Index does not exist")
            self.es.indices.create(index=self.IDX, ignore=400)
            tot = 0



@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    res={}
    if request.method == 'POST':
        name = request.form['name']
        e=esq(node="es_doc",port=9200)
        if form.validate():
            res=e.search(name)
            ## Save the comment here.
            #flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')

    return render_template('hello.html', form=form,dates=res)


@app.route('/delete')
def delete():
    e = esq("es_doc", 9200)
    e.es.indices.delete(index=e.IDX, ignore=[400, 404])
    return 'Index {} deleted'.format(e.IDX)


#curl -H "Content-type: application/octet-stream" \
#-X POST http://127.0.0.1:5000/messages --data-binary @file_to_load

@app.route('/add', methods=['POST'])
def add():
    if request.headers['Content-Type'] == 'text/plain':
        e = esq("es_doc", 9200)
        tot = e.count()
        doc = {}
        doc['text'] = request.data.decode('utf-8')

        try:

            res=e.es.index(index=e.IDX, doc_type=e.TYPE, id=tot, body=json.dumps(doc, ensure_ascii=False))
            print("Loaded Document {}".format(tot))
            tot = tot + 1
            return jsonify(id=tot,status=200)

        except Exception as err:
            flash(str(err))

    else:
        return "415 Unsupported Media Type ;)"

@app.route('/help')
def help():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
