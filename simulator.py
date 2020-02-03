audioSourceFile = ""
audioSourceFile = open(audioSourceFile, 'rb', 0)

audioDestinationFile = ""
audioDestinationFile=open(audioDestinationFile, 'wb+', 0)

#bytes
packetSize = 50


threshold = 0.5

#bytes
sampleSize = 1

def store(packet):
    audioDestinationFile.write(packet)
    return packet,packet[-sampleSize:]


def alternateStore(lastSample,lastPacket):
    mode = ''

    if mode == 'sample':
        writeData = ''
        while len(writeData) <= packetSize:
            writeData += lastSample
        writeData = writeData[:packetSize]

        audioDestinationFile.write(writeData)

    else:
        if mode == 'packet':
            audioDestinationFile
        else:
            audioDestinationFile.write(b'0' * packetSize)


def calculateProbability():
    from random import seed
    from random import random

    # seed random number generator
    seed(1)
    # generate random numbers between 0-1
    random()


while (True):

    packet = audioSourceFile.read(packetSize)
    if calculateProbability() < threshold:
        lastPacket,lastSample = store()






# open_audio_source_file();
# open_audio_dest_file();
# while not EOF {
# read_sample(); /* Read audio sample from a file */ loss = calculate_loss_probability(); /* P acket loss or jitter probabiliy */
# i f (loss < threshold) {
# store_sample();   /* Store the received sample */
# }
# else
# store_alternate_data(); / * See details for alternatives */
