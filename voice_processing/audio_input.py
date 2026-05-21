import pyaudio
import wave

def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    frames_per_buffer=1024
    )
    print("Recording... press CTRL+C to Stop")
    frames = []
    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
    except:
        print("Recording Stopped and Saved")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save WAV temporarily
    wav_file = r"data\audio_file.wav"

    wf = wave.open(wav_file, "wb")
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b"".join(frames))
    wf.close()
