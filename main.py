#==========================================================================================
# GPT-3
# AI CONVERSATIONAL PROTOTYPE
# DEVELOPED BY MITCH ALVES
#==========================================================================================

import config
from random import choice
import os
import openai

#==========================================================================================
# INITIALIZE
#==========================================================================================

openai.api_key = config.OPEN_API_KEY
completion = openai.Completion()

CHAT_LOG = None
BOT_NAME = 'AI-Bot'
USER_NAME = 'Mitch'

SESSION_PROMPT = f"Hi! I am {BOT_NAME}. You can ask me anything you want and will get a witty answer.\n\n{USER_NAME}: Who are you?\n{BOT_NAME}: I am {BOT_NAME}, your new work companion.\n\n{USER_NAME}: How were you create? Who created you? \n{BOT_NAME}: I was created by Mitch Alves, who used GPT-3 (Generative Pre-trained Transformer 3) for Artifial Intelligence conversations."

start_sequence = '\n{BOT_NAME}:'
restart_sequence = '\n\n{USER_NAME}:'

#==========================================================================================
# FUNCTIONS
#==========================================================================================

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=['\n'],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = SESSION_PROMPT 
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

#==========================================================================================
# MAIN
#==========================================================================================

if __name__ == '__main__':
    print(f'Welcome\n{USER_NAME}:')
    user_input = input()
    bot_output = ask(user_input, CHAT_LOG)
    CHAT_LOG = append_interaction_to_chat_log(user_input, bot_output, CHAT_LOG)
