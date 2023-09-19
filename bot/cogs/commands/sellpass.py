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
                print(response.text)
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
            await inter.send(embeds=[embed], ephemeral=True)

    @commands.slash_command()
    async def setshop_id(self, inter, token: str):
            """Connect your Bot with your Sellpass Shop!"""
            try:
                id = inter.guild.id
                authtoken = "Bearer " + token
                data = {
                    "Shop": {
                        "ID": id,
                        "Token": authtoken
                    }
                }
                data["Shop"]["ShopID"] = shopid
                
                response = requests.get(f'https://dev.sellpass.io/self/shops', headers={'Authorization': authtoken, 'Content-Type': 'application/json'})
                print(response.text)
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
            await inter.send(embeds=[embed], ephemeral=True)

def setup(bot):
    bot.add_cog(SellpassCog(bot))
