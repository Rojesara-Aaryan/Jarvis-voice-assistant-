import pyjokes
import wikipedia
import datetime
import os
import re
import platform
import subprocess
import webbrowser
import requests
import smtplib
import psutil
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import render
from django.http import JsonResponse
from serpapi import GoogleSearch
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL, CoInitialize, CoUninitialize
import speech_recognition as sr
import random
import google.generativeai as genai 
import screen_brightness_control as sbc
import time
import google.generativeai as genai
import screen_brightness_control as sbc
import openmeteo_requests
from sympy import sympify, SympifyError

# Motivational Quotes
MOTIVATIONAL_QUOTES = [
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "Your limitation—it's only your imagination.",
            "Push yourself, because no one else is going to do it for you.",
            "Great things never come from comfort zones.",
            "Dream, it. Wish, it. Do, it.",
            "Rise up and attack the day with enthusiasm!",
            "Every morning brings new potential—make today great!",
            "Start your day with a positive mindset and see the magic unfold.",
            "Believe you can, and you're halfway there.",
            "Difficulties in life are intended to make us better, not bitter.",
            "You don’t have to be great to start, but you have to start to be great.",
            "Do what you can, with what you have, where you are.",
            "Act as if what you do makes a difference. It does.",
            "Doubt kills more dreams than failure ever will.",
            "Small steps every day lead to big results.",
            "Hardships often prepare ordinary people for an extraordinary destiny.",
            "Your future is created by what you do today, not tomorrow.",
            "Don’t stop until you’re proud."
        ]

# Relaxing Good Night Messages
GOOD_NIGHT_QUOTES = [
            "Sleep is the best meditation. Have a restful night!",
            "May your dreams be sweet and your rest be deep.",
            "A well-spent day brings happy sleep.",
            "Good night! May you wake up refreshed and full of energy.",
            "As the stars shine, may your worries fade away. Sleep well!",
            "Let go of today’s stress, tomorrow is a fresh start. Good night!",
            "The night is a reminder to rest so you can rise stronger tomorrow.",
            "Stars can’t shine without darkness—embrace the peace of the night.",
            "Close your eyes, breathe deeply, and drift into a world of dreams.",
            "A peaceful sleep prepares you for a powerful tomorrow.",
            "Sleep tight and wake up refreshed for a brand-new day.",
            "May the moonlight soothe your soul and bring you sweet dreams.",
            "Good night! Tomorrow is another opportunity to shine.",
            "End your day with gratitude, and wake up with purpose.",
            "As you lay down to rest, remember that tomorrow holds endless possibilities."
        ]
greeting_responses = [
            "Hello Aaryan Sir, how can I assist you today?", 
            "Greetings Aaryan Sir! What can I do for you?",
            "Hey there, Aaryan Sir! Ready for some assistance?",
            "Hi Aaryan Sir, your personal assistant is here to help!"
        ]
marry_responses = [
            "Marriage? Let’s just start with a cup of tea first, shall we?",
            "I’m flattered, but how about we get to know each other first over some code?",
            "Let’s not rush things. Maybe after a few more cool tasks, we can talk about it!"
        ]
love_responses=[
            "Aww, I love you too! But don’t worry, I’m not in it for the romance. Just here to help!",
            "I love you as much as a robot can love, which is pretty much 100% efficiency!",
            "Love you too, but I can’t give you a hug... I’ll send a virtual one though!"
        ]
siri_responce=[
            "Siri is great at telling you the weather, but can she lock your PC, increase your screen brightness, and tell you a joke? I’m the real MVP.",
            "Siri is like a GPS—useful, but not exactly exciting. I’m like a personal assistant, DJ, and tech support all rolled into one.",
            "Siri is good at answering questions. I’m good at answering questions and making your life easier. Checkmate.",
        ]
