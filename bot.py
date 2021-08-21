import discord
import os
from discord.ext import commands
import TwitterSentiments as TS

client = commands.Bot(command_prefix="$",help_command=None)

@client.event
async def on_ready():
    print("Bot is ready.")

#User events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(name="help")
async def help(context):
    myEmbed = discord.Embed(title="Commands", description="Find out what twitter thinks about your stock and run a real-time stock analysis!")
    await context.send(embed=myEmbed)
'''
@client.command(name="gender")
async def calculate_percentage(ctx):

    await ctx.send('Enter your height (CM): ')
    message_response = client.wait_for('message', check='check')
    height = await int(message_response.content)

    await ctx.send('Enter your weight (KG): ')
    message_response = client.wait_for('message', check='check')
    weight = await int(message_response.content)

    await ctx.send('Enter your shoe size (US): ')
    message_response = client.wait_for('message', check='check')
    shoe_size = await int(message_response.content)

    #Calculations
    predicted_gender = classifier.main_function([[height, weight, shoe_size]])

    await ctx.send(f"Your gender according to the classifier is {predicted_gender}!")
'''

@client.command(name="stock")
async def calculate_percentage(ctx):

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    await ctx.send('Enter ticker symbol: ')
    msg = client.wait_for('message', check=check)
    ticker = str(message_response.content).upper()

    await ctx.send(f'Your ticker is {ticker}')


@client.command(name="shutdown")
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()
#Classified token
if __name__ == '__main__':
    client.run("ODc4NzU2MjEzNzI1MjE2Nzg5.YSFzfw.o27dpif4fjXPmZ1Ft9Sg0A-tVRA")
