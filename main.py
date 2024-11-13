from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv("config.env")
client = OpenAI(api_key=os.environ.get("API_KEY"))


def read_article(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def process_article_with_openai(article_text):
    full_prompt = f"{article_text}\n\n"
    full_prompt += (
        "Here are the guidelines: \n"
        "1. Use proper HTML tags for the structure, such as <h1> for main headings, <h2> for subheadings, <p> for paragraphs etc.\n"
        '2. Add <img src="image_placeholder.jpg" alt="detailed description of the image as a prompt for future image generation, dont use buzz words"> where suitable images might be added">\n'
        "3. Add <figcaption> to place a caption below each image.\n"
        "4. Do not include <html>, <head>, or <body> tags, only content for the <body> section.\n"
        "5. Ensure that the article text remains exactly as it is, without any alterations."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": full_prompt}],
    )

    generated_html = response.choices[0].message.content

    return generated_html


def save_html_to_file(html_content, output_file="artykul.html"):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"Generated HTML code saved to file {output_file}")


def main():
    input_file = "data/artykul.txt"
    output_file = "output/artykul.html"
    article_text = read_article(input_file)

    html_content = process_article_with_openai(article_text)

    save_html_to_file(html_content, output_file)


if __name__ == "__main__":
    main()
