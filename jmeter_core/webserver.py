from flask import Flask, render_template, abort , request, render_template_string
from jinja2 import TemplateNotFound
from flask import send_file


app = Flask(__name__, static_url_path='', static_folder="templates")

@app.route('/')
def render():
    return render_template_string(

'''<html>

<head>
    <title>Benchmarking</title>
</head>

<h1>Benchmarking</h1>

<body>
    <a href=" " onclick="javascript:event.target.port=3000"> Get real time results</a><br><br>
    <a href="/index.html">Get final results</a><br><br>
</body>

</html>''')

@app.route('/')
def root():
    return app.send_static_file('')

@app.route('/<page>')
def html_lookup(page):
    try:
        return render_template('{}'.format(page))
    except TemplateNotFound:
        abort(404)

@app.route('/content/pages/<page>')
def html_lookup_2(page):
    try:
        return render_template('/content/pages/{}'.format(page))
    except TemplateNotFound:
        abort(404)


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=4000)
