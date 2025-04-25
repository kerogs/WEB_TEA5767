import serial
import time, json
from flask import Flask, render_template, request

app = Flask(__name__)

# COM configuration
arduino_port = "COM3"  # Change with arduino port
baud_rate = 9600 # change with arduino baud rate

@app.route('/')
def index():
    """
    Send the index.html template to the user

    This function renders the index.html template and send it to the
    user. The user will see the web interface of the radio.

    :return: The rendered index.html template
    """
    return render_template('index.html')

@app.route('/data')
def get_data():
    """
    Get data from arduino.

    This function send a request to the arduino (by sending "1"),
    and then return the response as a string.

    The response is a JSON formatted string, containing the
    PLL, RSSI, RSSIdBm, stereo, hex and ASCII informations

    :return: The JSON formatted string containing the informations
    """
    arduino = serial.Serial(arduino_port, baud_rate)
    
    # Send "1" to arduino (request data)
    arduino.write(b'1') 
    
    msg_rx = arduino.readline();
    msg_rx = msg_rx.decode('utf-8');
    
    print(msg_rx)
    
    return "{}".format(msg_rx)
    
@app.route('/frequency', methods=['POST'])
def set_frequency():
    # GET VALUE FROM FORM
    """
    Send the frequency from the form to the arduino.

    :param request.form['frequency']: The frequency to send to the arduino
    :return: The rendered index.html template
    """
    frequency = float(request.form['frequency'])
    
    # Send frequency to arduino
    arduino = serial.Serial(arduino_port, baud_rate)
    arduino.write(b"" + str(frequency).encode('utf-8'))
    arduino.close()
    
    # Redirect to index page
    return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
