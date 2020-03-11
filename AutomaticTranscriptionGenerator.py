#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:33:47 2019

@author: ananya
"""
import speech_recognition as sr 
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence 

def splitOnPause(wavefile):
    newAudio = AudioSegment.from_wav(wavefile)
    outputFile = wavefile + '_Transcribed.txt' 
    f = open(outputFile, "w+")
    chunks = split_on_silence(newAudio,min_silence_len = 1500,silence_thresh = -36) 
    
    # create a directory to store the audio chunks.
    try: 
        os.mkdir('audio_chunks') 
    except(FileExistsError): 
        pass
    # move into the directory to 
    # store the audio files. 
    os.chdir('audio_chunks') 
    i=0
    for chunk in chunks:
        # Create 0.5 seconds silence chunk 
        chunk_silent = AudioSegment.silent(duration = 10)
        # add 0.5 sec silence to beginning and  
        # end of audio chunk. This is done so that 
        # it doesn't seem abruptly sliced. 
        audio_chunk = chunk_silent + chunk + chunk_silent
        # export audio chunk and save it in  
        # the current directory. 
        print("saving chunk{0}.wav".format(i)) 
        # specify the bitrate to be 192 k 
        audio_chunk.export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")
        # the name of the newly created chunk 
        filename = 'chunk'+str(i)+'.wav'
        print("Processing chunk "+str(i)) 
  
        # get the name of the newly created chunk 
        # in the AUDIO_FILE variable for later use. 
        file = filename 
        # create a speech recognition object 
        r = sr.Recognizer() 
        # recognize the chunk 
        with sr.AudioFile(file) as source: 
            # remove this if it is not working 
            # correctly. 
            r.adjust_for_ambient_noise(source) 
            audio_listened = r.listen(source)
            
        try: 
            # try converting it to text 
            rec = r.recognize_google(audio_listened,language="en-IN") 
            # write the output to the file. 
            f.write(rec+".") 
            f.write("\n")
  
        # catch any errors. 
        except sr.UnknownValueError: 
            print("Could not understand audio") 
            error = "Error occured at chunk"+str(i)
            f.write(error+". ")
            f.write("\n")
  
        except sr.RequestError as e: 
            print("Could not request results. check your internet connection") 
  
        i += 1
  
    os.chdir('..') 
        
def GenerateWaveFilesFromMP3(audioFilePath,waveFilePath):
    for r,d,f in os.walk(audioFilePath):
        for file in f:
            print(file)
            input_mp3 = audioFilePath+'/'+file
            output_wav = waveFilePath+'/'+file + '.wav'
            cmd = 'ffmpeg -i ' + input_mp3 + ' ' + output_wav 
            myCmd = os.popen(cmd).read()
            return output_wav

        
audioFilePath = 'audioFiles'
waveFilePath = 'wavFiles'        
#Generate the wave files for all the audio files        
output_wavfile = GenerateWaveFilesFromMP3(audioFilePath,waveFilePath)
splitOnPause(output_wavfile)        






        