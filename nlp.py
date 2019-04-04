import speech_recognition as sr
from get_data import download_file

#download_file
if download_file('data', 'audio') == False:
	print("Exiting with error")
	exit()

print("file downloaded successfully")

#instantiate the recognizer
r = sr.Recognizer()

#open the audio file/ or input fro mthe microphone


harvard = sr.AudioFile('sample.wav')
print('listening')
with harvard as source:
	#removing noise, set duration to set the  base signal to nulify effect
	r.adjust_for_ambient_noise(source, duration=0.5)
	audio = r.record(source)

#recognize using google web api
data = (r.recognize_google(audio))
dat = data.split()
print(dat)
for x in ['shoot', 'go', 'throw']:
	if x in dat:
		print('shooting')
		break

for y in ['red', 'green', 'blue']:
	if y in dat:
		print('{} {}'.format(x,y))
		break


