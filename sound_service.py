import pyaudio
import wave
import sys
import pygame

CHUNK = 1024

class SoundService():
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.sound_dict = {}
        self.initializeWavFiles()

    def initializeWavFiles(self):
        self.sound_dict["808-clap.wav"] = SoundPackage(self.p, "808-clap.wav")
        self.sound_dict["elrdrum.wav"] = SoundPackage(self.p, "elrdrum.wav")
        self.sound_dict["snap.wav"] = SoundPackage(self.p, "snap.wav")
        self.sound_dict["beep-02.wav"] = SoundPackage(self.p, "beep-02.wav")
        self.sound_dict["beep-07.wav"] = SoundPackage(self.p, "beep-07.wav")


    #Needs to be able to handle playing multiple sounds at the same time
    #construct a wave file list
    #construct a data list
    #
    #@param sound_list - list<filename:String>
    def playSounds(self, sound_list):
        if sound_list == []:
            return
        wf_list = []
        sounds = len(sound_list)
        for filename in sound_list:
            wf = wave.open(filename, 'rb')
            data = wf.readframes(CHUNK)
            wf_list.append([self.sound_dict[filename].stream, wf, data])

        run = True
        while run:
            for item in wf_list:
                if item[2] != '':
                    item[0].write(item[2])
                    item[2] = item[1].readframes(CHUNK)
                else:
                    sounds -= 1
            if sounds == 0:
                run = False


class SoundPackage():
    def __init__(self,p_audio, filename):
        self.filename = filename
        self.wf = wave.open(self.filename, 'rb')

        self.stream = p_audio.open(format=p_audio.get_format_from_width(self.wf.getsampwidth()),
                                    channels=self.wf.getnchannels(),
                                    rate=self.wf.getframerate(),
                                    output=True)
    def play(self):
        self.wf = wave.open(self.filename, 'rb')

        data = self.wf.readframes(CHUNK)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(CHUNK)
        # stream.stop_stream()


# wf = wave.open("elrdrum.wav", 'rb')
# wf2 = wave.open("bird.wav", 'rb')


# p = pyaudio.PyAudio()

# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True)

# stream2 = p.open(format=p.get_format_from_width(wf2.getsampwidth()),
#                 channels=wf2.getnchannels(),
#                 rate=wf2.getframerate(),
#                 output=True)



# data = wf.readframes(CHUNK)
# data2 = wf2.readframes(CHUNK)

# pygame.time.delay(100)
# while data != '':
#     stream.write(data)
#     data = wf.readframes(CHUNK)
#     stream2.write(data2)
#     data2 = wf2.readframes(CHUNK)



# stream.stop_stream()
# stream.close()

# p.terminate()
