#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:33:47 2019

@author: ananya
"""
import speech_recognition as sr 

choppedWaveFiles = 'split_pauses_Files/'    
outputFile =  'Transcribed.txt' 
f = open(outputFile, "w+")
#Generate the wave files for all the audio files        

choppedList = ['s_1.wav', 's_2.wav', 's_3.wav', 's_4.wav', 's_5.wav', 's_6.wav', 's_7.wav', 's_8.wav', 's_9.wav', 's_10.wav', 's_11.wav', 's_12.wav', 's_13.wav', 's_14.wav', 's_15.wav', 's_16.wav', 's_17.wav', 's_18.wav', 's_19.wav', 's_20.wav', 's_21.wav', 's_22.wav', 's_23.wav', 's_24.wav', 's_25.wav', 's_26.wav', 's_27.wav', 's_28.wav', 's_29.wav', 's_30.wav', 's_31.wav', 's_32.wav', 's_33.wav', 's_34.wav', 's_35.wav', 's_36.wav', 's_37.wav', 's_38.wav', 's_39.wav', 's_40.wav', 's_41.wav', 's_42.wav', 's_43.wav', 's_44.wav', 's_45.wav', 's_45_1.wav', 's_45_2.wav', 's_45_3.wav', 's_45_4.wav', 's_45_5.wav', 's_45_6.wav', 's_46.wav', 's_47.wav', 's_48.wav', 's_49.wav', 's_50.wav', 's_51.wav', 's_52.wav', 's_53.wav', 's_54.wav', 's_55.wav', 's_56.wav', 's_57.wav', 's_58.wav', 's_59.wav', 's_60.wav', 's_61.wav', 's_62.wav', 's_63.wav', 's_64.wav', 's_65.wav', 's_66.wav', 's_67.wav', 's_68.wav', 's_69.wav', 's_70.wav', 's_71.wav', 's_72.wav', 's_73.wav', 's_74.wav', 's_75.wav', 's_76.wav', 's_77.wav', 's_78.wav', 's_79.wav', 's_80.wav', 's_81.wav', 's_82.wav', 's_83.wav', 's_84.wav', 's_85.wav', 's_86.wav', 's_87.wav', 's_88.wav', 's_89.wav', 's_90.wav', 's_91.wav', 's_92.wav', 's_93.wav', 's_94.wav', 's_95.wav', 's_96.wav', 's_97.wav', 's_98.wav', 's_99.wav', 's_100.wav', 's_101.wav', 's_102.wav', 's_103.wav', 's_104.wav', 's_105.wav', 's_106.wav', 's_107.wav', 's_108.wav', 's_109.wav', 's_110.wav', 's_111.wav', 's_112.wav', 's_113.wav', 's_114.wav', 's_115.wav', 's_116.wav', 's_117.wav', 's_118.wav', 's_119.wav', 's_120.wav', 's_121.wav', 's_122.wav', 's_123.wav', 's_124.wav', 's_125.wav', 's_126.wav', 's_127.wav', 's_128.wav', 's_129.wav', 's_130.wav', 's_131.wav', 's_132.wav', 's_133.wav', 's_134.wav', 's_135.wav', 's_136.wav', 's_137.wav', 's_138.wav', 's_139.wav', 's_140.wav', 's_141.wav', 's_142.wav', 's_143.wav', 's_144.wav', 's_145.wav', 's_146.wav', 's_147.wav', 's_148.wav', 's_149.wav', 's_150.wav', 's_151.wav', 's_152.wav', 's_153.wav', 's_154.wav', 's_155.wav', 's_156.wav', 's_157.wav', 's_158.wav', 's_159.wav', 's_160.wav', 's_161.wav', 's_162.wav', 's_163.wav', 's_164.wav', 's_165.wav', 's_166.wav', 's_167.wav', 's_168.wav', 's_169.wav', 's_170.wav', 's_171.wav', 's_172.wav', 's_173.wav', 's_174.wav', 's_175.wav', 's_176.wav', 's_177.wav', 's_178.wav', 's_179.wav', 's_180.wav', 's_181.wav', 's_182.wav', 's_183.wav', 's_184.wav', 's_185.wav', 's_186.wav', 's_187.wav', 's_188.wav', 's_189.wav', 's_190.wav', 's_191.wav', 's_192.wav', 's_193.wav', 's_194.wav', 's_195.wav', 's_196.wav', 's_197.wav', 's_198.wav', 's_199.wav', 's_200.wav', 's_201.wav', 's_202.wav', 's_203.wav', 's_204.wav', 's_205.wav', 's_206.wav', 's_207.wav', 's_208.wav', 's_209.wav', 's_210.wav', 's_211.wav', 's_212.wav', 's_213.wav', 's_214.wav', 's_215.wav', 's_216.wav', 's_217.wav', 's_218.wav', 's_219.wav', 's_220.wav', 's_221.wav', 's_222.wav', 's_223.wav', 's_224.wav', 's_225.wav', 's_226.wav', 's_227.wav', 's_228.wav']

for wavfile in choppedList:
    file = choppedWaveFiles+wavfile
    print("Processing"+file)       
    r = sr.Recognizer() 
    # recognize the chunk 
    with sr.AudioFile(file) as source: 
        # remove this if it is not working 
        # correctly. 
        #r.adjust_for_ambient_noise(source) 
        audio_listened = r.listen(source)
        
    try: 
        # try converting it to text 
        rec = r.recognize_google(audio_listened,language="en-IN") 
        # write the output to the file. 
        f.write(rec+". ") 
        f.write("\n")
  
    # catch any errors. 
    except sr.UnknownValueError: 
        print("Could not understand audio") 
        error = "Error occured at chunk"+wavfile
        f.write(error+". ")
        f.write("\n")
  
    except sr.RequestError as e: 
        print("Could not request results. check your internet connection") 





        