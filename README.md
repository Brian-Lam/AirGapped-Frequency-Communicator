# Frequency Data Transmitter

This is a proof of concept, to demonstrate the possibility of transmitting data from an Air Gapped computer via frequency. 

### Background 

Air gapped computers are computers that are isolated from the public internet, either directly or through connections to other computers. This is done to protect high value information and to prevent it from leaving the system. There are a few experiments that have been done to extract data from an air gapped computer - I tried this as an experiment and a proof of concept. 

### How it works
A file is made up of a series of bits (0s and 1s). These bits can be serialized into frequencies (including those inaudible to human ears), and a microphone can pick it up and decode it - thus transmitting data via sound. 

### Functionality
This works, although not terribly well. If you plan on forking this repo, please don't do anything illegal, weird, or crazy with it. Thanks. 

### Requirements
##### Operating System
Currently, this works on Windows. May port this into other Operating Systems in the future, but for now, it's a proof of concept.

##### Python
This script was written in Python 2.7.  It makes use of scipy, matplotlib, pyaudio, and numpy. 
