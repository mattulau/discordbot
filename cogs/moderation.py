import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.py is online.")

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, count: int):
        await ctx.channel.purge(limit = count)

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, modreason):
        await ctx.guild.kick(member)

        conf_embed = discord.Embed(title = "Success", color = discord.Color.green())
        conf_embed.add_field(name = "Kicked:", value = f"{member.mention} has been kicked from this server by {ctx.author.mention}", inline = False)
        conf_embed.add_field(name = "Reason:", value = modreason, inline = False)

        await ctx.send(embed = conf_embed)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, modreason):
        await ctx.guild.ban(member)

        conf_embed = discord.Embed(title = "Success", color = discord.Color.green())
        conf_embed.add_field(name = "Banned:", value = f"{member.mention} has been Banned from this server by {ctx.author.mention}", inline = False)
        conf_embed.add_field(name = "Reason:", value = modreason, inline = False)

        await ctx.send(embed = conf_embed)

    @commands.command(name = "unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, userId):
        user = discord.Object(id = userId)
        await ctx.guild.unban(user)

        conf_embed = discord.Embed(title = "Success!", color = discord.Color.green())
        conf_embed.add_field(name = "Unbanned", value = f"<@{userId}> has been unabanned from the server by {ctx.author.mention}.", inline = False)

        await ctx.send(embed = conf_embed)


async def setup(client):
    await client.add_cog(Moderation(client))