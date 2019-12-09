from flask import Flask

app=Flask(__name__)
#web app is created

#route number 1
@app.route('/')
def index():

    return "HELLO FLASK"

@app.route('/test')
def test():
    return "TEST PAGE"

app.run(debug=True)
