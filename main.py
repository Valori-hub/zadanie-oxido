import openai
from dotenv import load_dotenv
import os

load_dotenv("config.env")
openai.api_key = os.getenv("API_KEY")


def read_article(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


input_file = "data/artykul.txt"

read_article(input_file)
