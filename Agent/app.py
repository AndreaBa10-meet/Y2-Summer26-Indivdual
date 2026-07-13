import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = input("What personality would you like the AI to have? ")

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break
        if user_input.lower() == 'reset':
            history.clear()
            print("Conversation history cleared.")
            continue
        history.append({'role': 'user', 'content': user_input})
        turn_number = (len(history) // 2) + 1
        print(f"[Turn {turn_number}] You: {user_input}")
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

##Step 2:
##    1. I asked it to sing me a song about computer science and tech. It delivered verses with encouraging words. I asked him to explain the .text function and it explain it to me. I also asked him to say it to me in simple words and it did. In addition, I asked it to explain computer science to me and parts of it and it was like a teacher. Lastly, I asked it should i research a topic more on my own, and it encouraged me to be curious.
##    2. Already done in #1. It helped me with what I needed.
##    3. "What is the best way to do a thing?", I asked it and it encouraged me to do things right but asked to provide it more details. 
##    4. The difference is that the terminal works directly in the chatbot instead of a seoerate web browser. 

##Step 3: All shown above. 

##Reflection:
##    1. Analogy: The Analogy is like when your playing a video game and then your mom calls you for lunch and you exit the game without thinking before. So when you come back and press resume, your back at the start and you have no progress made. You have to carry a huge backpack of progress and load it before resuming.
##    2. - "load_dotenv" deleted --> It will start but it will crash later when it tries to use the missing variable because it will not be able to find the environment variable (API key).
##       - Temperature set to 0.7 --> The AI will respond in a more wild and creative way and may also go of the track of the question.
##       - "if user_input.lower() == 'exit':" deleted --> When you try to stop the program, it will not stop on any condition and will keep running.
##    3. Dear Diary, Today I encountred an error in my code. It's the 401 error. I tried to use the pep protocol and got me to my guess that the API key was Disabled, then I thought that maybe the code was not as advanced as the model of Anthropic. It turns out that I need to do virtual environment which Lil and Samar helped me with. lucky to have them!! Andre OUT. 
## Bonuses are with the code. 
