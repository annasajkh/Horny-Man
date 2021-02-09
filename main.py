import discord
from discord.ext import commands
from udpy import UrbanClient
import random
from googlesearch import search
from gtts import gTTS
import os
import api
from googletrans import Translator
import magic8ball

translator = Translator()
client = UrbanClient()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Logged on as {0}!".format(bot.user))

@bot.command(name="affirmation")
async def _affirmation(ctx):
    try:
        await ctx.send(api.get_affirmation())
    except Exception as e:
        await ctx.send(e)

@bot.command(name="ask")
async def _ask(ctx,question):
    try:
        await ctx.send(random.choice(magic8ball.list))
    except Exception as e:
        await ctx.send(e)

@bot.command(name="quote")
async def _quote(ctx):
    try:
        await ctx.send(api.get_quote())
    except Exception as e:
        await ctx.send(e)

@bot.command(name="translate")
async def _translate(ctx,text):
    try:
        result = translator.translate(text)
        await ctx.send(result.text)
    except Exception as e:
        await ctx.send(e)

@bot.command(name="advice")
async def _advice(ctx):
    try:
        await ctx.send(api.get_advice())
    except Exception as e:
        await ctx.send(e)

@bot.command(name="numfact")
async def _numfact(ctx,num):
    try:
        await ctx.send(api.get_number_fact(num))
    except Exception as e:
        await ctx.send(e)

@bot.command(name="search")
async def _search(ctx,text,num_results):
    try:
        result = search(text,num_results=int(num_results))
        if len(result) > int(num_results):
            result.pop(len(result) - 1)
        string_result = ""
        for i in result:
            if "http" in i:
                string_result += i +'\n'
        await ctx.send(string_result)
    except Exception as e:
        await ctx.send(e)

@bot.command(name="urbandict")
async def _urbandict(ctx, xterm):
    try:
        result = client.get_definition(xterm)
        if len(result) == 0:
            await ctx.send("sorry i can't find any information about" + xterm)
        else:
            await ctx.send(result[random.randrange(0,len(result))].definition.replace("[","").replace("]",""))
    except Exception as e:
        await ctx.send(e)

@bot.command(name="say")
async def _say(ctx, text):
    try:
        tts = gTTS(text)
        tts.save("sound.mp3")
        await ctx.send(file=discord.File("sound.mp3"))
        os.remove("sound.mp3")
    except Exception as e:
        await ctx.send(e)

@bot.command(name="randomimg")
async def _randomimg(ctx,width,height):
    try:
        w = int(width)
        h = int(height)
        if w > 1000 or h > 1000:
            raise Exception("width and height has to be less or equal to 1000")
        api.get_random_image(w,h)
        await ctx.send(file=discord.File("img.png"))
        os.remove("img.png")
    except Exception as e:
        await ctx.send(e)

file = open("token.txt","r")
token = file.read()
file.close()
bot.run(token)