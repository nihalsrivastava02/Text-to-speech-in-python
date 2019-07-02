# pip install --upgrade google-cloud-texttospeech
#export GOOGLE_APPLICATION_CREDENTIALS="/home/hunt/Desktop/ibm/My First Project-36af9935ca3b.json" 		--> set path before running 



import os  
from google.cloud import texttospeech
from playsound import playsound

def setpath():
	credential_path = "/home/hunt/Desktop/ibm/My First Project-36af9935ca3b.json"
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
def text2speech():
	client = texttospeech.TextToSpeechClient()
	filetoread=open("test.txt","r")
	if filetoread.mode == 'r':
	    var = filetoread.read()
	    synthesis_input = texttospeech.types.SynthesisInput(text=var)

	voice = texttospeech.types.VoiceSelectionParams(
	    language_code='en-US',
	    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

	audio_config = texttospeech.types.AudioConfig(
	    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

	response = client.synthesize_speech(synthesis_input, voice, audio_config)

	with open('output.mp3', 'wb') as out:
	    
	    out.write(response.audio_content)
	playsound('output.mp3')

def main():
	setpath()
	print('Audio content pushed to "output.mp3"')
	print("Listen Carefully.......")
	text2speech()
	

main()

