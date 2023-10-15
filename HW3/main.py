import openai
import json
from gtts import gTTS
import os

# Load the JSON data from the file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Prepare a prompt for ChatGPT
prompt = f"Create a small story about {data['name']}, a {data['age']}-year-old {data['occupation']} from {data['city']}."

# Pass the JSON data and prompt to the ChatGPT API
openai.api_key = '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'
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=150
)

story = response.choices[0].text.strip()

print("Generated Story:")
print(story)

with open('generated_story.txt', 'w') as output_file:
    output_file.write(story)

print("Generated story has been saved to generated_story.txt")

tts = gTTS(story, lang='en')

tts.save('generated_speech.mp3')

os.system('generated_speech.mp3')

