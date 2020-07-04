from flask import Flask, render_template
from sensor_stuff import sensor

app = Flask(__name__)


@app.route('/humidity/<port>/<seconds>', methods=['GET'])
@app.route('/humidity/', defaults={'seconds': 4, 'port': 'COM4'})
def request_to_arduino(seconds, port):
    # todo send request via serial port and wait for it and then wait for it
    data = sensor.processRequest(port, seconds)
    return render_template('main.html', seconds=seconds, data=data)


if __name__ == '__main__':
    app.run()
