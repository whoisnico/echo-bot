import disnake
from disnake.ext import commands
import datetime

class UserInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def userinfo(self, ctx, member: disnake.Member = None):
        member = member or ctx.author

        embed = disnake.Embed(title="User Info", color=0x2F3136)
        embed.set_thumbnail(url=member.avatar.url)

        embed.add_field(name="Username", value=member.name, inline=True)
        if member.display_name is not None:
            embed.add_field(name="Displayname", value=member.display_name, inline=False)
        embed.add_field(name="Status", value=member.status.name.capitalize(), inline=False)
        embed.add_field(name="User ID", value=member.id, inline=False)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%b %d, %Y "), inline=False)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%b %d, %Y"), inline=False)
        
        if member.activity is not None:
            activity_type = member.activity.type.name.capitalize()
            if activity_type == "Playing":
                embed.add_field(name="Currently Playing", value=member.activity.name, inline=False)
            elif activity_type == "Streaming":
                embed.add_field(name="Currently Streaming", value=member.activity.name, inline=False)
                embed.add_field(name="Stream URL", value=member.activity.url, inline=False)
            elif activity_type == "Listening":
                embed.add_field(name="Currently Listening", value=member.activity.title, inline=False)
                embed.add_field(name="Artist", value=member.activity.artist, inline=True)
                embed.add_field(name="Album", value=member.activity.album, inline=True)
            elif activity_type == "Watching":
                embed.add_field(name="Currently Watching", value=member.activity.name, inline=False)

        user_flags = member.public_flags.all()
        if user_flags:
            
            badge_emojis = {
                "staff": "<:8485discordemployee:1134516315709771827> ",
                "partner": "<:6714discordpartner:1134514894482444369>",
                "hypesquad": "<:3809discordhypesquad:1134514888262299658>",
                "bug_hunter": "<:7732discordbughunterlv1:1134514896978067536> ",
                "hypesquad_bravery": "<:1247discordbravery:1134514880003723304>",
                "hypesquad_brilliance": "<:1350discordbrillance:1134514882000191619>",
                "hypesquad_balance": "<:5946discordbalance:1134514892972494889>",
                "early_supporter": "<:3121discordearlysupporter:1134514886660079696>",
                "system": "<:3965_system_badge:1134514889545748502>",
                "bug_hunter_level_2": "<:7904discordbughunterlv2:1134514898693541989> ",
                "verified_bot": "<:8207bottag:1134514901679878245>",
                "verified_bot_developer": "<:earlydev:1134524462751039508>",
                "early_verified_bot_developer": "<:earlydev:1134524462751039508>",
                "moderator_programs_alumni": "<:mpa:1134525752310763651>",
                "discord_certified_moderator": "<:9765badgemoderators:1134526352859607105>",
                "http_interactions_bot": "<:9435blurplebot:1134528790115135628> ",
                "spammer": "<:3965_system_badge:1134514889545748502>",
                "active_developer": "<:ad:1134516375134666752>"
            }

            flags_text = "\n".join(f"{badge_emojis[flag.name]} {flag.name.replace('_', ' ').title()}" for flag in user_flags)
            if member.bot == True:
                flags_text + "\n <:9435blurplebot:1134528790115135628>  Discord Bot"
            embed.add_field(name="Profile Badges", value=flags_text, inline=False)
        else:
            if member.bot == True:
                embed.add_field(name="Profile Badges", value="<:9435blurplebot:1134528790115135628>  Discord Bot", inline=False)



        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UserInfoCog(bot))
