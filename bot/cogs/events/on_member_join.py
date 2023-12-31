import datetime
import disnake
from disnake.ext import commands

class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1006156818579472505)
        guild = member.guild
        icon_url = guild.icon.url
        name = guild.name

        embed = disnake.Embed(
            title=name, 
            description=f"Welcome {member.mention}! \n You're the member number {len(list(member.guild.members))}.", 
            color=0x2F3136, 
            timestamp=datetime.datetime.utcnow()) 
        embed.set_image(url=f"{member.avatar.url}")
        embed.set_footer(text=name, 
                         icon_url=icon_url)
        
        await channel.send(embed=embed)
        

def setup(bot):
    bot.add_cog(OnMemberJoin(bot))