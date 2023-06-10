# Control Arduino nano or nrf24 using Keyboard
import pyfirmata
import socket
import keyboard
import serial

HOST = ""    # Replace with the IP address of your Arduino e.g. 192.168.1.100
PORT = ""   # Replace with the port Number used in the Arduino sketch (Transmission) e.g.12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Set up the serial communication
ser = serial.Serial('COM3',9600) # Replace with the serial Communication ort of coded Arduino

# Define the commands to send to the Arduino
COMMAND_FORWARD = "W"
COMMAND_BACKWARD = "S"
COMMAND_LEFT = "A"
COMMAND_RIGHT = "D"

# Define the keyboard shortcuts to send the commands
keyboard.add_hotkey('up', lambda:s.sendall(COMMAND_FORWARD.encode()))
keyboard.add_hotkey('down', lambda:s.sendall(COMMAND_BACKWARD.endcode)))
keyboard.add_hotkey('left', lambda:s.sendall(COMMAND_LEFT.endcode)))
keyboard.add_hotkey('right', lambda:s.sendall(COMMAND_RIGHT.encode)))

# Wait for the keyboard input
keyboard.wait()
