import pyaudio
import wave
import sys
import pygame

CHUNK = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

print sys.argv[1]

wf = wave.open("beep-07.wav", 'rb')
wf2 = wave.open("beep-02.wav",'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

stream2 = p.open(format=p.get_format_from_width(wf2.getsampwidth()),
                channels=wf2.getnchannels(),
                rate=wf2.getframerate(),
                output=True)

data = wf.readframes(CHUNK)
data2 = wf2.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)
    stream2.write(data2)
    data2 = wf2.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()
