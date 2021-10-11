# bot.py
import os
import random
import discord
import asyncio
import dotenv
import time
import datetime

from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix = "§")

@client.command(name = 'nick', help = 'Změní nick')
@commands.has_role("XeloR")
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Přezdívka změněna {member.mention} .')

@client.command(name = "mute", help = "Ztlumení")
@commands.has_role("XeloR")
async def mute(ctx, member : discord.Member):
        await member.edit(mute=True)

@client.command(name = 'ping', help = 'Uveď koho a kolikrát. (Maximu je 10)')
@commands.has_role("XeloR")
async def ping(ctx, member : discord.Member, pocet : int):
    i = 0;
    if pocet > 10:
        await ctx.send("Limit je 10.")
    while(i < pocet <11):
        await ctx.send(member.mention + " byl jsi povolán.")
        pocet = pocet - 1

@client.command(name= 'bonk', help = 'Go to horny jail. (Zvol někoho)')
@commands.has_role("XeloR")
async def bonk(ctx, member : discord.Member):
    await ctx.send(file = discord.File("bonk.png"))
    await ctx.send(member.mention + " Go to horny jail.")

@client.command(name = 'pepejam', help = 'Pepejam.')
@commands.has_role("XeloR")
async def pepejam(ctx):
    await ctx.send(file = discord.File("pepejam.gif"))

@client.command(name = 'steal', help = '§steal jméno')
@commands.has_role("XeloR")
async def steal(ctx, member : discord.Member):
    guild = ctx.guild;
    cil = ctx.author.voice.channel;
    await member.move_to(cil)
    await ctx.send(member.mention + " Byl jsi ukraden.")

@client.command(name = 'poke', help = '§poke jméno')
@commands.has_role("XeloR")
async def move(ctx, member : discord.Member):
    guild = ctx.guild;
    puvodni = ctx.author.voice.channel;

    if ctx.guild == client.get_guild(519891641482346508):
        bot_room_1 = client.get_channel(775384867814768670)
        bot_room_2 = client.get_channel(775384993886765056)

    if ctx.guild == client.get_guild(706262543500312596):
        bot_room_1 = client.get_channel(706262774983950428)
        bot_room_2 = client.get_channel(706262877639540828)

    i = 0;
    while i < 5 :
        i = i + 1
        await member.move_to(bot_room_1)
        await member.move_to(bot_room_2)
    await member.move_to(puvodni)

@client.command(name = 'stronk', help = 'I am Stronk.')
@commands.has_role("XeloR")
async def stronk(ctx):
    await ctx.send(file = discord.File("stronk.jpeg"))
    await ctx.send("I am Stronk.")

@client.command(name = 'stonks', help = 'Big Stonks.')
@commands.has_role("XeloR")
async def stonks(ctx):
    await ctx.send(file = discord.File("stonks.jpg"))
    await ctx.send("Big Stonks.")

@client.command(name = 'XeloR')
@commands.has_role("XeloR")
async def XeloR(ctx):
    await ctx.reply("Volal jsi mne mistře?")

@client.command(name = 'clear', help = 'Vymaže určitý počet zpráv. (limit 100)')
@commands.has_role("XeloR")
async def clear(ctx, pocet: int):
    if 1 < pocet <= 100 or pocet == 1:
        if pocet == 1:
            await ctx.message.delete()
            smazano = await ctx.channel.purge(limit=1000)
            await ctx.send("Smazal jsem: vše", delete_after=5)
            print(f"Smazal jsem: {len(smazano)} zpráv");

        await ctx.message.delete()
        smazano = await ctx.channel.purge(limit=pocet)
        await ctx.send(f"Smazal jsem: {len(smazano)} zpráv", delete_after=5)
        print(f"Smazal jsem: {len(smazano)} zpráv");
    else:
        await ctx.send("Limit je 100.")

@client.command(name = 'knp', help = 'Kámen, Nůžky, Papír. §knp k/n/p')
@commands.has_role("XeloR")
async def knp(ctx, Vyber_HRAC: str):
    Vyber_PC = random.randint(1,3);
    if Vyber_PC == 1:
        Vyber_PC = "k";
    elif Vyber_PC == 2:
        Vyber_PC = "n";
    else:
        Vyber_PC = "p";

    if Vyber_HRAC == "k" or Vyber_HRAC == "n" or Vyber_HRAC == "p":
        if Vyber_HRAC == "k" and Vyber_PC == "n" or Vyber_HRAC == "n" and Vyber_PC == "p" or Vyber_HRAC == "p" and Vyber_PC == "k":
            await ctx.reply("Gratuluji Vyhrál jsi.")
        elif Vyber_HRAC == Vyber_PC:
            await ctx.reply("Remíza")
        elif Vyber_PC == "k" and Vyber_HRAC == "n" or Vyber_PC == "n" and Vyber_HRAC == "p" or Vyber_PC == "p" and Vyber_HRAC == "k":
            if Vyber_PC == "k":
                await ctx.reply("Smolík, prohrál jsi. Bot vybral Kámen.")
            if Vyber_PC == "n":
                await ctx.reply("Smolík, prohrál jsi. Bot vybral Nůžky.")
            if Vyber_PC == "p":
                await ctx.reply("Smolík, prohrál jsi. Bot vybral Papír.")
    else:
        await ctx.reply("Neplatná volba.")

