from flask import Flask, request, redirect, url_for, send_from_directory, render_template

app = Flask(__name__)
app.debug = True


# Routes
@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')


@app.route('/<path:path>')
def static_prox(path):
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run()
    # app.run(host="0.0.0.0", port=80, threaded=True)
