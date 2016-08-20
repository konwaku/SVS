# dependency:

import matplotlib.pyplot as plt
import numpy as np
import numpy as np
from pydub import AudioSegment
import SIMM
import scipy.io.wavfile as wav
import os
from tracking import viterbiTrackingArray
import Tkinter
import os
import tkFileDialog
import tkMessageBox
from Tkinter import *
from separateLeadStereoParam import main

def file_path(FILE_PATH='/home/2'):
    if os.path.isdir(FILE_PATH):
        print 'dir %s exsits' % (FILE_PATH)
        pass
    else:
        print 'dir %s not exsits' % (FILE_PATH)
        os.makedirs(FILE_PATH)
        return 0

def divide_music(input_song = 'input.wav'):

    song = AudioSegment.from_wav('input.wav')
    ss = 10000
    length_song= len(song.duration_seconds)
    for part in range (length_song/ss):
        file_path('temp/')
        song[part*ss:ss*(part+1)].export('temp/'+input_song.split(".")[0]+'_'+str(part)+'wav','wav')
    return 0

def conbination_all_pieces(path_to_file='temp'):
    for parent, dirnames, filenames in os.walk(path_to_file):
        total_num = len (filenames)
    song = AudioSegment.from_wav('temp/input_0.wav')
    for part in range (total_num):
        song = song+AudioSegment.from_wav('temp/input_'+str(part+1)+'.wav')
    song.export('conbination.wav','wav')
    return 0

song = AudioSegment.from_wav('input.wav')
if song.duration_seconds < 10:
    pass
else:
    divide_music('input.wav')