from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Test"

if __name__ == '__main__':
    # app.run()

    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)