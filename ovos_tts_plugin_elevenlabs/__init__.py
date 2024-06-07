import requests
import random
from ovos_plugin_manager.templates.tts import TTS, TTSValidator, RemoteTTSException


class ElevenLabsTTSPlugin(TTS):
    public_servers = [
        "https://api.elevenlabs.io",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, audio_ext="mp3",
                         validator=ElevenLabsTTSValidator(self))
        self.host = self.config.get("host", None)
        self.voice_id = self.config.get("id", None)
        self.stability = self.config.get("stability", 0)
        self.similarity = self.config.get("similarity", 0.5)
        self.voice_style = self.config.get("style", 0.5)
        self.model = self.config.get("model", None)
        self.latency_level = self.config.get("latency_level", 4)
        self.token = self.config.get("token", None)

    def get_params(self, sentence):
        return {
            "model_id": self.model,
            "text": sentence,
            "voice_settings": {
                "stability": self.stability,
                "similarity_boost": self.similarity,
                "style": self.voice_style,
                "use_speaker_boost": False
            }
        }

    def get_servers(self):
        if self.host:
            if isinstance(self.host, str):
                servers = [self.host]
            else:
                servers = self.host
        else:
            servers = self.public_servers
            random.shuffle(servers)  # Spread the load among all public servers
        return servers


    def get_headers(self):
        return {
            'xi-api-key': self.token
        }

    def get_tts(self, sentence, wav_file, lang=None, voice=None):
        data = self._get_from_servers(
            self.get_params(sentence)
        )
        with open(wav_file, "wb") as f:
            f.write(data)
        return wav_file, None

    def get_url(self, url: str):
        return f'{url}/v1/text-to-speech/{self.voice_id}'

    def get_queries(self):
        return {
            "optimize_streaming_latency": self.latency_level
        }

    def _get_from_servers(self, params: dict):
        for url in self.get_servers():
            try:
                r = requests.post(self.get_url(url),
                        json=params, headers=self.get_headers(), params=self.get_queries()
                    )
                if r.ok:
                    return r.content
            except:
                continue
        raise RemoteTTSException(f"All ElevenLabs TTS servers are down!")

class ElevenLabsTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(ElevenLabsTTSValidator, self).__init__(tts)

    def validate_lang(self):
        pass

    def validate_connection(self):
        pass

    def get_tts_class(self):
        return ElevenLabsTTSPlugin


ElevenLabsTTSConfig = {}
