# JCD

This is an extremely simple Discord bot used to save messages from a specific channel to a json file.

To use the bot have discord.py installed, create a config.py and put your token in as "TOKEN = "YOUR TOKEN HERE" "
you can then run main.py.

To change the channel which it saves from change the message.channel.id to whatever channel ID you want.
You can get the channel ID by enabling developer mode in Discord and right clicking a channel and selecting "Copy Channel ID"

It will save the messages to a json file in the codes directory, that can be changed at the "save_to_json" function.
