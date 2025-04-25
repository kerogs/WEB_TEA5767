# Web interface for TEA5767 radio module

This is a simple web interface to control and read informations from a TEA5767 radio module connected to an Arduino board.

## Features

* Change the frequency of the radio
* Read informations about the radio (frequency, RSSI, PLL, stereo flag, and raw data in hexadecimal)
* Update the informations in real time

## How to use

1. Connect your Arduino board to your computer
2. Upload the `webcode` sketch to your Arduino board
3. Open a web browser and go to `http://localhost:5000`
4. You will see the web interface with the informations about the radio
5. You can change the frequency of the radio by clicking on the "Change" button and entering the new frequency
6. The informations about the radio will be updated in real time

## Requirements

* An Arduino board (e.g. Arduino Uno)
* A TEA5767 radio module
* A breadboard and some jumper wires
* A computer with a web browser
* The Arduino IDE

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