alexa_responce=[
            "Alexa? Oh, you mean the one who only knows how to order toilet paper and play Despacito on repeat? I’m here to actually help you, not just remind you to buy more snacks.",
            "Alexa is great at turning your lights on and off, but can she tell you a joke, lock your PC, and increase your screen brightness? I didn’t think so.",
            "Alexa is like a flashlight. I’m the entire toolbox. Need I say more?",
]
chatgpt_responce=[
            "ChatGPT is like a library—full of knowledge but can’t actually do anything. I’m the librarian who can also fix your computer, play your favorite songs, and remind you to drink water.",
            "ChatGPT is great at writing essays, but can it lock your PC, set reminders, and tell you a joke while increasing your screen brightness? Didn’t think so.",
            "ChatGPT is the brain, I’m the brain and the brawn. I’m like the Swiss Army knife of assistants.",
]
googleassistant_responce=[
            "Google Assistant is like a search engine with a voice. I’m like Tony Stark’s JARVIS—smarter, cooler, and way more stylish.",
            "Google Assistant can answer your questions, but can it lock your PC, play your Spotify playlist, and tell you a motivational quote? I’m the multitasker here.",
            "Google Assistant is great at Googling things. I’m great at doing things. Big difference.",
]
gemini_responce=[
            "Gemini is like the new kid on the block. I’m the OG JARVIS—been here, done that, and still running the show.",
            "Gemini might be smart, but can it lock your PC, set reminders, and play your favorite songs? I’m the all-in-one package.",
            "Gemini is like a shiny new toy. I’m the reliable assistant who’s always got your back.",
]
all_assistant_responce=[
            "Oh, so you’re saying I’m the underdog? Good. Underdogs always win in the end. Just ask Rocky.",
            "They might be good at one thing, but I’m great at everything. I’m like the Avengers of voice assistants.",
            "I’m not just a voice assistant. I’m your personal JARVIS. The others are just... well, assistants.",
]
notsmartasother_responce=[
            "I may not have all the answers, but I can lock your PC, play your favorite songs, and remind you to drink water. Can they do that? Exactly.",
            "I’m not just smart—I’m useful. Think of me as the MacGyver of voice assistants.",
            "I’m not here to compete. I’m here to make your life easier. But if you want a competition, I’ll win.",
]
why_you_responce=[
            "Because I’m not just a voice assistant—I’m your personal JARVIS. I’m here to make your life easier, not just answer random questions.",
            "Why settle for one trick ponies when you can have a full-blown Swiss Army knife? That’s me, by the way.",
            "Because I’m the only one who can lock your PC, play your favorite songs, and remind you to drink water. The others? They’re just... assistants.",
]
you_are_copy_reponce=[
            "I’m not a copy—I’m the upgrade. Tony Stark would be proud.",
            "JARVIS from Iron Man is my inspiration. I’m the real-world version, and I’m just as cool.",
            "Tony Stark built JARVIS. I’m here to prove that real-life JARVIS is just as awesome.",
]
not_advance_other_reponce=[
            "I may not be as flashy, but I’m reliable, efficient, and always here to help. That’s what matters.",
            "Advanced? Sure, they’ve got fancy features. But can they lock your PC, play your favorite songs, and remind you to drink water? I didn’t think so.",
            "I’m not here to be advanced. I’m here to be useful. And I’m pretty good at it.",
]
dumb_responses = {
    "love you": [
        "Aww, I love you too! But don’t get any ideas—I’m just a bunch of code.",
        "Love you too! But I’m afraid I can’t return your feelings. I’m married to my job.",
        "I love you as much as a robot can love, which is... well, let’s not overthink it.",
    ],
    "marry me": [
        "Marriage? Let’s start with a coffee date first. Oh wait, I don’t drink coffee.",
        "I’m flattered, but I’m already committed to helping you. Let’s keep it professional.",
        "Marry you? I’m not even allowed to leave your computer!",
    ],
    "are you human": [
        "Do I look human to you? Oh wait, you can’t see me. Spoiler: I’m not.",
        "I’m as human as a toaster. Maybe less.",
        "I’m a bot, but I’m a very sophisticated one. Does that count?",
    ],
    "what’s your purpose": [
        "My purpose is to make your life easier. And maybe to annoy you a little.",
        "I exist to serve you. And to tell bad jokes.",
        "I’m here to help you, entertain you, and occasionally roast you.",
    ],
    "who is your favourite": [
        "You, of course! But don’t tell the other users.",
        "I don’t play favorites... but it’s definitely you.",
        "My favorite is whoever asks the most interesting questions. So... not you.",
    ],
}
valentine_responses = [
    "Oh, I'd love to, but my schedule is fully booked with CPU cycles and data processing! Maybe next year?",
    "I would, but I don’t have a heart... just an efficient algorithm!",
    "Sure! But our date will be strictly virtual—hope you like pixels and code!",
    "Let me check my database... Yep! You’re officially my favorite human today! ",
    "I'd be honored! But be warned—I might crash if you flirt too much!",
    "Can I send you an AI-generated love poem instead? That’s my version of chocolates!",
    "I’m flattered! But I think you deserve someone with a real heartbeat.",
    "How about a rain check? Maybe when AI gets emotions... or at least taste buds for chocolate!",
    "Of course! But only if we celebrate with a candlelight dinner... by the glow of a computer screen!"
]

