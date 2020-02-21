#import sounddevice as sd
#import numpy as np
#import scipy.io.wavfile as wav

#fs=44100
#duration = 5  # seconds
#myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
#print ("Recording Audio")
#sd.wait()
#print ("Audio recording complete , Play Audio")
#sd.play(myrecording, fs)
#sd.wait()
#print ("Play Audio Complete")
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

print('Recording...')
with mic as source:
    audio = r.listen(source)

with open("audio_file.wav", "wb") as file:
    file.write(audio.get_wav_data)