import os

from dotenv import load_dotenv
from discord.ext import commands


class BananaBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")

    async def on_command_error(self, context, exception):
        print(f"{self.user.display_name} : {exception}.")

    async def on_message(self, message):
        print(f"{self.user.display_name} : {message.content}.")
        if message.content.lower() == "ping":
            await message.channel.send("pong", delete_after=2)
            sup = await message.channel.history(limit=2).flatten()
            for each_message in sup:
                await each_message.delete()
        await bot.process_commands(message)

load_dotenv(dotenv_path="config")
bot = BananaBot()
@bot.command(name="del")
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()
    nb = 0
    for each_message in messages:
        await each_message.delete()
        print("Bananabot: del message.")
        print(f"{each_message}")
        nb += 1
    await ctx.channel.send(f"{number_of_messages} message suprimé", delete_after=2)
bot.run(os.getenv("TOKEN"))
