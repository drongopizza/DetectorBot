import discord
import json
import asyncio
import fileinput
from discord.ext import commands

debug = True # Runs debug commands when 'true'
TOKEN = 'NTgxMDM2MjAzNTE2ODg3MDQx.XOcazA.q3RDvvS1AnHWedxDEPzUjeHfitQ' # User token for the bot

detector = commands.Bot(command_prefix="$", description='k') # Sets command prefix for bot


with open("wordlist.txt", "r+") as f:
    wordlist = f.read()


# with open("wordlist.txt", "r+") as f:
#     for line in f:
#         if not line.isspace():
#             f.write(line)

@detector.event
async def on_ready(): 
    print("--------")
    print("Bot is online")
    print(detector.user.name)
    print(detector.user.id)
    print("--------")
    game = discord.Game("with VSCode")
    await detector.change_presence(status=discord.Status.online, activity=game) # Sets the "Playing: " on discord


@detector.event
async def on_message(message):
    
    if message.author == detector.user: # Don't change unless you're retarded
        return

    for i in wordlist: # Checks messages for matches in the wordlist.txt file
        if not (message.content.find(i) == -1):
            if debug: 
                await message.channel.send("Word found.")

    await detector.process_commands(message) # Processes all commands - DO NOT TOUCH

@detector.command()
async def add(ctx, wd): # Use $add (word) to add words to the wordlist
    if wd in wordlist:
        await ctx.send("You have already added that word.") # Checks if the word is already in the wordlist
    else:
        with open("wordlist.txt", "a") as f:
            f.seek(0, 0)
            f.write(wd + ",")
        if debug: await ctx.send("Word added.") 
    return

@detector.command()
async def remove(ctx, wd): # Use the $remove to remove a word from the wordlist
    with open("wordlist.txt") as f:
        f.seek(0, 0)
        f.read()
        remw = f.read().replace(wd + ",", '')
    if wd not in wordlist: # Detects if the word is in the wordlist
        await ctx.send("That word hasn't been added.")
    else:
        with open("wordlist.txt", "w") as f:
            f.write(remw)
            
    
    

    #read = json.loads(open("words.json").read())
    #write = json.dump("words.json", "words.json")

    



detector.run(TOKEN)