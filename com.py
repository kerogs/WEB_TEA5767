# This program is used to send a message to the arduino (testing)

import os;

os.system('cls');

import serial
arduino = serial.Serial('COM3', 9600, timeout=0.1);

while True:
    msg_tx = input("message: ");
    arduino.write(b'{msg_tx}\n');
    
    msg_rx = arduino.readline();
    msg_rx = msg_rx.decode('utf-8');
    print(f"message: {msg_rx}\n");