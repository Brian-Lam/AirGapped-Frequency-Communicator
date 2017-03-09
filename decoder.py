from matplotlib.mlab import find
import pyaudio
import numpy as np
import math

from airgap import FREQUENCY_STEP, PREAMBLE_FREQUENCY

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 300
ROLLING_AVERAGE_WINDOW = 3

# CREDIT: http://stackoverflow.com/questions/9082431/frequency-analysis-in-python
# find_frequency in audio stream code
# Much love. <3 

def find_frequency(signal):
    signal = np.fromstring(signal, 'Int16');
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing));
    f0=round(len(index) *RATE /(2*np.prod(len(signal))))
    return f0;

p = pyaudio.PyAudio()

# Open Audio Stream
stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK)

stream_length = RATE / CHUNK

# Initiate rolling average table
frequencies_avg = [0] * ROLLING_AVERAGE_WINDOW

# Initiate preamble count
preambles_detected = 0
recording_started = False

print "Listening for preamble"

# BRIAN-LAM: Code below needs heavy refactoring
for i in range(1, stream_length * RECORD_SECONDS):
    # Read from microphone stream
    data = stream.read(CHUNK)
    frequency = find_frequency(data)

    # Add to rolling average table
    frequencies_avg[i % ROLLING_AVERAGE_WINDOW] = frequency

    if (i % stream_length == 0):
        # Only run this once a second
        # BRIAN-LAM: Lol make sure this actually only runs once a second 
        # and this isn't machine specific
        average_frequency = sum(frequencies_avg)/len(frequencies_avg)

        # Round average frequency to nearest frequency
        offset = ((average_frequency + (FREQUENCY_STEP / 2)) % FREQUENCY_STEP)
        rounded_frequency = (average_frequency - offset + (FREQUENCY_STEP/2))

        print rounded_frequency

        # Reset preamble count if this isn't a preamble
        if rounded_frequency != PREAMBLE_FREQUENCY:
            preambles_detected = 0

        # Check for Preamble
        if (preambles_detected != 3):
            if rounded_frequency == PREAMBLE_FREQUENCY:
                preambles_detected += 1
                if (preambles_detected == 3):
                    # Start recording data when three preamble beeps have been detected
                    print "Preamble detected"
                    if recording_started:
                        print "Finished."
                        exit
                    if not recording_started:
                        recording_started = True
                        preambles_detected = 0
        


