# CircuitPlaygroundExpress_AnalogIn
# reads the analog voltage level from a 10k potentiometer
# connected to GND, 3.3V, and pin A1
# and prints the results to the REPL

from adafruit_circuitplayground.express import cpx
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import board
import time
import audioio
import array
import math



#----------------------------------------------------
# Analog Pin definitions
#----------------------------------------------------
    
# make 1-5 analog pins
analoginA1 = AnalogIn(board.A1)
analoginA2 = AnalogIn(board.A2)
analoginA3 = AnalogIn(board.A3)
analoginA4 = AnalogIn(board.A4)
analoginA5 = AnalogIn(board.A5)

A1 = 0xFF
A2 = 0xFF
A3 = 0xFF
A4 = 0xFF
A5 = 0xFF

A1_PRE = 0xFF
A2_PRE = 0xFF
A3_PRE = 0xFF
A4_PRE = 0xFF
A5_PRE = 0xFF

gap = 0.3

#----------------------------------------------------
# Analog Voltage
#----------------------------------------------------
    
def getVoltage(pin):  # helper 
    return (pin.value * 3.3) / 65536


#----------------------------------------------------
# NeoPixcel definitions
#----------------------------------------------------
    
numpix = 10

def set_all_pixels(color): 
    for i in range(cpx.pixels.n):
        cpx.pixels[i] = color
    cpx.pixels.show()

def set_all_pixels_off(): 
    for i in range(cpx.pixels.n):
        cpx.pixels[i] = 0x000000
    cpx.pixels.show()
 
#----------------------------------------------------
# Sound definitions
#----------------------------------------------------
    
# set up time signature
whole_note = 1.5
half_note = whole_note / 2
quarter_note = whole_note / 4
dotted_quarter_note = quarter_note * 1.5
eighth_note = whole_note / 8

# set up note values
TONE_A3 = 220    # RA
TONE_Bb3 = 233   # 
TONE_B3 = 247    # SHI
TONE_C4 = 262    # DO
TONE_Db4 = 277
TONE_D4 = 294    # LE
TONE_Eb4 = 311   
TONE_E4 = 330    # MI
TONE_F4 = 349    # FA
TONE_Gb4 = 370
TONE_G4 = 392    # SO
TONE_Ab4 = 415
TONE_A4 = 440    # LA
TONE_Bb4 = 466
TONE_B4 = 494    # SHI
TONE_C5 = 523    # DO
TONE_D5 = 587    # LE
TONE_E5 = 659    # MI

#----------------------------------------------------
# Play Song
#----------------------------------------------------
def play_sound(tone):
    cpx.start_tone(tone)
    time.sleep(half_note)
    cpx.stop_tone()

#----------------------------------------------------
# Play Sound
#----------------------------------------------------
def play_song(song_number):

    if song_number == 1:
        # jingle bells
        jingle_bells_song = [[TONE_E4, quarter_note], [TONE_E4, quarter_note],
        [TONE_E4, half_note], [TONE_E4, quarter_note], [TONE_E4, quarter_note],
        [TONE_E4, half_note], [TONE_E4, quarter_note], [TONE_G4, quarter_note],
        [TONE_C4, dotted_quarter_note], [TONE_D4, eighth_note], [TONE_E4, whole_note]]
 
        for n in range(len(jingle_bells_song)):
            cpx.start_tone(jingle_bells_song[n][0])
            time.sleep(jingle_bells_song[n][1])
            cpx.stop_tone()
 
 
    if song_number == 2:
        # Let It Snow
        let_it_snow_song = [[TONE_B4, dotted_quarter_note], [TONE_A4, eighth_note],
        [TONE_G4, quarter_note], [TONE_G4, dotted_quarter_note], [TONE_F4, eighth_note],
        [TONE_E4, quarter_note], [TONE_E4, dotted_quarter_note], [TONE_D4, eighth_note],
        [TONE_C4, whole_note]]
 
        for n in range(len(let_it_snow_song)):
            cpx.start_tone(let_it_snow_song[n][0])
            time.sleep(let_it_snow_song[n][1])
            cpx.stop_tone()


#----------------------------------------
# Main roop
#----------------------------------------
while True:
    
    A1_PRE = A1
    A2_PRE = A2
    A3_PRE = A3
    A4_PRE = A4
    A5_PRE = A5
    
    A1 = getVoltage(analoginA1)
    A2 = getVoltage(analoginA2)
    A3 = getVoltage(analoginA3)
    A4 = getVoltage(analoginA4)
    A5 = getVoltage(analoginA5)
    
    print("V: %f  %f  %f  %f  %f" % (A1, A2, A3, A4, A5))
    
    if cpx.switch:
        if A1 < gap and A1_PRE < gap:   
            set_all_pixels(0x101000)     
            play_sound(TONE_C4)            
        if A2 < gap and A2_PRE < gap: 
            set_all_pixels(0x100010)  
            play_sound(TONE_D4)    
        if A3 < gap and A3_PRE < gap:  
            set_all_pixels(0x001010) 
            play_sound(TONE_E4)    
        if A4 < gap and A4_PRE < gap: 
            set_all_pixels(0x100000) 
            play_sound(TONE_F4)        
        if A5 < gap and A5_PRE < gap: 
            set_all_pixels(0x001000) 
            play_sound(TONE_G4)
    else:
        if A1 < gap and A1_PRE < gap:   
            set_all_pixels(0x000010) 
            play_sound(TONE_A4)    
        if A2 < gap and A2_PRE < gap:   
            set_all_pixels(0x051005) 
            play_sound(TONE_B4)    
        if A3 < gap and A3_PRE < gap:   
            set_all_pixels(0x100505) 
            play_sound(TONE_C5)    
        if A4 < gap and A4_PRE < gap:   
            set_all_pixels(0x050510) 
            play_sound(TONE_D5)        
        if A5 < gap and A5_PRE < gap:   
            set_all_pixels(0x101010)
            play_sound(TONE_E5)
    set_all_pixels_off()
    
    
    if cpx.button_a & cpx.button_b:
        play_song(1)
        
    elif cpx.button_a:
        cpx.play_file("rimshot.wav")
        
    elif cpx.button_b:
        cpx.play_file("laugh.wav")

    
    time.sleep(0.1)
	