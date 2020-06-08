import discord
import markovify
import random
import dogeystrings


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.content.lower()[:5] != "bork ":
        return
    try:
        if message.content.find("help") != -1 or message.content.find("halp") != -1:
            await message.channel.send(dogeystrings.helpPrompt)
            return
        with open("dogebase.txt",encoding="utf-8") as f:
            text = f.read().split("\n")
            random.shuffle(text)
            text = '\n'.join(text)
        text_model = markovify.Text(text)
        response = text_model.make_sentence()
        if not response:
            response = ''
        responseL = response.split()
        await message.channel.send(' '.join(responseL[:random.randint(10,45)])+"\n"+random.choice(dogeystrings.helpStrs))
        
    except Exception as err:
        await message.channel.send("Oh noes! I has an error: {}".format(err))
    

client.run(dogeystrings.token)