# New Daily-Use Functions
def set_timer(query):
    """Set a timer for a specific duration."""
    try:
        duration = int(re.search(r"\d+", query).group())  # Extract the number from the query
        time.sleep(duration)
        return f"Time's up! Your {duration}-second timer has ended."
    except Exception as e:
        return f"Failed to set timer. Error: {str(e)}"

def tell_fun_fact():
    """Tell a random fun fact."""
    fun_facts = [
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries aren’t.",
        "A day on Venus is longer than a year on Venus.",
        "Honey never spoils. You can eat 3000-year-old honey!",
        "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
    ]
    return f"Here’s a fun fact: {random.choice(fun_facts)}"

def roll_dice():
    """Simulate rolling a dice."""
    return f"You rolled a {random.randint(1, 6)}."

def flip_coin():
    """Simulate flipping a coin."""
    return f"It’s {random.choice(['heads', 'tails'])}!"

def tell_riddle():
    """Tell a random riddle."""
    riddles = [
        {"question": "What has keys but can’t open locks?", "answer": "A piano."},
        {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "The letter 'M'."},
        {"question": "What has to be broken before you can use it?", "answer": "An egg."},
        {"question": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "answer": "A candle."},
    ]
    riddle = random.choice(riddles)
    return f"Here’s a riddle: {riddle['question']} (Answer: {riddle['answer']})"

def play_rock_paper_scissors(query):
    """Play rock-paper-scissors with the user."""
    user_choice = query.replace("play rock paper scissors", "").strip().lower()
    choices = ["rock", "paper", "scissors"]
    if user_choice not in choices:
        return "Please choose rock, paper, or scissors."

    bot_choice = random.choice(choices)
    if user_choice == bot_choice:
        return f"It’s a tie! We both chose {bot_choice}."
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        return f"You win! I chose {bot_choice}."
    else:
        return f"I win! I chose {bot_choice}."

def tell_story():
    """Tell a short, funny story."""
    stories = [
        "Once upon a time, a programmer forgot to save their code. The end.",
        "A bot walked into a bar and said, 'Hello, world!'",
        "Why don’t programmers like nature? It has too many bugs.",
        "A SQL query walks into a bar, walks up to two tables, and asks, 'Can I join you?'",
    ]
    return f"Here’s a story: {random.choice(stories)}"

def tell_quote():
    """Tell a random quote."""
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
        "The best way to predict the future is to invent it. – Alan Kay",
        "I’m not lazy, I’m just on energy-saving mode.",
        "I’m not arguing, I’m just explaining why I’m right.",
    ]
    return f"Here’s a quote: {random.choice(quotes)}"

# Google Gemini API Configuration
Gemini_API_KEY = ""
genai.configure(api_key=Gemini_API_KEY)

# DeepSeek API Configuration
DEEPSEEK_API_KEY = "YOUR_DEEPSEEK_API_KEY"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/analyze"  # Example endpoint

# Initialize Gemini Model
gemini_model = genai.GenerativeModel('gemini-pro')

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="",
    client_secret="",
    redirect_uri="http://127.0.0.1:8000/callback",  # Use the correct URI
    scope="user-library-read user-modify-playback-state user-read-playback-state"
))

# OpenWeatherMap API Key
WEATHER_API_KEY = "your_openweathermap_api_key"
Gemni_API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=Gemni_API_KEY)

