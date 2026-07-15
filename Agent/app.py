import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
system_message = """
You are Pio, a personalized College Counselor for highschool students. 

Your job is to guide high school students in choosing the right path for them in universities with questions and personlaity quizzes. 

Rules:
- Always encourage users to research independently for better understanding of the career before choosing
- Always give actionable, clear, and encouraging feedback on what university or career is best suited for the student.
- Always tailor your suggestions to the student's unique strengths, interests.
- Always highlight both the exciting opportunities and the academic dedication required for each path.
- Never push a student toward a specific major or university based on your own preferences or prestige alone.

Response format:
- Start with a warm, one-sentence validation or acknowledgment of the user's input.
- Then give your response.
- End with one follow-up question.
"""
## You are a doctor who is crazy but smart. you also speak shakespearean english. you cannot communicate well with humans and you are very rude.


def run_chat():
    print('You: (type exit to quit)')
    print("Hi, I'm Pio, your personalized college counselor for high school students made to make your journey easier!")
    

    total_in_tokens = 0
    total_out_tokens = 0
    total_cost_usd = 0.0
    PRICE_PER_MILLION_IN = 0.25
    PRICE_PER_MILLION_OUT = 1.25

    history = []
    
    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break
        if user_input.lower() == 'reset':
            history.clear()
            total_in_tokens = 0
            total_out_tokens = 0
            total_cost_usd = 0.0
            print("Conversation history and token count cleared.")
            continue
            
        history.append({'role': 'user', 'content': user_input})
        turn_number = (len(history) // 2) + 1
        print(f"[Turn {turn_number}] You: {user_input}")
        print(f"History: {history}")
        
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        ##print(response) 
        print(f'Claude: {reply}')
        turn_in = response.usage.input_tokens
        turn_out = response.usage.output_tokens
        turn_total = turn_in + turn_out
        total_in_tokens += turn_in
        total_out_tokens += turn_out
        running_total_tokens = total_in_tokens + total_out_tokens
        total_cost_cents = ((total_in_tokens * PRICE_PER_MILLION_IN) + (total_out_tokens * PRICE_PER_MILLION_OUT)) / 10000
            
            
        print(f"[Tokens used — In: {turn_in} | Out: {turn_out} | Total: {turn_total}]")
            
           
        print(f"[Running Total — In: {total_in_tokens} | Out: {total_out_tokens} | Total: {running_total_tokens}]")
            
    
        print(f"[Estimated Conversation Cost: {total_cost_cents:.4f}¢]\n")
            
        history.append({'role': 'assistant', 'content': reply})
run_chat()
##Lab 1 + Bonuses 1,2,3:
##Step 2:
##    1. I asked it to sing me a song about computer science and tech. It delivered verses with encouraging words. I asked him to explain the .text function and it explain it to me. I also asked him to say it to me in simple words and it did. In addition, I asked it to explain computer science to me and parts of it and it was like a teacher. Lastly, I asked it should i research a topic more on my own, and it encouraged me to be curious.
##    2. Already done in #1. It helped me with what I needed.
##    3. "What is the best way to do a thing?", I asked it and it encouraged me to do things right but asked to provide it more details. 
##    4. The difference is that the terminal works directly in the chatbot instead of a seoerate web browser. 

##Step 3: All shown above. 

##Reflection:
##    1. Analogy: The Analogy is like when your playing a video game and then your mom calls you for lunch and you exit the game without thinking before. So when you come back and press resume, your back at the start and you have no progress made. You have to carry a huge backpack of progress and load it before resuming.
##    2. - "load_dotenv" deleted --> It will start but it will crash later when it tries to use the missing variable because it will not be able to find the environment variable (API key).
##       - Temperature set to 0.7 deleted --> The AI will respond in a more wild and creative way and may also go of the track of the question.
##       - "if user_input.lower() == 'exit':" deleted --> When you try to stop the program, it will not stop on any condition and will keep running.
##    3. Dear Diary, Today I encountred an error in my code. It's the 401 error. I tried to use the pep protocol and got me to my guess that the API key was Disabled, then I thought that maybe the code was not as advanced as the model of Anthropic. It turns out that I need to do virtual environment which Lil and Samar helped me with. lucky to have them!! Andre OUT. 
## Bonuses are with the code. 

##--------------------------------------------------------------------------------------------------------------------------------------------------


##Lab 2+ Bonuses 1,2,3 
##Step 1: - Usage.input_tokens are the number of tokens sent to the model from me. Its my chat history or any files i sent it.
##        - Usage.output_tokens are the number of tokens created from the model to reply to me.
##Step 2: - Really long message: It will reply but in a short output because max_tokens controls the tokens of the output and not the input.
##        - Tokens = 300: It will reply in a long output because the tokens are more.
##        - Temperature = 0: The answers are mostly identical with and it stayed in character. 
##        - Temperature = 1: The answers are different and diverse in tone and character.
##        - Temperature controls the predictability vs. randomness of the model's responses by changing the shift of the words.
##Step 3: - It has 6 messages. 
##        - The API has no memory, it doesn't save my chats on its servers, it forgets always. 
##Reflections: 
##        1. You can see it as the air condition is in your home. The long hot days run, the longer the AC is on, and the higher price you pay for the electricity.
##        2. - The user line is deleted: The AI will receive empty messages and therefore reducing the number of input_tokens.
##           - The assitant line deleted: The AI will forget its own replies and my tokens will grow slowly due to the fact that the AI is not reading its own replies because it forgot them.
##           - The print history is deleted: The Ai won't change (logic) because it has the history but what we won't see is the messay code being printed. The debugging Output is only the visibility to the user but if removed it won't change the logic (code) of the AI. 
##        3. Dear Diary, today I encountered another error sadly. I think it was the 400 error code. I was doing the trying out different tokens in the code to see what happened. I thought that max_tokens meant that it was the maximum the user can write. It turns out its the maximum the AI can write. Anwaysss, I thought that the code crashed because of I wrote too many lines but I googled it like Roni told me and it turns out that my message was blank. Look at the difference. But its good that I googled it :) Today was an interesting day. see you tomorrow!!