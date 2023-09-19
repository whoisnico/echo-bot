import disnake
from disnake.ext import commands

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            activity=disnake.Activity(
                type=disnake.ActivityType.playing,
                name="being fresh"
            ),
            status=disnake.Status.online
        )
        

def setup(bot):
    bot.add_cog(OnReady(bot))