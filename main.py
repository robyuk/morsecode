#! /usr/bin/python

# This program for a Raspberry Pi, accepts a text message as input,
# then outputs the text in morse code on GPIO ledPin.
# Enter ### to cleanup and end the program

import RPi.GPIO as GPIO
import time

# A tick is one unit, the smaller this number, the quicker the morse code will be
tick=0.1
tickx3=tick*3
tickx7=tick*7

# Connect a LED or active buzzer in series with a 220R resistor to ground on ledPin
ledPin=17

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)


def dot():
        GPIO.output(ledPin,1)
        time.sleep(tick)       # Length of dot is one unit
        GPIO.output(ledPin,0)
        time.sleep(tick)       # The space between parts of a letter is one unit

def dash():
        GPIO.output(ledPin,1)
        time.sleep(tickx3)       # Length of dash is three units
        GPIO.output(ledPin,0)
        time.sleep(tick)


while True:
        input = raw_input('What would you like to send? ')
        for letter in input:
                if letter.upper() in CODE:
                        for symbol in CODE[letter.upper()]:
                                if symbol == '-':
                                        dash()
                                elif symbol == '.':
                                        dot()
                                else:
                                        time.sleep(tickx7) # Space between words, seven units
                        time.sleep(tickx3) # Space between letters is three units
                elif input == '###':
                        GPIO.setup(ledPin,GPIO.IN)
                        exit()
