# Zadanie-oxido

### This repository contains a Python app that uses the OpenAI API to transform text articles into well-structured HTML. The app formats the articles to make them more readable, adding placeholders for images and captions where needed. This makes it easy to maintain the original content while preparing the layout for future visuals.

## Features

- Reads a plain text article from a specified file.
- Uses OpenAI's API to convert the article content into HTML with a structured format.
- Adds placeholders for images &lt;img src="image_placeholder.jpg" alt="future prompt to generate image"&gt;
- Saves the generated HTML into an output file for easy viewing.

# Setup Instructions

## 1. Clone the project

```bash
  git clone https://github.com/Valori-hub/zadanie-oxido.git
```

## 2. Go to the project directory

```bash
  cd zadanie-oxido
```

## 3. Install dependencies

```bash
  pip install -r requirements.txt
```

## 4. Configure Environment Variables

- Create a config.env file in the root directory.
- Add your OpenAI API key to the config.env file.

```bash
API_KEY=your_openai_api_key
```

## 5. Run the Program

```bash
  python main.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