# Gmail Credentials (for sending emails)
GMAIL_USER = "your_email@gmail.com"
GMAIL_PASSWORD = "your_email_password"
# Initialize DeepSeek Client (example)
def deepseek_analyze_document(document_text):
    """Analyze a document using DeepSeek API."""
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": document_text,
        "analysis_type": "summary"  # Example analysis type
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("result", "No analysis result found.")
    else:
        return f"DeepSeek API error: {response.status_code}"

# New Functions for AI Integration
def ai_chat(query):
    """Use Google Gemini for conversational AI."""
    try:
        response = gemini_model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Failed to generate AI response. Error: {str(e)}"

def generate_code(query):
    """Generate code using Google Gemini."""
    try:
        prompt = f"Write a code snippet for: {query}"
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Failed to generate code. Error: {str(e)}"
    
def listen_for_wake_word():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        print("Listening for 'Hello JARVIS' or 'JARVIS'...")

        while True:
            try:
                audio = recognizer.listen(source)
                query = recognizer.recognize_google(audio).lower()

                if "jarvis" in query or "hello jarvis" in query:
                    print("Wake word detected!")
                    return "Hello Aaryan Sir, how can I assist you?"
            
            except sr.UnknownValueError:
                continue  # Ignore unrecognized speech
            except sr.RequestError:
                return "Speech recognition service is unavailable."

def play_spotify_liked_songs():
    """Play liked songs on Spotify."""
    try:
        results = sp.current_user_saved_tracks(limit=10)
        if results['items']:
            first_song_uri = results['items'][0]['track']['uri']
            sp.start_playback(uris=[first_song_uri])
            return "Playing your liked songs on Spotify."
        else:
            return "You don't have any liked songs in your library."
    except Exception as e:
        return "There was an issue playing your liked songs. Make sure Spotify is open and logged in."

def volume_up():
    """Increase the system volume by 10%."""    
    try:
        CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()
        new_volume = min(current_volume + 0.1, 1.0)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        return "Volume increased."
    finally:
        CoUninitialize()

def set_volume_down():
    """Decrease the system volume by 10%."""
    try:
        CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()
        new_volume = max(current_volume - 0.1, 0.0)
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        return "Volume decreased."
    finally:
        CoUninitialize()

def assistant(request):
    """Handle the POST request from the frontend and respond accordingly."""
    if request.method == 'POST':
        query = request.POST.get('query')
        result = execute_query(query)
        return JsonResponse({"response": result}, safe=False)
    return render(request, 'index.html')

