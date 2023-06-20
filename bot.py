import discord
import discord.ui
from discord import app_commands
import requests
import json
import config


def run_discord_bot():
    TOKEN = config.TOKEN
    session = '2022W' #to get first section in this session
    intents = discord.Intents.default()  
    intents.message_content = True
    client = discord.Client(intents=intents)

    tree = app_commands.CommandTree(client)

    @tree.command(name = "ubcinfo", description = "Get Info on a UBC Course")
    async def first_command(interaction: discord.Interaction, course_code: str, course_number: str):
        code = course_code.upper()

        grade_api = f'https://ubcgrades.com/api/v3/course-statistics/UBCV/{code}/{course_number}'
        sections_api = f'https://ubcgrades.com/api/v3/sections/UBCV/{session}/{code}/{course_number}'
        
        grade_request = requests.get(grade_api)
        sections_request = requests.get(sections_api)

        if (grade_request.status_code == 200):
            api_json = json.loads(grade_request.content)
            first_section = str(json.loads(sections_request.content)[0])

            average = round(api_json['average'], 2)
            title = api_json['course_title']
            ssc = f'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept={code}&course={course_number}'
            
            #ubcgrades no longer has overall section so it puts you on the first available section
            ubc_grades = f'https://ubcgrades.com/#UBCV-{session}-{code}-{course_number}-{first_section}' 
            await interaction.response.send_message(
                embed=discord.Embed(
                    title=f'{code} {course_number}: {title}',
                    description=f'Average: {average}% \n[SSC Link]({ssc}) \n[UBCGrades Link]({ubc_grades})',
                )
            )
        else:
            await interaction.response.send_message(f"{code} {course_number} doesn't seem to exist!")

    @client.event
    async def on_ready():
        await tree.sync()
        print(f'{client.user} is now running!')
    
    client.run(TOKEN)