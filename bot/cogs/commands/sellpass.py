import json
import disnake
from disnake.ext import commands
import datetime

import requests

class SellpassCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command()
    async def setshop_token(self, inter, token: str):
            """Connect your Bot with your Sellpass Account!"""
            try:
                id = inter.guild.id
                authtoken = "Bearer " + token
                data = {
                    "Shop": {
                        "ID": id,
                        "Token": authtoken
                    }
                }
                with open("database/sellpass/shop.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
                
                response = requests.get(f'https://dev.sellpass.io/self/shops', headers={'Authorization': authtoken, 'Content-Type': 'application/json'})
                if response.status_code == 200:
                    data = response.json()["data"]
                    if not data:
                        message = "No Shops found"
                    else:
                        message = "List of shops:\n"
                        for shop in data:
                            name = shop["shop"]["name"]
                            id = shop["shop"]["id"]
                            message += f"Shop ID: {id} - Name: {name}\n"
                else:
                    message = f"Error: {response.status_code}"
            except requests.exceptions.RequestException as e:
                message = f"Request Exception: {e}"
            except json.JSONDecodeError as e:
                message = f"JSON Decode Error: {e}"
            
            embed = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"Your account has been connected! \n {message} \n Select one of your Shops to continue! `/setshop_shopid`")
            embed.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
            await inter.send(embeds=[embed], ephemeral=True)

    @commands.slash_command()
    async def setshop_id(self, inter, shopid: int):
            """Connect your Bot with your Sellpass Shop!"""
            
            try:
                with open("database/sellpass/shop.json", "r") as json_file:
                    data = json.load(json_file)
                    if data:
                        if not "Shop" in data and "Token" in data["Shop"] and "ShopID" in data["Shop"]:
                            error1 = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"**Error:** You have to set first your token & shopid! \n [Click for Help](https://whoisnico.github.io/echo-bot/) | `/setshop_token` | `/setshop_id`")
                            error1.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
                            await inter.send(embed=error1, ephemeral=True)
                            return
                    else:
                        error2 = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"**Error:** You have to set first your token & shopid! \n [Click for Help](https://whoisnico.github.io/echo-bot/) | `/setshop_token` | `/setshop_id`")
                        error2.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
                        await inter.send(embed=error2, ephemeral=True)
                        return
            except:
                error3 = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"**Error:** You have to set first your token & shopid! \n [Click for Help](https://whoisnico.github.io/echo-bot/) | `/setshop_token` | `/setshop_id`")
                error3.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
                await inter.send(embed=error3, ephemeral=True)
                return
            
            with open("database/sellpass/shop.json", "r") as json_file:
                data = json.load(json_file)
            
            data["Shop"]["ShopID"] = shopid
            with open("database/sellpass/shop.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
                
            embed = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"Your Shop has been connected!")
            embed.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
            await inter.send(embed=embed, ephemeral=True)

    @commands.slash_command()
    async def setshop_customer_role(self, inter, role: disnake.Role):
            """Set a customer role connected with your Shop!"""
            try:
                with open("database/sellpass/shop.json", "r") as json_file:
                    data = json.load(json_file)
                    if data:
                        if not "Shop" in data and "ID" in data["Shop"] and "Token" in data["Shop"] and "ShopID" in data["Shop"]:
                            embed = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"**Error:** You have to set first your token & shopid! \n [Click for Help](https://whoisnico.github.io/echo-bot/) | `/setshop_token` | `/setshop_id`")
                            embed.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
                            await inter.send(embed=embed, ephemeral=True)
                            return
                    else:
                        embed = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"**Error:** You have to set first your token & shopid! \n [Click for Help](https://whoisnico.github.io/echo-bot/) | `/setshop_token` | `/setshop_id`")
                        embed.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
                        await inter.send(embed=embed, ephemeral=True)
                        return
            except:
                embed = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"**Error:** You have to set first your token & shopid! \n [Click for Help](https://whoisnico.github.io/echo-bot/) | `/setshop_token` | `/setshop_id`")
                embed.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
                await inter.send(embed=embed, ephemeral=True)
                return
            with open("database/sellpass/shop.json", "r") as json_file:
                data = json.load(json_file)
            
            data["Shop"]["CustomerRole"] = role.id
            with open("database/sellpass/shop.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
            
            embed = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"<@{role.id}> is now your customer role! \n Your customer can claim this Role with `/claim_customer`")
            embed.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
            await inter.send(embed=embed, ephemeral=True)


    @commands.slash_command()
    async def shop_claimrole(self, inter, orderid):
            """Get your customer role!"""
            try:
                with open("database/sellpass/shop.json", "r") as json_file:
                    data = json.load(json_file)
                    if data:
                        if not "Shop" in data and "ID" in data["Shop"] and "Token" in data["Shop"] and "ShopID" in data["Shop"] and "CustomerRole" in data["Shop"]:
                            embed = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"**Error:** You have to set first your token & shopid! \n [Click for Help](https://whoisnico.github.io/echo-bot/) | `/setshop_token` | `/setshop_id`")
                            embed.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
                            await inter.send(embed=embed, ephemeral=True)
                            return
                    else:
                        embed = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"**Error:** You have to set first your token & shopid! \n [Click for Help](https://whoisnico.github.io/echo-bot/) | `/setshop_token` | `/setshop_id`")
                        embed.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
                        await inter.send(embed=embed, ephemeral=True)
                        return
            except:
                embed = disnake.Embed(title="Sellpass Connection Setup", color=0x2F3136, description=f"**Error:** You have to set first your token & shopid! \n [Click for Help](https://whoisnico.github.io/echo-bot/) | `/setshop_token` | `/setshop_id`")
                embed.set_thumbnail(url="https://www.sythe.org/data/avatars/l/1560/1560703.jpg")
                await inter.send(embed=embed, ephemeral=True)
                return
            with open("database/sellpass/shop.json", "r") as json_file:
                data = json.load(json_file)
            
            role= data["Shop"]["CustomerRole"]
            authtoken= data["Shop"]["Token"]
            shopId= data["Shop"]["ShopID"]
            response = requests.get(f'https://dev.sellpass.io/self/{shopId}/invoices/{orderid}', headers={'Authorization': authtoken, 'Content-Type': 'application/json'})
            response_json = json.loads(response.text)
            print(response_json)
            
    

def setup(bot):
    bot.add_cog(SellpassCog(bot))
