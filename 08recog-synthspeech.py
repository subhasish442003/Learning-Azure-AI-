#Enviroment (.env) file for Recognize and synthesize speech
SPEECH_KEY="7hovYdNPnGAdH7jhjOHs3DjyZrr2YXiZ36gLxDLLtMiBskcxGF9oJQQJ99AKACYeBjFXJ3w3AAAYxxxxxxx"
SPEECH_REGION="eastus"

#code for Recognize and synthesize speech
from dotenv import load_dotenv
from datetime import datetime
from playsound import playsound
import os
import azure.cognitiveservices.speech as speech_sdk  # Import namespaces

def main():
    try:
        global speech_config
        
        # Load configuration settings
        load_dotenv()
        ai_key = os.getenv('SPEECH_KEY')
        ai_region = os.getenv('SPEECH_REGION')
        
        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(subscription=ai_key, region=ai_region)
        print('Ready to use speech service in:', speech_config.region)
        
        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()
    except Exception as ex:
        print(f"Error: {ex}")

def TranscribeCommand():
    command = ''
    try:
        # Configure speech recognition with default microphone
        audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
        speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        print('Speak now...')
        
        # Play audio prompt (optional)
        current_dir = os.getcwd()
        audio_file = os.path.join(current_dir, 'time.wav')
        playsound(audio_file)
        
        # Process speech input from file
        audio_config = speech_sdk.AudioConfig(filename=audio_file)
        speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        speech = speech_recognizer.recognize_once_async().get()
        
        if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
            command = speech.text
            print(f"Recognized command: {command}")
        else:
            print(f"Recognition failed: {speech.reason}")
            if speech.reason == speech_sdk.ResultReason.Canceled:
                cancellation = speech.cancellation_details
                print(f"Cancellation reason: {cancellation.reason}")
                print(f"Error details: {cancellation.error_details}")
    except Exception as ex:
        print(f"Error during transcription: {ex}")
    
    # Return the command
    return command

def TellTime():
    try:
        now = datetime.now()
        response_text = 'The time is {}:{:02d}'.format(now.hour, now.minute)
        
        # Configure speech synthesis
        speech_config.speech_synthesis_voice_name = 'en-GB-LibbyNeural'  # Example voice
        speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config=speech_config)
        
        # Create SSML response
        response_ssml = (
            "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>"
            f"<voice name='en-GB-LibbyNeural'>"
            f"{response_text}<break strength='weak'/>Time to end this lab!"
            "</voice></speak>"
        )
        
        # Synthesize SSML output
        ssml_speak = speech_synthesizer.speak_ssml_async(response_ssml).get()
        if ssml_speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
            print(f"SSML synthesis failed: {ssml_speak.reason}")
        
        # Synthesize text output
        text_speak = speech_synthesizer.speak_text_async(response_text).get()
        if text_speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
            print(f"Text synthesis failed: {text_speak.reason}")
        
        # Print the response
        print(response_text)
    except Exception as ex:
        print(f"Error during time announcement: {ex}")

if __name__ == "__main__":
    main()

