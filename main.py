import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
bottoken = "UNESI TOKEN OVDJE" #kad saveas na github ne zaboravi izbrisat token odavde

@bot.event
#ova funkcija nam govori da je bot spreman i da se uspjesno povezao na discord server, i ispisuje nam poruku u konzoli sa imenom bota
async def on_ready():
    print(f"Logged in as {bot.user}")

#self explanatory, kad netko napise !hello bot ce odgovoriti sa "pop je gej"
@bot.command()
async def hello(ctx):
    await ctx.send("pop je gej")

bot.run(bottoken)
