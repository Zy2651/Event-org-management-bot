
import discord
import asyncio
from discord.ext import commands
import random
import requests
from PIL import Image, ImageDraw, ImageFont



intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("---------------")


@client.command()
async def ask(ctx):
    await ctx.send("What's your favorite color?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        message = await client.wait_for('message', check=check, timeout=30.0)
        await ctx.send(f"Your favorite color is {message.content}!")
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond!")

@client.command()
async def eternal(ctx):
    await ctx.send("An organization that provides belonging.")

@client.command()
async def link(ctx):
    await ctx.send("Copy this link: https://discord.com/oauth2/authorize?client_id=1270194998645887077 to allow the bot to be in your server")
@client.command()
async def data(ctx, number: int, organization_name: str):
    
    

    club_trophy_list = []
    club_list = []
    

    
    
    def mean(Club_trophy_List,is2DList):
        numList = []
        if is2DList:
            for club in Club_trophy_List:
                for trophy in club:
                    numList.append(trophy)
        else:
            for trophy in Club_trophy_List:
                numList.append(trophy)
        sum = 0
        for num in numList:
            sum = sum + num
        return sum / len(numList)
            
    def median(Club_trophy_List, is2DList):
        numList = []
        if is2DList:
            for club in Club_trophy_List:
                for trophy in club:
                    numList.append(trophy)
        else:
            for trophy in Club_trophy_List:
                numList.append(trophy)

        
        numList.sort()
        if ((len(numList) % 2) == 1):
            median_index = int((len(numList)/2.0))
            return numList[median_index]
        else:
            Index1 = int((len(numList) / 2.0)) - 1
            Index2 = int((len(numList) / 2.0))
            return (numList[Index1] + numList[Index2]) / 2.0
    
    def check2d(List):
        try:
            sum(List, [])
            return True
        except:
            return False    
    
    def count(Club_trophy_List,is2DList):
        numList = []
        if is2DList:
            for club in Club_trophy_List:
                for trophy in club:
                    numList.append(trophy)
        else:
            for trophy in Club_trophy_List:
                numList.append(trophy)
        return len(numList)
    def minumum(Club_trophy_List, is2DList):
        numList = []
        if is2DList:
            for club in Club_trophy_List:
                for trophy in club:
                    numList.append(trophy)
        else:
            for trophy in Club_trophy_List:
                numList.append(trophy)
        numList.sort()
        return numList[0]
    def maximum(Club_trophy_List, is2DList):
        numList = []
        if is2DList:
            for club in Club_trophy_List:
                for trophy in club:
                    numList.append(trophy)
        else:
            for trophy in Club_trophy_List:
                numList.append(trophy)
        numList.sort()
        return numList[len(numList) - 1]
    def firstQuatile(Club_trophy_List, is2DList):
    
        numList = []
        if is2DList:
            for club in Club_trophy_List:
                for trophy in club:
                    numList.append(trophy)
        else:
            for trophy in Club_trophy_List:
                numList.append(trophy)
            
        numList.sort()
        median = 0
        if ((len(numList) % 2) == 1):
            median_index = int((len(numList)/2.0))
            median = numList[median_index]
        else:
            Index1 = int((len(numList) / 2.0)) - 1
            Index2 = int((len(numList) / 2.0))
            median = (numList[Index1] + numList[Index2]) / 2
        try:
            indexOfMedian = numList.index(median)
            firstIndex = int(indexOfMedian / 2.0 + 0.5) 
            secondIndex = int(indexOfMedian / 2.0 - 0.5)
        
            return (numList[firstIndex] + numList[secondIndex]) / 2
        except:
            halfLength = len(numList) / 2
            indexOf1stQuatile = int(halfLength / 2 + 0.5)
        
            return numList[indexOf1stQuatile]

    def thirdQuatile(Club_trophy_List, is2DList):
    
        numList = []
        if is2DList:
            for club in Club_trophy_List:
                for trophy in club:
                    numList.append(trophy)
        else:
            for trophy in Club_trophy_List:
                numList.append(trophy)
        numList.sort()
        median = 0
        if ((len(numList) % 2) == 1):
            median_index = int((len(numList)/2.0))
            median = numList[median_index]
        else:
            Index1 = int((len(numList) / 2.0)) - 1
            Index2 = int((len(numList) / 2.0))
            median = (numList[Index1] + numList[Index2]) / 2
        try:
            indexOfMedian = numList.index(median)
            firstIndex = int(((indexOfMedian + len(numList)) / 2) + 0.5)
            secondIndex = int(((indexOfMedian + len(numList)) / 2) - 0.5)
        
            return (numList[firstIndex] + numList[secondIndex]) / 2
        except:
            halfLength = len(numList) / 2
            indexOf3rdQuatile = int((halfLength + len(numList))/2 + 0.5)

            return numList[indexOf3rdQuatile]


    
    for i in range(number):
    
        await ctx.send("Enter your Club Tag. For example, 2UUGC0LVQ.")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            club_tag = await client.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send("You took too long")


        
        api_key =  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjMzMWQwNWQzLTYxZTgtNDk2OS05MjI2LTc0ZmVjMWU0NTRiYiIsImlhdCI6MTcyMzQ5NzA5NCwic3ViIjoiZGV2ZWxvcGVyLzlmZGE4M2ZmLTVkNzQtN2NjYi0zYjg5LTRhZjMzN2ZiMzFmNCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiOTkuMTcwLjMzLjYzIl0sInR5cGUiOiJjbGllbnQifV19.VJIdlCpBaliK2GLQfQvzdwkqiaB1dvJBdmY_Qsq75aPLqlPGC6gtPt55-TFrkncqgqnMRGY-7DX51_cfC3vHrg'
        headers = {
            'Authorization': f'Bearer {api_key}'
        }
        club_tag = club_tag.content
        response = requests.get(f'https://api.brawlstars.com/v1/clubs/%23{club_tag}', headers=headers)
        data = response.json()
        club_members = data["members"]
        trophy_list = []
        for member in club_members:
            trophy_list.append(member["trophies"])
            
        club_trophy_list.append(trophy_list)
        club_list.append(data["name"])
    if number > 1:
        for i in range(len(club_trophy_list)):
            await ctx.send(club_list[i] + "'s descriptive statistics")
            await ctx.send("Member Count - "+ str(count(club_trophy_list[i], check2d(club_trophy_list[i]))))
            await ctx.send("Median Trophies - "+ str(median(club_trophy_list[i], check2d(club_trophy_list[i]))))
            await ctx.send("The 25 percentile's Trophies - "+ str(firstQuatile(club_trophy_list[i], check2d(club_trophy_list[i]))))
            await ctx.send("The 75 percentile's Trophies - "+ str(thirdQuatile(club_trophy_list[i], check2d(club_trophy_list[i]))))
            await ctx.send("Mean Trophies - " + str(mean(club_trophy_list[i], check2d(club_trophy_list[i]))))
            await ctx.send("Max Trophies - "+ str(maximum(club_trophy_list[i], check2d(club_trophy_list[i]))))
            await ctx.send("Min Trophies - "+ str(minumum(club_trophy_list[i], check2d(club_trophy_list[i]))))
    
    await ctx.send(organization_name + "'s descriptive statistics")
    await ctx.send("Member Count - " + str(count((club_trophy_list), check2d(club_trophy_list))))
    await ctx.send( "Median Trophies - " + str(median((club_trophy_list), check2d(club_trophy_list))))
    await ctx.send("The 25 percentile's Trophies - "+ str(firstQuatile(club_trophy_list, check2d(club_trophy_list))))
    await ctx.send("The 75 percentile's Trophies - "+ str(thirdQuatile(club_trophy_list, check2d(club_trophy_list))))
    await ctx.send("Mean Trophies - " + str(mean(club_trophy_list, check2d(club_trophy_list))))
    await ctx.send("Max Trophies - "+ str(maximum(club_trophy_list, check2d(club_trophy_list))))
    await ctx.send("Min Trophies - "+ str(minumum(club_trophy_list, check2d(club_trophy_list))))
        
@client.command()
@commands.has_permissions(kick_members=True) 
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')

@kick.error
async def kick_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that")

@client.command()
@commands.has_permissions(ban_members=True) 
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has been banned')
@ban.error
async def ban_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that")



@client.command()
async def create_bracket(ctx, names: str, bracket_size: int):
    name_list = []
    bracket_list = []
    def checkComma(comma):
        if comma == ",":
            return True
        return False


    def sortNames(names):
        
        startingIndex = 0 
        i = 0
        while (i < len(names)):
    
                if(i + 1 == len(names) or checkComma(names[i + 1])):
                    name_list.append(names[startingIndex:i + 1])
                    startingIndex = i + 2
                i = i + 1
    
    

    
    sortNames(names)
    for i in range(bracket_size):
        bracket_list.append("bye")
    
    j = 0
    
    while j < bracket_size:        
        index = random.randint(0,len(name_list) - 1)
        index2 = random.randint(0,len(bracket_list) - 1)
        if bracket_list[index2] == "bye":
            bracket_list[index2] = name_list[index]
            name_list.remove(name_list[index])
            j = j + 1
    await ctx.send(bracket_list)
    # Create a blank white image
    img = Image.new('RGB', (700, 800), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    
    font = ImageFont.load_default()
    text_color = (0, 0, 0)
    
    tries = bracket_size
    if bracket_size == 16:
        y = 0
        y2 = 10
        y3 = 10
        x = 0
        x2 = 50
        for i in range(tries):
            draw.text((10,y),text=bracket_list[i],fill=text_color, font=font)
            draw.line((x, y2, x2, y2), fill='black', width=1)
            y = y + 50
            y2 = y2 + 50
        tries = int(tries / 2)
        for i in range(tries):
            draw.line((x2, y3, x2, y3+50), fill='black', width=1)
            y3 = y3 + 100
        x = x + 50
        x2 = x2 + 50
        y = 0
        y2 = 35
        y3 = 35
        for i in range(tries):
            draw.line((x, y2, x2, y2), fill='black', width=1)
            y = y + 100
            y2 = y2 + 100

        
    
    # Save the image locally
    img.save("generated_image.png")
    
    # Send the image in Discord
    with open("generated_image.png", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
