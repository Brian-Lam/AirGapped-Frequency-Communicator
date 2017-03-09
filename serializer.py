import winsound

DEBUG = True

PREAMBLE_FREQUENCY = 3000
BASE_FREQUENCY = 4000
FREQUENCY_STEP = 500

def playPreamble():
    for i in range(3):
        winsound.Beep(PREAMBLE_FREQUENCY, 1000)

def hexFrequency(hexValue):
    """ Calculate a hex frequency for a hex's int value """
    return BASE_FREQUENCY + hexValue * FREQUENCY_STEP

def processCharacter(hexChar):
    """ Process a hex character """
    hexValue = int(hexChar, 16)
    frequency = hexFrequency(hexValue)
    winsound.Beep(frequency, 1000)
    if DEBUG:
        print(hexChar + ": " + str(frequency))

def processByte(byte):
    """ Convert the byte into two hex characters """
    byteHex = byte.encode('hex') # Will encode to two character hex string
    processCharacter(byteHex[0])
    processCharacter(byteHex[1])

def readFile(url):
    """ Read file byte by byte """
    targetFile = open(url, "rb")
    try:
        byte = targetFile.read(1)
        while byte != "":
            processByte(byte)
            byte = targetFile.read(1)
    finally:
        targetFile.close()

if __name__ == "__main__":
    playPreamble()
    readFile("data.txt")
    playPreamble()