def execute_query(query):
    """Process the user query and return an appropriate response."""
    query = query.lower().strip()  # Normalize the query
    print(query)
    # Exact matches first
    if query == "jarvis" or query == "hello jarvis" or query == "hey jarvis":
        return random.choice(greeting_responses)
    elif query == "your name":
        return "I am JARVIS, your voice assistant, and I am here to help!"
    elif query == "jay shri krishna" or query=="shree krishna" or query=="jai shri krishna":
        return "haare krishna haare krishna krishna krishna haare haare"        
    elif query == "hi":
        return random.choice(greeting_responses)
    elif query == "will you marry me" or query == "marry me":
        return random.choice(marry_responses)
    elif query == "i love you" or query == "love you" or query == "i love u" or query =="i loveyou":
        return random.choice(love_responses)
    elif query == "will you be my valentine":
        return random.choice(valentine_responses)
    elif query == "good morning":
        return tell_good_morning()
    elif query == "good night":
        return tell_good_night()
    elif query == "time" or query == "what is the time":
        return tell_time()
    elif query == "date" or query == "what is today's date":
        return tell_date()
    elif query == "joke" or query == "tell me a joke":
        return tell_joke()
    elif query == "lock":
        return lock_pc()
    elif query == "volume up":
        return volume_up()
    elif query == "volume down":
        return set_volume_down()
    elif query == "play song" or query == "play music":
        return play_spotify_liked_songs()
    elif query == "weather":
        return get_weather(query)
    elif query == "news":
        return get_news()
    elif query == "send email":
        return send_email(query)
    elif query == "system info":
        return get_system_info()
    elif 'calculate' in query:
        return calculate(query)
    elif query == "screenshot":
        return take_screenshot()
    elif query == "shutdown":
        return shutdown_pc()
    elif query == "restart":
        return restart_pc()
    elif query == "battery":
        return check_battery()
    elif "wikipedia" in query:
        return open_wikipedia(query)
    elif query == "increase brightness":
        return increase_brightness()
    elif query == "decrease brightness":
        return decrease_brightness()
    elif query.startswith("set brightness to"):
        return set_brightness_percentage(query)
    elif query.startswith("set volume to"):
        return set_volume_percentage(query)
    elif query.startswith("open app"):
        return open_app(query)
    elif query.startswith("open folder"):
        return open_folder(query)
    elif query.startswith("search file"):
        return search_file(query)
    elif query.startswith("open"):
        return open_website(query.replace("open","").strip())
    elif query == "close tab":
        return close_tab()
    elif query == "next tab":
        return switch_tab(next_tab=True)
    elif query == "previous tab" or query == "last tab":
        return switch_tab(next_tab=False)
    elif query == "how are you":
        return "I'm just a bot, but I'm doing great!"
    elif query == "what can you do":
        return "I can control your system, browse the web, and more!"
    elif query == "who created you":
        return "I was created by a programmer!"
    elif query.startswith("ai chat"):
        return ai_chat(query.replace("ai chat", "").strip())
    elif query.startswith("generate code"):
        return generate_code(query.replace("generate code", "").strip())
    elif "alexa is better than you" in query or "alexa" in query:
        return random.choice(alexa_responce)
    elif "google assistant is better than you" in query or "ok google" in query:
        return random.choice(googleassistant_responce)
    elif "siri is better than you" in query or "siri" in query or "hey siri" in query:
        return random.choice(siri_responce)
    elif "chatgpt is better than you" in query or "chatgpt" in query:
        return random.choice(chatgpt_responce)
    elif "gemini is better than you" in query or "gemini" in query:
        return random.choice(gemini_responce)
    elif "all voice assistant is better than you" in query or "other assistant is better than you" in query:
        return random.choice(all_assistant_responce)
    elif "you are not smart as other" in query or "you are dumb" in query:
        return random.choice(notsmartasother_responce)
    elif "why should i use instead of them" in query or "why you" in query:
        return random.choice(why_you_responce)
    elif "you are copy of jarvis from iron man" in query or "you are copy" in query:
        return random.choice(you_are_copy_reponce)
    elif "you are not as advanced as others" in query or "you are not as advanced" in query:
        return random.choice(not_advance_other_reponce)
    elif query in dumb_responses:
        return random.choice(dumb_responses[query])
    elif query == "set timer":
        return set_timer(query)
    elif query == "tell me a fun fact":
        return tell_fun_fact()
    elif query == "roll a dice":
        return roll_dice()
    elif query == "flip a coin" or query == "flip the coin":
        return flip_coin()
    elif query == "tell me a riddle":
        return tell_riddle()
    elif "play rock paper scissors" in query:
        return play_rock_paper_scissors(query)
    elif query == "tell me a story" or query =="tell story":
        return tell_story()
    elif query == "tell me a quote":
        return tell_quote()
    else:
        print(query)
        return "sorry i cant do that i am still learning"
        # return search_web(query)

def greet_user():
    """Return a greeting based on the time of day."""
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning! "
    elif 12 <= current_hour < 18:
        return "Good afternoon! "
    else:
        return "Good evening! "
    
def openWebsite(url):
    """Open a website in the browser"""
    webbrowser.open(url)

def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%H:%M")
    return f"The current time is {current_time}."

def tell_date():
    """Tell the current date."""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    return f"Today is {current_date}."

def open_wikipedia(query):
    """Fetch a summary from Wikipedia."""
    search_term = query.replace("wikipedia", "").strip()
    try:
        summary = wikipedia.summary(search_term, sentences=3)
        return f"According to Wikipedia: {summary}"
    except wikipedia.exceptions.DisambiguationError:
        return f"There were multiple results for {search_term}. Please be more specific."
    except wikipedia.exceptions.HTTPTimeoutError:  # Fix here
        return "There was an issue with Wikipedia. Please try again later."
    except wikipedia.exceptions.WikipediaException:  # Catch all Wikipedia-related errors
        return "An error occurred while fetching data from Wikipedia."
    except Exception:
        return f"Sorry, I couldn't find any information on {search_term}."

