# Zadanie-oxido

### This repository contains a Python application that utilizes the OpenAI API to convert text articles into structured HTML with embedded guidelines for image placeholders and captions. The output HTML file retains the original article text while formatting it with HTML tags for readability and future image placement.

## Features

- Reads a plain text article from a specified file.
- Uses OpenAI's API to convert the article content into HTML with a structured format.
- Adds placeholders for images (<img src="image_placeholder.jpg" alt="future prompt to generate image">) and captions (<figcaption>) where images might be added.
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
