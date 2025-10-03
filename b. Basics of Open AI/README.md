# OpenAI Models Overview

| Use Case / Modality         | Model Name(s) / Family                              | Example Client Code                  |
|------------------------------|-----------------------------------------------------|--------------------------------------|
| **Chat / Text Generation**  | gpt-4, gpt-4o, gpt-4o-mini, gpt-3.5-turbo           | `client.chat.completions.create()`   |
| **Image Generation**        | dall-e-2, dall-e-3, gpt-image-1                     | `client.images.generate()`           |
| **Speech-to-Text (ASR)**    | whisper-1                                           | `client.audio.transcriptions.create()`|
| **Text-to-Speech (TTS)**    | gpt-4o-mini-tts                                     | `client.audio.speech.create()`       |
| **Video Generation**        | sora (limited access)                               | *(not public in API yet)*            |
| **Embeddings**              | text-embedding-ada-002, text-embedding-3-small/large| `client.embeddings.create()`         |
