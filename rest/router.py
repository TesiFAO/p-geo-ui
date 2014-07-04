from flask import Flask
from flask import render_template
from flask.ext.cors import cross_origin


app = Flask(__name__)


@app.route('/')
@cross_origin(origins='*')
def root():
    modis = render_template('modis.html')
    return render_template('index_bootstrap.html', main_content=modis)


if __name__ == '__main__':
    app.run(port = 5005, debug = True)