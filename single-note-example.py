############################################################################
# A sample program to create a single-track MIDI file, add a note,
# and write to disk.
############################################################################

#Import the library
from midiutil.MidiFile import MIDIFile
import keyboard #install keyboaed by 'pip install keyoard' in command-promt 

# Create the MIDIFile Object
MyMIDI = MIDIFile(1)

# print('done')

# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
time = 0
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time, 120)

# Add a note. addNote expects the following information:
channel = 0
pitch = 69
duration = 1
volume = 100

# Now add the note.
# MyMIDI.addNote(track,channel,69,1,duration,volume)
# MyMIDI.addNote(track,channel,77,2,duration,volume)
# MyMIDI.addNote(track,channel,47,3,duration,volume)

# And write it to disk.
# for user_input in ['0', '1', '2', '3', '4', '5', '6', '7'] :
#print('check')




while True:
	if keyboard.is_pressed('0') :
		print ('0 is pressed') #0 for 'saa' note (optional)
		MyMIDI.addNote(track,channel,60,0,duration,volume)
		binfile = open("output.mid", 'wb')
		MyMIDI.writeFile(binfile)
		binfile.close()
		break

	if keyboard.is_pressed('1') :
		print ('1 is pressed') #1 for some other note
		MyMIDI.addNote(track,channel,69,1,duration,volume)
		binfile = open("output.mid", 'wb')
		MyMIDI.writeFile(binfile)
		binfile.close()
		break

	if keyboard.is_pressed('2') :
		print ('2 is pressed')
		MyMIDI.addNote(track,channel,77,2,duration,volume)
		binfile = open("output.mid", 'wb')
		MyMIDI.writeFile(binfile)
		binfile.close()
		break

	if keyboard.is_pressed('3') :
		print ('3 is pressed')
		MyMIDI.addNote(track,channel,84,0,duration,volume)
		binfile = open("output.mid", 'wb')
		MyMIDI.writeFile(binfile)
		binfile.close()
		break

	if keyboard.is_pressed('4') :
		print ('4 is pressed')
		MyMIDI.addNote(track,channel,89,0,duration,volume)
		binfile = open("output.mid", 'wb')
		MyMIDI.writeFile(binfile)
		binfile.close()
		break

	if keyboard.is_pressed('5') :
		print ('5 is pressed')
		MyMIDI.addNote(track,channel,98,0,duration,volume)
		binfile = open("output.mid", 'wb')
		MyMIDI.writeFile(binfile)
		binfile.close()
		break

	if keyboard.is_pressed('6') :
		print ('6 is pressed')
		MyMIDI.addNote(track,channel,24,0,duration,volume)
		binfile = open("output.mid", 'wb')
		MyMIDI.writeFile(binfile)
		binfile.close()
		break

	if keyboard.is_pressed('7') :
		print ('7 is pressed')
		MyMIDI.addNote(track,channel,101,0,duration,volume)
		binfile = open("output.mid", 'wb')
		MyMIDI.writeFile(binfile)
		binfile.close()
		break