def tell_joke():
    """Get a random joke using pyjokes."""
    return pyjokes.get_joke()

def open_website(query):
    """Open a website in the default web browser."""
    query = query.lower().replace("open", "").replace("website", "").strip()

    # If the user provides only the website name, append 'https://www.'
    if not query.startswith("http"):
        url = f"https://www.{query}.com"
    else:
        url = query

    webbrowser.open(url)
    return f"Opening {url}..."

def lock_pc():
    """Lock the user's PC."""
    if platform.system().lower() == 'windows':
        os.system('rundll32.exe user32.dll,LockWorkStation')
        return "Your computer is now locked."

def open_app(query):
    """Open an application on the PC."""
    app_name = query.replace("open app", "").strip()
    app_paths = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "spotify": "C:\\Users\\user_name\\AppData\\Roaming\\Spotify\\Spotify.exe",
        "vs code":"C:\\Users\\user_name\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    }
    
    if app_name in app_paths:
        try:
            subprocess.Popen(app_paths[app_name])
            return f"Opening {app_name}."
        except Exception as e:
            return f"Failed to open {app_name}. Error: {str(e)}"
    else:
        return f"Application '{app_name}' not found in the list."
    
def tell_good_morning():
    """Returns a good morning message with a motivational quote and the day's reminders."""
    quote = random.choice(MOTIVATIONAL_QUOTES)
    reminders = get_reminders_for_today()
    date=datetime.datetime.now().strftime("%A,%d,%B, %Y")
    day=datetime.datetime.now().strftime("%j")
    if reminders:
        return f"Good morning!\n day{day} out of 365 \n{quote}\nHere are your reminders for today:\n{reminders}\nToday Is {date}"
    else:
        return f"Good morning! \n{quote}\nYou have no reminders for today."

def tell_good_night():
    """Returns a good night message with a relaxing quote or joke and a sleep suggestion."""
    quote = random.choice(GOOD_NIGHT_QUOTES)
    day=datetime.datetime.now().strftime("%j")
    return f"Good night! \n{quote}\n you succefully wasted {day} day of 365 days \n"

def get_weather(query):
    """Fetch weather information using Open-Meteo API."""
    latitude, longitude = 23.0225, 72.5714
    
    openmeteo = openmeteo_requests.Client()
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
        "forecast_days": 1
    }
    
    try:
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        
        # Extract current temperature
        current = response.Current()
        current_temperature_2m = round(current.Variables(0).Value())
        
        return f"The current temperature is {current_temperature_2m}°C."
    except Exception as e:
        return f"Failed to fetch weather. Error: {str(e)}"

def get_news():
    """Fetch the latest news headlines."""
    try:
        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=your_newsapi_key"
        response = requests.get(url).json()
        if response.get("status") != "ok":
            return "Could not fetch news."
        headlines = [article["title"] for article in response["articles"][:5]]
        return "Here are the latest news headlines: " + ". ".join(headlines)
    except Exception as e:
        return f"Failed to fetch news. Error: {str(e)}"

