# CONFIG
# ---------
prefix = "NS!" # This will be used at the start of commands.
embed_role = 980445045385740358 # The id of role in your server used for embedding.
game = "At service for Team NS." # This will display as the game on Discord.

# ----------

# from email.mime import image
from http import client
from discord.ext import commands
from discord.ext.commands import Bot
import discord
import os
import asyncio
from os import environ

Client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))
Client.remove_command("help")

@Client.event
async def on_ready():
    print ("Ready when you are. ;)") 
    print ("Name: {}".format(Client.user.name))
    print ("ID: {}".format(Client.user.id))
    await Client.change_presence(status=discord.Status.online,activity=discord.Game(name=game))

@Client.command(pass_context=True)
@commands.has_any_role(embed_role)
async def help(ctx):
    embed = discord.Embed(title="Help!", description="Basically, this is how I'm used.", color=0x00a0ea)
    embed.add_field(name="`{}start`".format(prefix), value="Starts building an embed based on user inputs.", inline=False)
    embed.add_field(name="`{}ping`".format(prefix), value="Shows Latency of the bot.", inline=False)
    embed.add_field(name="`{}msg [#Channnel] [Message(optional)]`".format(prefix), value="Posts the message in specified channel. (Including Attachments)", inline=False)
    embed.add_field(name="`{}rmsg [#Channel] [Reply_message_id] [Message(optional)]`".format(prefix), value="Replies to the reference message with the input message. (Including Attachments)", inline=False)
    embed.add_field(name="`NOTE`".format(prefix), value="instead of using `{}`, you can simply `@mention` the bot and use above commands as well.".format(prefix), inline=False)
    embed.set_footer(text="- Designed by kebu#0090")
    await ctx.reply(embed=embed)


@Client.command(pass_context=True)
@commands.has_role(embed_role)
async def ping(ctx):
    await ctx.reply('My Latency is {0} ms'.format(round(Client.latency*1000,2)))



@Client.command(pass_context=True)
@commands.has_role(embed_role)
async def msg(ctx,channel=None,*,msg=None):
        if channel==None:
            await ctx.send(embed=discord.Embed(title="Bruh moment",description="You forgot to mention the `channel` Argument. Command format : `NS!msg [#Channel] [Message + attachments]`"))
            return
        if msg==None and ctx.message.attachments==[]:
            await ctx.send(embed=discord.Embed(title="Bruh moment",description="You forgot to write a message or attach some files bruh. Command format : `NS!msg [#Channel] [Message + attachments]`"))
            return
        Channel=Client.get_channel(int(str(channel).replace('<','').replace('>','').replace('#','')))
        await Channel.send(content=msg,files=[await f.to_file() for f in ctx.message.attachments])
        await ctx.message.delete()


@Client.command(pass_context=True)
@commands.has_role(embed_role)
async def rmsg(ctx,channel=None,rmsg=None,*,msg=None):
    if channel==None:
            await ctx.send(embed=discord.Embed(title="Bruh moment",color=0xff0000,description="You forgot to mention the `#channel` Argument. Command format : `NS!rmsg [#Channel] [Reply_message_id] [Message + attachments]`"))
            return
    if rmsg==None:
            await ctx.send(embed=discord.Embed(title="Bruh moment",color=0xff0000,description="You forgot to mention the `Reply_message_id` Argument. Command format : `NS!rmsg [#Channel] [Reply_message_id] [Message + attachments]`"))
            return
    if msg==None and ctx.message.attachments==[]:
            await ctx.send(embed=discord.Embed(title="Bruh moment",color=0xff0000,description="You forgot to write a message or attach some files bruh. Command format : `NS!rmsg [#Channel] [Reply_message_id] [Message + attachments]`"))
            return
    Channel=Client.get_channel(int(str(channel).replace('<','').replace('>','').replace('#','')))
    r=await Channel.fetch_message(rmsg)
    await r.reply(content=msg,files=[await f.to_file() for f in ctx.message.attachments])
    await ctx.message.delete()



# @Client.command(pass_context=True)
# @commands.has_role(embed_role)
# async def edt(ctx,*,msg):
#     print(ctx.message)
#     m = await ctx.send(msg+"WTF")
#     await m.edit(content='WTF HEHE')




