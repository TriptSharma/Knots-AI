import speech_recognition as sr

FILENAME = "audio_file.wav"

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print('Recording...')
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    # if keyboard.is_pressed('enter'):
    #     print('Recording Complete')
        # break
    print('Stopped')

with open(FILENAME, "wb") as file:
    print('Saving Audio...')
    file.write(audio.get_wav_data())

print('Done')