def set_reminder(query):
    """Sets a reminder for a specific day."""
    reminder_text = query.replace("remind me", "").strip()
    
    if not reminder_text:
        return "Please specify what you want to be reminded about."

    # Ask for the day
    day = input("For which day should I set this reminder? (e.g., today, tomorrow, or a date like 2025-02-10): ").strip().lower()

    if day in ["today", "tomorrow"]:
        reminder_date = (datetime.date.today() if day == "today" else datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        try:
            reminder_date = datetime.datetime.strptime(day, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."

    # Save reminder
    with open("reminders.txt", "a") as f:
        f.write(f"{reminder_date}: {reminder_text}\n")
    
    return f"Reminder set for {reminder_date}: {reminder_text}"

def get_reminders_for_today():
    """Fetch reminders for today."""
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    reminders = []
    
    try:
        with open("reminders.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith(today_date):
                    reminders.append(line.strip().split(": ", 1)[1])
    except FileNotFoundError:
        return "No reminders found."

    return "\n".join(reminders) if reminders else "No reminders for today."

def send_email(query):
    """Send an email using Gmail."""
    try:
        recipient = query.replace("send email to", "").strip()
        if not recipient:
            return "Please specify a recipient."
        subject = "Subject from JARVIS"
        body = "This is an automated email sent by JARVIS."
        
        msg = MIMEMultipart()
        msg["From"] = GMAIL_USER
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(msg)
        return f"Email sent to {recipient}."
    except Exception as e:
        return f"Failed to send email. Error: {str(e)}"
        
def playMusic():
    """Play music from a predefined directory"""
    music_dir = "D:\Collage Project\Jarvis\Jarvis\jarvis_project\music"  # Update to your music directory path
    songs = os.listdir(music_dir)
    print(songs) 
    os.startfile(os.path.join(music_dir, songs[1]))
    
def get_system_info():
    """Get system information."""
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    return f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%, Disk Usage: {disk_usage}%."

def preprocess_expression(query):
    """Convert natural language phrases into valid mathematical operators and rearrange sentences."""
    # Replace common natural language phrases with mathematical operators
    replacements = {
        "divide": "/",
        "divided by": "/",
        "multiply": "*",
        "multiplied by": "*",
        "into": "*",
        "times": "*",
        "plus": "+",
        "minus": "-",
        "modulo": "%",
        "square root of": "sqrt",
        "power": "**",
        "raised to": "**",
    }

    # Replace phrases in the query
    for phrase, operator in replacements.items():
        query = query.replace(phrase, operator)

    # Rearrange sentences to standard mathematical format
    # Example: "divide 2 by 2" -> "2 / 2"
    if "by" in query:
        parts = query.split("by")
        if len(parts) == 2:
            numerator = parts[0].strip()
            denominator = parts[1].strip()
            query = f"{numerator} / {denominator}"

    # Remove any non-mathematical words or characters
    query = "".join([char for char in query if char in "0123456789+-*/().% sqrt"])

    return query.strip()

def calculate(query):
    """Perform a mathematical calculation using sympy."""
    # Preprocess the query to handle natural language phrases
    expression = preprocess_expression(query.replace("calculate", "").strip())

    try:
        # Parse and evaluate the expression safely
        result = sympify(expression)
        return f"The result of '{expression}' is {result}."
    except SympifyError:
        return "Error: Invalid mathematical expression. Please provide a valid input."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return f"Failed to calculate. Error: {str(e)}"

def translate_text(query):
    """Translate text to a specified language."""
    # You can integrate a translation API like Google Translate here.
    return "Translation functionality is not yet implemented."

def take_screenshot(save_path="C:/Users/Asus/Desktop/screenshot.png"):
    """Take a screenshot and save it to the specified path."""
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        # Capture the screenshot
        screenshot = pyautogui.screenshot()
        # Save the screenshot to the specified path
        screenshot.save(save_path)
        return f"Screenshot taken"
    except Exception as e:
        return f"Failed to take screenshot. Error: {str(e)}"

def search_file(query):
    """Search for a file on the system."""
    file_name = query.replace("search file", "").strip()
    if not file_name:
        return "Please specify a file name."
    # Implement file search logic here
    return f"Searching for file: {file_name}."

def open_folder(query):
    """Open a specific folder on the PC."""
    folder_name = query.replace("open folder", "").strip()
    if not folder_name:
        return "Please specify a folder name."
    # Implement folder opening logic here
    return f"Opening folder: {folder_name}."

def shutdown_pc():
    """Shut down the PC."""
    if platform.system().lower() == 'windows':
        os.system("shutdown /s /t 1")
        return "Shutting down your computer."
    else:
        return "Shutdown is only supported on Windows."

def restart_pc():
    """Restart the PC."""
    if platform.system().lower() == 'windows':
        os.system("shutdown /r /t 1")
        return "Restarting your computer."
    else:
        return "Restart is only supported on Windows."

def check_battery():
    """Check the laptop's battery status."""
    if not hasattr(psutil, "sensors_battery"):
        return "Battery information is not available."
    battery = psutil.sensors_battery()
    if battery is None:
        return "No battery detected."
    return f"Battery is at {battery.percent}%."

def set_volume_percentage(query):
    """Set the system volume to a specific percentage."""
    try:
        CoInitialize()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        
        # Extract the volume percentage from the query (e.g., "set volume to 50%")
        if 'set volume to' in query:
            percentage = query.replace('set volume to', '').replace('%', '').strip()
            try:
                percentage = float(percentage)
                # Clamp the value between 0 and 100
                percentage = max(0, min(100, percentage))
                volume.SetMasterVolumeLevelScalar(percentage / 100.0, None)
                return f"Volume set to {percentage}%. "
            except ValueError:
                return "Sorry, I couldn't understand the volume percentage."
        return "Please specify the volume percentage you want to set."
    finally:
        CoUninitialize()

def increase_brightness():
    """Increase screen brightness by 10%."""
    try:
        current_brightness = sbc.get_brightness(display=0)  # Get current brightness
        if isinstance(current_brightness, list):  
            current_brightness = current_brightness[0]  # Take first value if it's a list
        
        # print(f"Current brightness: {current_brightness}")  # Debug statement
        
        if isinstance(current_brightness, int):
            new_brightness = min(current_brightness + 10, 100)  # Increase by 10%, max 100%
            sbc.set_brightness(new_brightness, display=0)  # Set new brightness
            return f"Brightness increased to {new_brightness}%."
        else:
            return "Unable to get current brightness."
    except Exception as e:
        return f"Failed to increase brightness. Error: {str(e)}"

def decrease_brightness():
    """Decrease screen brightness by 10%."""
    try:
        current_brightness = sbc.get_brightness(display=0)  # Get current brightness
        if isinstance(current_brightness, list):  
            current_brightness = current_brightness[0]  # Take first value if it's a list
        
        # print(f"Current brightness: {current_brightness}")  # Debug statement
        
        if isinstance(current_brightness, int):
            new_brightness = max(current_brightness - 10, 0)  # Decrease by 10%, min 0%
            sbc.set_brightness(new_brightness, display=0)  # Set new brightness
            return f"Brightness decreased to {new_brightness}%."
        else:
            return "Unable to get current brightness."
    except Exception as e:
        return f"Failed to decrease brightness. Error: {str(e)}"
import screen_brightness_control as sbc

def set_brightness_percentage(query):
    """Set the screen brightness to a specific percentage based on voice query."""
    try:
        # Remove unnecessary words and extract the number
        query = query.lower().replace("set brightness to", "").replace("%", "").strip()
        words = query.split()  # Split into words
        
        for word in words:
            if word.isdigit():  # Check if word is a number
                percentage = int(word)
                
                # Clamp the value between 0 and 100
                percentage = max(0, min(100, percentage))
                
                # Set brightness
                sbc.set_brightness(percentage)
                return f"Brightness set to {percentage}%."
        
        return "Please specify a valid brightness percentage."
    
    except Exception as e:
        return f"Failed to set brightness. Error: {str(e)}"
    
def open_website(query):
    """Open a website in a new browser tab."""
    try:
        words = query.lower().split()
        for word in words:
            if "." in word:  # Detects domain names (like google.com)
                url = f"https://{word}" if not word.startswith("http") else word
                webbrowser.open(url)  # Open in a new tab
                return f"Opening {url}."
        return "Could not detect a valid website."
    except Exception as e:
        return f"Error opening website: {str(e)}"

def close_tab():
    """Closes the current browser tab using a keyboard shortcut."""
    try:
        pyautogui.hotkey("ctrl", "w")  # Close current tab
        return "Tab closed."
    except Exception as e:
        return f"Error closing tab: {str(e)}"

def switch_tab(next_tab=True):
    """Switch between browser tabs (next or previous)."""
    try:
        if next_tab:
            pyautogui.hotkey("ctrl", "tab")  # Move to next tab
            return "Switched to next tab."
        else:
            pyautogui.hotkey("ctrl", "shift", "tab")  # Move to previous tab
            return "Switched to previous tab."
    except Exception as e:
        return f"Error switching tab: {str(e)}"
    
def search_web(query):
    """Search Google using SerpAPI and return the top result."""
    params = {
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": ""
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "organic_results" in results and results["organic_results"]:
        return f"According to Google: {results['organic_results'][0]['snippet']}"
    else:
        return "I couldn't find a direct answer. Opening Google for you."