import discord
import markovify

with open("doge2.txt",encoding="utf-8") as f:
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
        text_model = markovify.Text(text)
        response = text_model.make_short_sentence(350)
        while not response:
            response = text_model.make_short_sentence(350)
        responseL = '!'.join(response.split('.')).split('!')
        await message.channel.send('\n'.join(responseL[:3])+'\nif u want halp say bork bork i want help or something similar')
        
    except Exception as err:
        await message.channel.send("Error: {}".format(err))
    

client.run('NjI2OTA3MDExNDM0NTQ1MTYz.XY07HQ.Nx8z0oMZSb-r9YEr2G7hApr9EFo')
