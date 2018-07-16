from flask import Flask, render_template, flash, request
from flask import Markup
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_table import Table, Col
from elasticsearch import Elasticsearch
import markdown
import json
from glob import glob

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = StringField('Name:', validators=[validators.required()])

class esq(object):
    def __init__(self,node="0.0.0.0",port=9200):
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


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    e=esq("0.0.0.0",9200)
    res={}
    if request.method == 'POST':
        name = request.form['name']

        if form.validate():
            res=e.search(name)
            ## Save the comment here.
            #flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')

    return render_template('hello.html', form=form,dates=res)


if __name__ == '__main__':
    app.run()
