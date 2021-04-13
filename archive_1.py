import discord
from discord.ext import commands
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']  # Bot_token
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)
bot_states_msg = "playing"


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(bot_states_msg))
    print("ready")


@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    channel = guild.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    DM_msg = discord.Embed(description=f"{payload.emoji.name}リアクションが届いています。宜しければお返事お願いします。")
    if payload.member != message.author:
        if payload.channel_id == 791047604347076668 or payload.channel_id == 827843443765149706 or payload.channel_id == 827843103549423626:
            DM_msg.set_author(name=payload.member, icon_url=payload.member.avatar_url)
            DM_msg.add_field(name="メッセージ内容", value=message.content)
            await message.author.send(embed=DM_msg)
            await message.remove_reaction(payload.emoji, payload.member)
            print(message.content)


bot.run(TOKEN)