@client.command(name = 'ruleta', help = 'Ruská ruleta. §ruleta počet kulek(1-5)')
@commands.has_role("XeloR")
async def ruleta(ctx, naboje: int):
    if naboje > 5:
        await ctx.reply("Máš 6 komor. Co to tu zkoušíš. Počet nábojů byl nastaven na 5.")
        naboje = 5;
    naboj1 = 0;
    naboj2 = 0;
    naboj3 = 0;
    naboj4 = 0;
    naboj5 = 0;

    if naboje == 1:
	       naboj1 = random.randint(1, 6)

    if naboje == 2:
    	while naboj1 == naboj2 or naboj1 == naboj3 or naboj1 == naboj4 or naboj1 == naboj5 or naboj2 == naboj3 or naboj2 == naboj4 or naboj2 == naboj5:
    		naboj1 = random.randint(1, 6)
    		naboj2 = random.randint(1, 6)

    if naboje == 3:
    	while naboj1 == naboj2 or naboj1 == naboj3 or naboj1 == naboj4 or naboj1 == naboj5 or naboj2 == naboj3 or naboj2 == naboj4 or naboj2 == naboj5 or naboj3 == naboj4 or naboj3 == naboj5:
    		naboj1 = random.randint(1, 6)
    		naboj2 = random.randint(1, 6)
    		naboj3 = random.randint(1, 6)

    if naboje == 4:
    	while naboj1 == naboj2 or naboj1 == naboj3 or naboj1 == naboj4 or naboj1 == naboj5 or naboj2 == naboj3 or naboj2 == naboj4 or naboj2 == naboj5 or naboj3 == naboj4 or naboj3 == naboj5 or naboj4 == naboj5:
    		naboj1 = random.randint(1, 6)
    		naboj2 = random.randint(1, 6)
    		naboj3 = random.randint(1, 6)
    		naboj4 = random.randint(1, 6)

    if naboje == 5:
    	while naboj1 == naboj2 or naboj1 == naboj3 or naboj1 == naboj4 or naboj1 == naboj5 or naboj2 == naboj3 or naboj2 == naboj4 or naboj2 == naboj5 or naboj3 == naboj4 or naboj3 == naboj5 or naboj4 == naboj5:
    		naboj1 = random.randint(1, 6)
    		naboj2 = random.randint(1, 6)
    		naboj3 = random.randint(1, 6)
    		naboj4 = random.randint(1, 6)
    		naboj5 = random.randint(1, 6)

    pozice = random.randint(1, 6)
    if pozice == naboj1 or pozice == naboj2 or pozice == naboj3 or pozice == naboj4 or pozice == naboj5:
    	await ctx.reply("Rána prošla přímo skrz!")
    else:
    	await ctx.reply("Jsi v pohodě. Dnes je tvůj šťastný den.")

@client.command(name = 'text', help = 'Převod textu. §text "Tady napiš text" i/b/u/s/spoiler 0/1')
@commands.has_role("XeloR")
async def text(ctx, text : str, typ : str, Schovany : int ):

    if typ == "i":
        text = "_"+text+"_";
    if typ == "b":
        text = "**"+text+"**";
    if typ == "u":
        text = "__"+text+"__";
    if typ == "s":
        text = "~~"+text+"~~";
    if typ == "spoiler":
        text = "||"+text+"||";
        await ctx.message.delete()
    if Schovany == 1 and typ != "spoiler":
        await ctx.message.delete()
    await ctx.send(text)

@ping.error
async def ping_error(ctx, error):
    await ctx.reply("Uveď přesné jméno a počet.")

@bonk.error
async def bonk_error(ctx, error):
    await ctx.reply("Musíš někoho označit.")

@clear.error
async def clear_error(ctx, error):
    await ctx.reply("Zadej číslo. (Limit 100)")

@knp.error
async def knp_error(ctx, error):
    await ctx.reply("Musíš si vybrat k/n/p.")

@ruleta.error
async def ruleta_error(ctx, error):
    await ctx.reply("Musíš specifikovat počet nábojů.")

@text.error
async def text_error(ctx, error):
    await ctx.reply("Nekdě jsi na něco zapomněl.")



@client.event
async def on_message(message):
    if message.channel.name == 'develop' or message.channel.name == 'anime-quiz' or message.author.name == 'chazp246' or message.author.name == 'TeAge' or  message.content == "§clear 10" or message.content == "§clear 50" or message.content == "§clear 100":
        await client.process_commands(message)

client.run(TOKEN)
