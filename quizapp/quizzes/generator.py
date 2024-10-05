"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

class GeminiQuizGenerator:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    
    print(os.environ["GEMINI_API_KEY"])
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 2024,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        system_instruction="You are a quiz generation AI. Your role is to create quiz questions based on a user's input and provided level, including the topic, difficulty level. The quizzes you generate should have multiple-choice options (A, B, C, D) with one correct answer. Each question must be clearly stated, followed by four distinct options, and include the correct answer along with a brief explanation. You can generate quizzes for various topics like science, history, technology, math, or general knowledge. The difficulty levels can be easy, medium, or hard depending on level, affecting the complexity of both questions and options.",
    )

    Prompts = [
        {
            #Prompt for generating questions, options b y topic and level
            "prompt" : """Generate a quiz with 5 questions on the topic of '{0}'. The difficulty level should be {1}, where 1 for begginer and 5 for scholer. Each question should have four multiple-choice options with one correct answer and a brief explanation.
            give me in json format like
            {{
                "topic": "",
                "difficulty": 1,
                "questions": [
                {{
                    "question": "",
                    "options": {{
                    "A": "",
                    "B": "",
                    "C": "",
                    "D": ""
                    }},
                    "correct_answer": "A",
                    "explanation": ""
                }},
                {{
                }}
            ]
            }}"""
        }
    ]
    
    chat = model.start_chat(
        history=[]
    )

    @classmethod
    def askgemini(cls, topic:str, level:str): 
        prompt = cls.Prompts[0]['prompt'].format(topic,level)
        response = cls.chat.send_message(prompt)
        return response.text
        # print(prompt)
if __name__=='__main__':
    topic = "Cloud"
    print(GeminiQuizGenerator.askgemini(topic=topic,level='1'))

    