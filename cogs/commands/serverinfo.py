import disnake
from disnake.ext import commands

class ServerInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        invite = await guild.text_channels[0].create_invite()
        invite_url = invite.url
        button = disnake.ui.Button(
            style=disnake.ButtonStyle.url,
            label="Generate Invite Link",
            url=invite_url
        )

        embed = disnake.Embed(title="Server Info", color=0x2F3136)
        embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Server ID", value=guild.id, inline=False)
        embed.add_field(name="Owner", value=guild.owner.mention, inline=False)
        embed.add_field(name="Creation Date", value=guild.created_at.strftime("%b %d, %Y"), inline=False)
        embed.add_field(name="Verification Level", value=str(guild.verification_level).capitalize(), inline=False)
        embed.add_field(name="Member Count", value=guild.member_count, inline=False)

        if guild.premium_tier > 0:
            embed.add_field(name="Boost Level", value=f"Level {guild.premium_tier}", inline=False)
            embed.add_field(name="Boost Count", value=guild.premium_subscription_count, inline=False)

        if guild.features:
            features_text = "\n".join(feature.replace("_", " ").title() for feature in guild.features)
            embed.add_field(name="Server Features", value=features_text, inline=False)
            
        view = disnake.ui.View()
        view.add_item(button)

        await ctx.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(ServerInfoCog(bot))
