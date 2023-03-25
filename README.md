# GPT CLI
This tool interacts with OpenAI's api.

## Requirements 
- Python 3.9+
- OpenAI API key
- Supported platforms: mac, win, linux

Create an OpenAI key and set `OPENAI_API_KEY` as an environment variable.
```
export OPENAI_API_KEY=sk-*********
```

## Install
```
make install
```
To uninstall run the following
```
make clean
```

## CLI Usage
Chat with ChatGPT
```
gpt-chat <YOUR PROMPT>
```

Get an Image
```
gpt-image --prompt '<YOUR-PROMPT>' --count 1 --resolution '1024x1024'
```
| Flag         | Short Flag | Description                      |
|:-------------|:-----------|:---------------------------------|
| --prompt     | -p         | Prompt to generate image         |
| --count      | -c         | Number of variations to generate |
| --resolution | -r         | Resolution of the image          |

