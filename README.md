# Frequency Data Transmitter

This is a proof of concept, to demonstrate the possibility of transmitting data from an Air Gapped computer via frequency. 

### How it works
A file can be serialized into frequencies (including those inaudible to human ears), and a microphone can pick it up and decode it. 

### Requirements
##### Operating System
Currently, this works on Windows. May port this into other Operating Systems in the future, but for now, it's a proof of concept.

##### Python
This script was written in Python 2.7.  It makes use of scipy, matplotlib, pyaudio, and numpy. 