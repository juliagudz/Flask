from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
    return 'Hello world'


@app.route('/api/v1/hello-world-5')
def ind():
    return 'Hello world 5'

if __name__=="__main__":
    app.run(debug=True)