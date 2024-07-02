from flask import Flask, request, abort

app = Flask(__name__)
import time


@app.route('/api')
def hello_world():
    # read query parameter "crash"
    crash = request.args.get('crash')
    if crash == "false":
        # raise exception to crash the application
        return 'Hello World!'
    status = int(request.args.get('status'))
    abort(status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
