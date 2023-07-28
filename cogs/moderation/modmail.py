import datetime
import json
import disnake
from disnake.ext import commands
with open("config.json") as file:
    config = json.load(file)
    guildID = config["guild"]

class ModmailCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if isinstance(message.channel, disnake.DMChannel):

            guild = self.bot.get_guild(guildID)
            modmail_channel = disnake.utils.get(guild.text_channels, name="modmail")
            if modmail_channel:
                embed = disnake.Embed(title=f"Modmail - {message.author}", description=message.content, color=0x2F3136, timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=message.author.avatar.url)
                embed.set_footer(text=f"ID: {message.author.id}")
                await modmail_channel.send(embed=embed)
            else:
                await message.author.send("Es gibt kein Modmail-Kanal auf diesem Server.")
    
    @commands.slash_command()
    @commands.has_permissions(moderate_members=True)
    async def mod_answer(self, inter, answer_id: str, message: str):
        user = await inter.bot.fetch_user(answer_id)
        if user:
            embed = disnake.Embed(title=f"Modmail - Staff Reply", description=message, color=0x2F3136, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=inter.author.avatar.url)
            embed.set_footer(text=f"Staff . {inter.author}")
            await user.send(embed=embed)
            await inter.send(f"DM was successfull!")
        else:
            await inter.send("User not found!")
        
    @mod_answer.error
    async def mod_error(self, inter: disnake.ApplicationCommandInteraction, error: Exception) -> None:
        if isinstance(error, commands.MissingPermissions):
            return await inter.response.send_message("This is a **Staff** only command!", ephemeral=True)


def setup(bot):
    bot.add_cog(ModmailCog(bot))