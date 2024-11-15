from openai import OpenAI
from dotenv import load_dotenv
import sys
import time
import os

# Load environment variables from the .env file
load_dotenv("config.env")
client = OpenAI(api_key=os.environ.get("API_KEY"))


# Reads the content of an article file from the specified file path.
def read_article(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"Success: The file '{file_path}' was read successfully.")
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


# Displays a spinning loader in the terminal to indicate processing is ongoing.
def spinning_loader():
    spinner = ["|", "/", "-", "\\"]
    while True:
        for symbol in spinner:
            sys.stdout.write(f"\rProcessing {symbol}")
            sys.stdout.flush()
            time.sleep(0.1)


# Sends the article text to the OpenAI API for processing and structuring the text into HTML.
def process_article_with_openai(article_text):
    full_prompt = "Please structure the following article into HTML format, strictly adhering to the guidelines listed below.\n"
    full_prompt += (
        "Here are the guidelines: \n"
        "1. Divide the text into sections based on the natural context and flow, using <section> tags for each section. Each section should represent a cohesive idea or topic.\n"
        "2. Use <h1> for the main title and <h2> for subheadings, followed by relevant content within <p> tags.\n"
        '3. Insert <img src="image_placeholder.jpg"> where suitable images might be added.\n'
        "4. Ensure the alt attribute provides a detailed description of the image for future AI image generation prompts. Avoid buzzwords, and write this in English.\n"
        "5. Add a <figcaption> with a short caption in Polish below each image.\n"
        "6. Wrap <img> and <figcaption> tags in a <figure> tag.\n"
        "7. Exclude <html>, <head>, and <body> tags; include only the content for the <body> section.\n"
        "8. Ensure that every part of the text remains within a section.\n"
        "9. Maintain the original order of the lines as they appear in the input text to ensure clarity.\n"
        "10. Make sure that no part of the input text is omitted, and the entire text is included in your response without any omissions or truncations.\n"
    )

    try:
        # Import threading to allow the loader to run in parallel with the API call
        import threading

        # Start the spinning loader in a separate thread
        loader_thread = threading.Thread(target=spinning_loader)
        loader_thread.daemon = True
        loader_thread.start()

        # Make the OpenAI API call
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": full_prompt},
                {"role": "user", "content": article_text},
            ],
        )
        # Get the generated HTML content from the response
        generated_html = response.choices[0].message.content

    except Exception as e:
        print(f"Error: {e}")
        return None
    return generated_html


# Saves the generated HTML content to a specified file.
def save_html_to_file(html_content, output_file="artykul.html"):
    # Create the folder if not exist
    output_folder = os.path.dirname(output_file)
    os.makedirs(output_folder, exist_ok=True)
    # Save the HTML file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"Generated HTML code saved to file {output_file}")


def main():
    input_file = "data/artykul.txt"
    output_file = f"output/artykul.html"
    article_text = read_article(input_file)  # Read the article content

    html_content = process_article_with_openai(article_text)

    save_html_to_file(html_content, output_file)


if __name__ == "__main__":
    main()
