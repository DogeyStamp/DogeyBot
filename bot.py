import discord
import markovify

with open("doge.txt",encoding="utf-8") as f:
    text = f.read()
text_model = markovify.Text(text)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.content.lower()[:5] != "bork ":
        return
    try:
        response = text_model.make_sentence()
        while not response:
            response = text_model.make_sentence()
        await message.channel.send(text_model.make_sentence())
        
    except Exception as err:
        await message.channel.send("Error: {}".format(err))
    

client.run('NjI2OTA3MDExNDM0NTQ1MTYz.XY07HQ.Nx8z0oMZSb-r9YEr2G7hApr9EFo')