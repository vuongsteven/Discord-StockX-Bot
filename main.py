import discord
from stockx import search

token = "" #bot token goes here

client = discord.Client()

# channel_id = "981937387733151804" - Designated channel ID

@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.channel.id != channel_id:
    #     return

    if message.content.split(' ')[0] == '!stockx':
        query = message.content.replace('!stockx ', '')

        item = search(query)

        embedd = discord.Embed(
            title = item['title'],
            url = 'https://stockx.com/' + item['urlKey']
        )
        embedd.set_thumbnail(
            url = item['media']['imageUrl']
        )
        embedd.add_field(
            name= 'Colorway',
            value=item['colorway']
        )
        embedd.add_field (
            name = "Retail Price",
            value = '$' + str(item['retailPrice'])
        )
        embedd.add_field (
            name = 'Last Sale Price',
            value = '$' + str(item['market']['lastSale'])
        )
        embedd.add_field(
            name = 'Minimum Bid',
            value = '$' + str(item['minimumBid'])
        )
        embedd.add_field(
            name = 'Highest Bid',
            value = '$' + str(item['market']['highestBid']),
            inline = True
        )
        embedd.set_footer (
            text = 'dev: nobers'
        )
        await message.channel.send(embed=embedd)

    if message.content == '!stockxhelp':
        embed = discord.Embed (
            title = "**StockX Bot Help**"
        )
        embed.add_field(
            name = "Commands",
            value = "!stockx <name of shoe>"
        )
        embed.set_footer (
            text = 'dev: nobers'
        )
        await message.channel.send(embed = embed)
        
client.run(token)