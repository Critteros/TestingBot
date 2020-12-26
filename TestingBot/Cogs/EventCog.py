import discord
from discord.ext import commands

class EventCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")
        
    @commands.command()
    async def test(self,ctx):
        embed = discord.Embed(title="Tile", description="Desc", color=0x00ff00)\
            .add_field(name="Fiel1", value=self.exampleText(), inline=False)
        await ctx.send(embed = embed)
        
    def exampleText(self) ->list:
        return [1,2,3]
        


def setup(bot):
    bot.add_cog(EventCog(bot))