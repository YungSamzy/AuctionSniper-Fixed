import discord
from discord.ext import commands
import time
import os
import collections
import sys
intents=discord.Intents.all()
bot = commands.Bot(command_prefix = 'fa.', intents=intents)

def sort_margins(margins):
    try:
        sorteddict = collections.OrderedDict(sorted(margins.items(), reverse=True))
        #sorted_dict_to_list = sorted(margins, key = lambda tup: tup[0], reverse=True)
        #return sorted_dict_to_list
        return sorteddict
    except AttributeError:
        pass

def get_margin(auctions):
    new_auction_list = {}
    for auc in auctions:
        if auc != '':
            pricei = int(auc.split("`")[5].replace(',',''))
            priceii = int(auc.split("`")[7].replace(',',''))
            margin = (priceii - pricei)

            if margin <= 50000000:
                new_auction_list[margin] = auc
    if new_auction_list != {}: return new_auction_list

async def check_logs():
    channel = bot.get_channel(1037559187271598122) #unused xd
    lm_channel = bot.get_channel(1037559673215275081)
    f2channel = bot.get_channel(1037559775384309760)
    f2_2channel = bot.get_channel(1037559857051602944)
    f3channel = bot.get_channel(1037559910780649472)
    superchannel = bot.get_channel(1037559984139018250)
    #super2channel = bot.get_channel()#make channel soon
    petchannel = bot.get_channel(1037560042901213294)
    runechannel = bot.get_channel(1037560105350213684)
    log = './fliplogs/logs.txt' #unused xd
    lmlog = './fliplogs/logs_f1.txt'
    f2log = './fliplogs/logs_f2.txt'
    f2_2log = './fliplogs/logs_f2_2.txt'
    f3log = './fliplogs/logs_f3.txt'
    logsuper = './fliplogs/logs_s.txt'
    logsuper2 = './fliplogs/logs_s2.txt'#unused
    petlog = './fliplogs/pet_logs.txt'
    runelog = './fliplogs/logs_runes.txt'
    try:

        # part for #auction-sniper-main

        '''
        
        #main sniper gone cuz bad #4
        
        with open(log, 'r+') as f:
            if os.path.getsize('./fliplogs/logs.txt') > 0:
                lines = [line.rstrip() for line in f]
                for d in lines:s
                    if d != '': 
                        await channel.send(d)
                f.truncate(0)'''

        # part for #ah-sniper-f1

        with open(lmlog, 'r+') as f:
            if os.path.getsize('./fliplogs/logs_f1.txt') > 0:
                lines = [line.rstrip() for line in f]
                try:
                    slist = sort_margins(get_margin(lines))
                    await lm_channel.purge(limit=5)
                    
                    embed = discord.Embed(title='Current Top Flips (1M Margin) 1st Filter')
                    
                    slistcut = list(slist.items())[:10]
                    
                    for i, (margin, aucstr) in enumerate(slistcut):
                        #aucstr = tup[1]
                        embed.add_field(name=str(i+1)+'.', value=aucstr, inline=False)
                    await lm_channel.send(embed=embed)
                    f.truncate(0)
                except:
                    pass
        
        # #ah-sniper-f2

        with open(f2log, 'r+') as f:
            if os.path.getsize(f2log) > 0:
                lines = [line.rstrip() for line in f]
                try:
                    slist = sort_margins(get_margin(lines))
                    await f2channel.purge(limit=5)
                    embed = discord.Embed(title='Current Top Flips (1M Margin) 2nd Filter')
                    slistcut = list(slist.items())[:10]
                    for i, (margin, aucstr) in enumerate(slistcut):
                        embed.add_field(name=str(i+1)+'.', value=aucstr, inline=False)
                    await f2channel.send(embed=embed)
                    f.truncate(0)
                except:
                    pass
        
        #ah-sniper-f2-v2

        with open(f2_2log, 'r+') as f:
            if os.path.getsize(f2_2log) > 0:
                lines = [line.rstrip() for line in f]
                try:
                    slist = sort_margins(get_margin(lines))
                    await f2_2channel.purge(limit=5)
                    embed = discord.Embed(title='Current Top Flips (1M Margin) 2nd Filter v2')
                    slistcut = list(slist.items())[:10]
                    for i, (margin, aucstr) in enumerate(slistcut):
                        embed.add_field(name=str(i+1)+'.', value=aucstr, inline=False)
                    await f2_2channel.send(embed=embed)
                    f.truncate(0)
                except:
                    pass

        with open(f3log, 'r+') as f:
            if os.path.getsize(f3log) > 0:
                lines = [line.rstrip() for line in f]
                try:
                    slist = sort_margins(get_margin(lines))
                    await f3channel.purge(limit=5)
                    embed = discord.Embed(title='Currently Top Flips (1M Margin) 3rd Filter')
                    slistcut = list(slist.items())[:10]
                    for i, (margin, aucstr) in enumerate(slistcut):
                        embed.add_field(name=str(i+1)+'.', value=aucstr, inline=False)
                    await f3channel.send(embed=embed)
                    f.truncate(0)
                except:
                    pass

        # ah-sniper-super

        with open(logsuper, 'r+') as f:
            try:
                if os.path.getsize(logsuper) > 0:
                    lines = [line.rstrip() for line in f]
                    for d in lines:
                        if d != '': 
                            await superchannel.send(d)
                    f.truncate(0)
            except:
                pass

        '''with open(logsuper2, 'r+') as f:
            try:
                if os.path.getsize(logsuper2) > 0:
                    lines = [line.rstrip() for line in f]
                    for d in lines:
                        if d != '': 
                            await super2channel.send(d)
                    f.truncate(0)
            except:
                pass
            '''
        
        #pet results

        with open(petlog, 'r+') as f:
            if os.path.getsize(petlog) > 0:
                lines = [line.rstrip() for line in f]
                try:
                    slist = sort_margins(get_margin(lines))
                    await petchannel.purge(limit=5)
                    embed = discord.Embed(title='Current Top Pet Flips (1M Margin)')
                    slistcut = list(slist.items())[:10]
                    for i, (margin, aucstr) in enumerate(slistcut):
                        embed.add_field(name=str(i+1)+'.', value=aucstr, inline=False)
                    await petchannel.send(embed=embed)
                    f.truncate(0)
                except:
                    pass

        with open(runelog, 'r+') as f:
            if os.path.getsize(runelog) > 0:
                lines = [line.rstrip() for line in f]
                try:
                    slist = sort_margins(get_margin(lines))
                    await runechannel.purge(limit=5)
                    embed = discord.Embed(title='Current Top Flips With T3 Runes (1M Margin, Excluding Rune Prices)')
                    slistcut = list(slist.items())[:10]
                    for i, (margin, aucstr) in enumerate(slistcut):
                        embed.add_field(name=str(i+1)+'.', value=aucstr, inline=False)
                    await runechannel.send(embed=embed)
                    f.truncate(0)
                except:
                    pass
                    

    except FileNotFoundError:
        pass

@bot.command(name = 'run')
async def start_check(ctx):
    if ctx.author.id == 877392093155311686:
        while True:
            try:
                await check_logs()
            except:
                os.execv(sys.executable, ['python'] + sys.argv)

bot.run(TOKEN)