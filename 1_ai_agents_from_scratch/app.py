from flask import Flask, request, render_template_string
from agents.rule_based import RuleBasedAgent
from agents.memory import MemoryAgent
from agents.chat import ChatAgent
from agents.llm import LLMAgent
from utils.api_keys import WEATHER_API_KEY
import time

app = Flask(__name__)

rule_agent = RuleBasedAgent()
memory_agent = MemoryAgent()
chat_agent = ChatAgent()
llm_agent = LLMAgent()

cache = {}

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['message']
        start_time = time.time()

        if user_input in cache:
            response = cache[user_input]
        elif user_input.startswith("weather in"):
            response = chat_agent.respond(user_input)
            