@Client.command(pass_context=True)
@commands.has_role(embed_role)
async def start(ctx):

    # embed=discord.Embed(title="Title", description="Description", color=0x24dcf5)
    # embed.set_author(name="Author Name", url="https://www.instagram.com/Team_nsofficial/", icon_url="https://cdn.discordapp.com/attachments/964485967895494717/977618968628043796/unknown.png")
    # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/964485967895494717/977618500078153778/unknown.png")
    # embed.add_field(name="Field 1", value="Some Text", inline=False)
    # embed.add_field(name="Field 2", value="Some Text", inline=False)
    # embed.set_footer(text="Footer Text")
    # await ctx.send("Let start Building a New Embed./nPlease refer below Embed for Refrence of Field Positions.",embed=embed)


    def check(m):
        return  m.author == ctx.author
    m_title=None
    m_Color=None
    desc=None
    
    embed1=discord.Embed()
    embed1.set_author(name='Team NS', url="https://www.instagram.com/Team_nsofficial/", icon_url="https://media.discordapp.net/attachments/964485967895494717/977214545934286918/unknown.png")
    # embed1.set_footer(text="",icon_url="https://media.discordapp.net/attachments/964485967895494717/977214545934286918/unknown.png")
    ebd=await ctx.send(embed=embed1)
    
    # Title Input
    q1 = await ctx.send('Enter the Title of Embed. Type "no" to skip title.')
    m_title=await Client.wait_for('message',check=check)
    
    if m_title.content.lower() == "no" :
        await q1.delete()
        await m_title.delete()
    else:
        embed1.title=m_title.content
        await q1.delete()
        await m_title.delete()
        await ebd.edit(embed=embed1)
    
    # Description Input
    q2 = await ctx.send('Enter the Description for Embed. Type "no" to skip Description.')
    desc=await Client.wait_for('message',check=check)
    if desc.content.lower() == "no":
        await q2.delete()
        await desc.delete()
    else:
        embed1.description=desc.content
        await q2.delete()
        await desc.delete()
        await ebd.edit(embed=embed1)
    
    # color input
    q3 = await ctx.send('Enter the hex code for embed color. Type "no" to skip color selection.')
    m_Color = await Client.wait_for('message',check=check)
    if m_Color.content.lower() == "no":
        await q3.delete()
        await m_Color.delete()
    else:
        embed1.color=int('0x'+m_Color.content.replace('#',''),16)
        await q3.delete()
        await m_Color.delete()
        await ebd.edit(embed=embed1)
    
    # image input
    q4 = await ctx.send('Attach the Image. Type "no" to skip image upload.')
    m_img = await Client.wait_for('message',check=check)
    if m_img.content.lower() == "no":
        await q4.delete()
        await m_img.delete()
    else:
        embed1.set_image(url=m_img.attachments[0].url)
        await q4.delete()
        #await m_img.delete()
        await ebd.edit(embed=embed1)

        
    qs=await ctx.send('Would you like to add fields? Type yes or no.')
    msg=await Client.wait_for('message', check=check)
    if msg.content.lower()=='yes':
        while(msg.content.lower()=='yes'):
            await qs.delete()
            await msg.delete()
            qt=await ctx.send('Enter the title of the field.')
            msg1=await Client.wait_for('message',check=check)
            qv=await ctx.send('Enter the description of the field.')
            msg2=await Client.wait_for('message',check=check)
            embed1.add_field(name=msg1.content,value=msg2.content,inline=False)
            await qt.delete()
            await qv.delete()
            await msg1.delete()
            await msg2.delete()
            await ebd.edit(embed=embed1)
            qs=await ctx.send('Would you like to add fields? Type yes or no.')
            msg=await Client.wait_for('message', check=check)
    await qs.delete()
    await msg.delete()



    # Update Embed
    # embed1.color=int('0x'+m_Color.content.replace('#',''),16)
    # embed1.title=m_title.content
    # embed1.description=desc.content

    #message input
    q5= await ctx.send('Please type a message to mention out side the embed. Type "no" to skip this.')
    mg = await Client.wait_for('message',check=check)
    if mg.content.lower()== "no":
        await q5.delete()
        await mg.delete()
        mgc=None
    else:
        await q5.delete()
        await mg.delete()
        mgc=mg.content
        await ebd.edit(content=mgc,embed=embed1)
    
    
    # Announcement Channel Input
    post=await ctx.send('Mention the announcement channel. Type "no" to discard the embed.')
    msg=await Client.wait_for('message', check=check)
    
    if msg.content.lower()=="no":
        await post.delete()
        await msg.delete()
    else:
        # Send Embed to given Announcement Channel
        channel=Client.get_channel(int(str(msg.content).replace('<','').replace('>','').replace('#','')))
        await channel.send(content=mgc,embed=embed1)
        print (ctx.message.author.name + " has embedded a message in " + channel.name)
        await post.delete()
        await msg.delete()

Client.run(environ['token'])
