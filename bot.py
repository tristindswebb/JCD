import discord
from config import TOKEN
import json

intents = discord.Intents.default()
intents.message_content = True

def save_to_json(data):
    with open('messages.json', 'a') as file:
        json.dump(data, file, indent=2)
        file.write('\n')

def run_bot():
    intents.message_content = True
    client = discord.Client(intents=intents)
    @client.event
    async def on_ready():
        print(f"{client.user} is now running")
        for guild in client.guilds:
            print(f'Guild Name: {guild.name}')
            print(f'Guild ID: {guild.id}')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        message_data = {
        'author': str(message.author),
        'content': message.content,
        'timestamp': str(message.created_at),
        }
        if message.channel.id == 887771482992824353:
            save_to_json(message_data)
        else:
            print("fat animal wrong channimal")

        

        print(f"{message.author} said: '{message.content}' in ({message.channel})")

    
    client.run(TOKEN)