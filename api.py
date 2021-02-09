
import requests
import json
import urllib.request

def get_affirmation():
    response = requests.get("https://www.affirmations.dev/")
    return json.loads(response.text)["affirmation"]

def get_number_fact(num):
    response = requests.get(f"http://numbersapi.com/{num}")
    return response.text

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    result = json.loads(response.text)
    return result[0]["q"] + "\n -" + result[0]["a"]

def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    result = json.loads(response.text)
    return result["slip"]["advice"]

def get_random_image(width,height):
    urllib.request.urlretrieve(f"https://picsum.photos/{width}/{height}","img.png")