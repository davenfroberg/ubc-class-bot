import discord
import discord.ui
import responses
from discord import app_commands
import requests
import json
import config


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = config.TOKEN
    intents = discord.Intents.default()  
    intents.message_content = True
    client = discord.Client(intents=intents)

    tree = app_commands.CommandTree(client)

    @tree.command(name = "ubcinfo", description = "Get Info on a UBC Course", guild=discord.Object(id=1004543455332147351)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
    async def first_command(interaction: discord.Interaction, course_code: str, course_number: str):
        code = course_code.upper()
        grade_api = f'https://ubcgrades.com/api/v3/course-statistics/UBCV/{code}/{course_number}'
        request = requests.get(grade_api)
        if (request.status_code == 200):
            api_json = json.loads(request.content)
            average = round(api_json['average'], 2)
            title = api_json['course_title']
            ssc = f'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept={code}&course={course_number}'
            await interaction.response.send_message(
                embed=discord.Embed(
                    title=f'{code} {course_number}: {title}',
                    description=f'Average: {average}% \n[SSC Link]({ssc}) \n[UBCGrades Link](https://ubcgrades.com/course/{code}/{course_number})',
                )
            )
        else:
            await interaction.response.send_message(f"{code} {course_number} doesn't seem to exist!")

    @client.event
    async def on_ready():
        await tree.sync(guild=discord.Object(id=1004543455332147351))
        print(f'{client.user} is now running!')
    
    
    client.run(TOKEN)