from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/humidity/<seconds>', methods=['GET'])
@app.route('/humidity/', defaults={'seconds': 4})
def hello_world(seconds=4):
     # call sensor method
    print(seconds)
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
