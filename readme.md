## Description

OpenVoiceOS companion plugin for [OpenVoiceOS TTS Server](https://github.com/OpenVoiceOS/ovos-tts-server)

## Install

```bash
pip install git+https://github.com/FormigTeen/ovos-tts-plugin-elevenlabs.git
```

## Configuration

```json
  "tts": {
    "module": "ovos-tts-plugin-elevenlabs",
    "ovos-tts-plugin-elevenlabs": {
        "token": "YOUR-TOKEN-HERE",
        "model": "eleven_multilingual_v1",
        "id": "your-voice-id",
        "stability": 0.5,
        "similarity_boost": 0,
        "style": 0.2
    }
 }
```
