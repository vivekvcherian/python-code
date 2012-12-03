#! /usr/bin/python

import math
signal_power = 20 # Signal Power #
noise_power = 10 # Noise Power #
ratio = signal_power/ noise_power
decibels = 10 * math.log10(ratio)
print decibels
