import discord
from discord.ext import commands
import random

# Enable intents to access members
intents = discord.Intents.all()
intents.members = True  
# Create bot object
bot = commands.Bot(command_prefix='!', intents=intents, permissions=discord.Permissions(send_messages=True))

# Define the giveaway command
@bot.command()
async def giveaway(ctx):
    # Get the roles for each hat level
    black_hat_role = discord.utils.get(ctx.guild.roles, name='Black Hat - 214k')
    diamond_hat_role = discord.utils.get(ctx.guild.roles, name='Diamond Hat - 150k')
    platinum_hat_role = discord.utils.get(ctx.guild.roles, name='Platinum Hat - 100k')
    gold_hat_role = discord.utils.get(ctx.guild.roles, name='Gold Hat - 75k')
    silver_hat_role = discord.utils.get(ctx.guild.roles, name='Silver Hat - 50k')

    # Create a dictionary to store entries for each member
    entries = {}

    # Loop through all members and add their entries based on their hat level
    for member in ctx.guild.members:
        if black_hat_role in member.roles:
            entries[member] = entries.get(member, 0) + 5
        elif diamond_hat_role in member.roles:
            entries[member] = entries.get(member, 0) + 4
        elif platinum_hat_role in member.roles:
            entries[member] = entries.get(member, 0) + 3
        elif gold_hat_role in member.roles:
            entries[member] = entries.get(member, 0) + 2
        elif silver_hat_role in member.roles:
            entries[member] = entries.get(member, 0) + 1

    # Check if there are any eligible members for the giveaway
    if not entries:
        await ctx.send("No eligible members found!")
        return

    # Print the total number of entries for each hat level
    print("Total number of entries:")
    for role in [black_hat_role, diamond_hat_role, platinum_hat_role, gold_hat_role, silver_hat_role]:
        role_entries = sum([entries[member] for member in ctx.guild.members if role in member.roles])
        role_members = len([member for member in ctx.guild.members if role in member.roles])
        print(f"{role.name} - {role_members} members, {role_entries} entries")
    
    # Choose a random winner from the eligible members
    eligible_winners = [member for member, entry_count in entries.items()]
    chosen_winner = random.choice(eligible_winners)

    # Print the total number of entries and eligible members, and the winner's number of entries
    total_entries = sum(entries.values())
    print(f'Total Entries: {total_entries}')
    print(f'Members: {", ".join([str(member) for member in entries])}')
    winner_entries = entries[chosen_winner]
    
    # Announce the winner in the channel
    await ctx.send(f'Congratulations to {chosen_winner.mention} for winning the giveaway with {winner_entries} entries out of {total_entries} total entries!')

# Run the bot with the specified token
bot.run('')
