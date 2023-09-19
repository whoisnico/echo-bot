import time
import disnake
from disnake.ext import commands
import datetime
import psutil
import requests
from disnake.utils import parse_time


class BotInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def botinfo(self, inter):
        
        api_url = f'https://api.github.com/repos/whoisnico/echo-bot/commits?per_page=1'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            
            if data:
                last_push_unix = data[0]['commit']['committer']['date']
                last_push_struct_time = time.strptime(last_push_unix, "%Y-%m-%dT%H:%M:%SZ")
                last_push_unix_seconds = int(time.mktime(last_push_struct_time))
                
            else:
                last_push = "Not Found"
                
        except requests.exceptions.RequestException as e:
            last_push = "Error"
        
        current_time = time.time()
        uptime_seconds = int(current_time - self.bot.start_time)

        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        embed = disnake.Embed(title="Echo Bot Info", 
                              color=0x2F3136, 
                              timestamp=datetime.datetime.utcnow(),
                              description=f"UpTime - {days}d, {hours}h {minutes}m \n Bot Name - {self.bot.user.name} \n Bot ID - {self.bot.user.id}\n Status - {self.bot.status.name.capitalize()} \n Ping - {round(self.bot.latency * 1000)}ms\n Servers - {len(self.bot.guilds)}\n Last Update - <t:{last_push_unix_seconds}:R> \n [GitHub](https://github.com/whoisnico/echo-bot) - [Documentation](https://whoisnico.github.io/echo-bot/) - [Support](https://discord.gg/KJs5jM7JTa)")
        
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text="copyright by github.com/whoisnico")
        await inter.send(embed=embed)
 

def setup(bot):
    bot.add_cog(BotInfoCog(bot))
