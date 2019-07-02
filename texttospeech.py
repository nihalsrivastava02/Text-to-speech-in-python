#sudo apt-get -y install python3-pip  --> Install pip
#pip3 install gTTS -- > to install Google Text to Speech 
#sudo pip3 install playsound -->  for playing audio


import gtts
from playsound import playsound

def play_audio(path_of_audio):
	playsound(path_of_audio)

def convert_to_audio(text):
	tts = gtts.tts.gTTS(text, lang='en')
	tts.save("test.mp3")
	play_audio('test.mp3')

def main():
	f=open("test.txt","r")
	if f.mode == 'r':
		contents = f.read()
		convert_to_audio(contents)
main()
