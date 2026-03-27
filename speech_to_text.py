import whisper

model = whisper.load_model("small") #base/small/medium

def speech_to_text(audio_path):
    result = model.transcribe(
        audio_path,
        language="hi",       # Force Hindi
        task="transcribe",   # Do not translate
        fp16=False           # Required for CPU
    )
    return result["text"]
