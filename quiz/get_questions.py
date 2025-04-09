from openai import OpenAI
import os

my_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=my_key)

response = client.responses.create(
  model="gpt-4o",
  input=[
    {
      "role": "system",
      "content": [
        {
          "type": "input_text",
          "text": "Return each question as a list: [question_text, option1, option2, option3, option4, correct_option_index]"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "Generate 5 random trivia questions"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "Sure! Here are five random trivia questions:\n\n1. \n   - \"What is the capital of France?\"\n   - \"Lyon\"\n   - \"Marseille\"\n   - \"Paris\"\n   - \"Nice\"\n   - 3\n   \n2. \n   - \"Who wrote the play 'Romeo and Juliet'?\"\n   - \"William Wordsworth\"\n   - \"William Shakespeare\"\n   - \"Charles Dickens\"\n   - \"Jane Austen\"\n   - 2\n\n3. \n   - \"What is the largest mammal in the world?\"\n   - \"Elephant\"\n   - \"Blue Whale\"\n   - \"Giraffe\"\n   - \"Hippopotamus\"\n   - 2\n\n4. \n   - \"Which element has the chemical symbol 'O'?\"\n   - \"Gold\"\n   - \"Oxygen\"\n   - \"Osmium\"\n   - \"Nitrogen\"\n   - 2\n\n5. \n   - \"In which year did the Titanic sink?\"\n   - \"1914\"\n   - \"1912\"\n   - \"1916\"\n   - \"1920\"\n   - 2"
        }
      ]
    }
  ],
  text={
    "format": {
      "type": "text"
    }
  },
  reasoning={},
  tools=[],
  temperature=1,
  max_output_tokens=2048,
  top_p=1,
  store=True
)

print(response.output_text)
