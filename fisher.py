from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 200)
    response.headers = headers
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=3003)
