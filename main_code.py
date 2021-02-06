import pyaudio
import wave
import sys
import numpy as np
import matplotlib.pyplot as plt


def create_spectrum(data):
    '''
    creates power spectrum of the audio signal
    '''
    hanning = np.hanning(window_size)
    plt.plot(data)
    plt.show()
    windowed = data[:window_size] * hanning
    plt.plot(windowed)
    plt.show()
    spectrum = np.fft.fft(windowed) / window_size
    autopower = np.abs(spectrum * np.conj(spectrum))
    plt.plot(spectrum)
    plt.show()
    return autopower[:window_size]

def create_cepstrum(data):
    """
    Calculates the complex cepstrum of a real sequence and returns the fundamental/peak frequency
    """
    spectrum = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(spectrum))
    #l = len(data)
    imax = np.argmax(np.abs(spectrum))
    fs_max = freqs[imax]
    frequencies_max = abs(fs_max * frame_rate)
    #freq = imax * fs / l
    #frequencies.append(freq)
    #print(frequencies)
    log_spectrum = np.log(np.abs(spectrum))
    cepstrum = np.fft.ifft(log_spectrum).real
    min_freq, max_freq = 600, 700
    start = int(frame_rate / max_freq)
    end = int(frame_rate / min_freq)
    narrowed_cepstrum = cepstrum[start:end]
    peak_ix = narrowed_cepstrum.max()
    freq0 = frame_rate / (start + peak_ix)
    if freq0 < min_freq or freq0 > max_freq:
        # Ignore the note out of the desired frequency range
        return

    return freq0

def hz_to_midi(frequencies):
    return 12 * (np.log2(np.atleast_1d(frequencies)) - np.log2(440.0)) + 69
def console():

    #saurabh's midi code
    pass

wf = wave.open("0.wav", 'rb')
# instantiate PyAudio (1)
p = pyaudio.PyAudio()
# open stream (2)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(-1)
data_int = np.frombuffer(data, dtype= "int16")
frame_rate = wf.getframerate()
# duration of sound wave
duration = len(data) / frame_rate
# timestamp
Time = np.linspace(0, len(data_int) / frame_rate, len(data_int))
# window size
window_size = 2048
spectrum = create_spectrum(data_int)
freq0 = create_cepstrum(data_int)
print(freq0)
midi_note = hz_to_midi(freq0)

# play stream (3)
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(2048)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()

