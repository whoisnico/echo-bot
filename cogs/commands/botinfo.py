import time
import disnake
from disnake.ext import commands
import datetime
import psutil



class BotInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def botinfo(self, inter):
        current_time = time.time()
        uptime_seconds = int(current_time - self.bot.start_time)

        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        embed = disnake.Embed(title="Echo Bot Info", 
                              color=0x2F3136, 
                              timestamp=datetime.datetime.utcnow(),
                              description=f"UpTime - {days}d, {hours}h {minutes}m \n Bot Name - {self.bot.user.name} \n Status - {self.bot.status.name.capitalize()} \n [GitHub](https://github.com/whoisnico/echo-bot) - [Documentation](https://whoisnico.github.io/echo-bot/) - [Support](https://discord.gg/KJs5jM7JTa)")
        
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text="copyright by github.com/whoisnico")
        await inter.send(embed=embed)
 

def setup(bot):
    bot.add_cog(BotInfoCog(bot))
