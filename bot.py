import yaml
import discord
from discord.ext import commands
from discord import Option
from discord import SlashCommandGroup
from discord.commands import slash_command, Option
from asyncio import *
from urllib.error import HTTPError, URLError
from discord.ext.ui import Message
import json
import urllib.request
import deepl

###############################################################
# Congig File
with open('config.yml') as f:
    keys = yaml.load(f, Loader=yaml.FullLoader)

# Discord Token
token = keys['Keys']['Token']

# Discord Test_Token
Test_token = keys['Keys']['Test_Token']

# Naver Open API application ID (Papago)
client_id = keys['Keys']['client_id']

# Naver Open API application token (Papago)
client_secret = keys['Keys']['client_secret']

# DeepL API Key
API_KEY = keys['Keys']['DeepL_Token']

# Papago API URL
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
###############################################################
###############################################################
# Error Check (Papago APIのみ)
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as res:
        body = res.read()
except urllib.error.HTTPError as err:
    print("ステータス コード:")
    print(err.code)
    if(err.code == 200 or err.code == 405):
        print("OK")
    else:
        print("HTTPError")
        print(err.code)
        quit()
except urllib.error.URLError as err:
    print("URLError")
    print(err.reason)
    quit()
###############################################################
# debug_guilds=[]にギルドIDを指定する。
#bot = discord.Bot(debug_guilds=[xxxxxxxxxxxxxxxxxx])
bot = discord.Bot()


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Type /LANG1_LANG2"))
    print("BOTが起動しました。\nID: {0.user}".format(bot))

# 日本語
class ja_en_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【日本語⇛English】 DeepL API")
        text = self.children[0].value
        target_lang = 'EN-US'
        translator = deepl.Translator(API_KEY)
        result = translator.translate_text(text, target_lang=target_lang)
        print("翻訳前")
        print(text)
        print("翻訳後")
        print(result)
        embed.add_field(name="翻訳前🇯🇵", value=text)
        embed.add_field(name="翻訳後🇺🇸", value=result)
        await interaction.response.send_message(embeds=[embed])

class ja_ko_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【日本語⇛한국어】 papago API")
        text = self.children[0].value
        output = ('%0A'.join(text.splitlines()))
        source = "ja"
        target = "ko"
        data = f"source={source}&target={target}&text={output}"
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            response = json.loads(response_body.decode('utf-8'))
            result = response['message']['result']['translatedText']
            print("翻訳前\n"+text)
            print("翻訳後\n"+result)
        else:
            print("Error Code:" + rescode)
        embed.add_field(name="翻訳前🇯🇵", value=text)
        embed.add_field(name="翻訳後🇰🇷", value=result)
        await interaction.response.send_message(embeds=[embed])

class ja_cn_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【日本語⇛中文】 DeepL API")
        text = self.children[0].value
        target_lang = 'ZH'
        translator = deepl.Translator(API_KEY)
        result = translator.translate_text(text, target_lang=target_lang)
        print("翻訳前")
        print(text)
        print("翻訳後")
        print(result)
        embed.add_field(name="翻訳前🇯🇵", value=text)
        embed.add_field(name="翻訳後🇨🇳", value=result)
        await interaction.response.send_message(embeds=[embed])

# 英語
class en_ja_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【English⇛日本語】 DeepL API")
        text = self.children[0].value
        target_lang = 'JA'
        translator = deepl.Translator(API_KEY)
        result = translator.translate_text(text, target_lang=target_lang)
        print("翻訳前")
        print(text)
        print("翻訳後")
        print(result)
        embed.add_field(name="翻訳前🇺🇸", value=text)
        embed.add_field(name="翻訳後🇯🇵", value=result)
        await interaction.response.send_message(embeds=[embed])

class en_ko_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【English⇛한국어】 papago API")
        text = self.children[0].value
        output = ('%0A'.join(text.splitlines()))
        source = "en"
        target = "ko"
        data = f"source={source}&target={target}&text={output}"
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            response = json.loads(response_body.decode('utf-8'))
            result = response['message']['result']['translatedText']
            print("翻訳前\n"+text)
            print("翻訳後\n"+result)
        else:
            print("Error Code:" + rescode)
        embed.add_field(name="翻訳前🇺🇸", value=text)
        embed.add_field(name="翻訳後🇰🇷", value=result)
        await interaction.response.send_message(embeds=[embed])

class en_cn_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【English⇛中文】 DeepL API")
        text = self.children[0].value
        target_lang = 'ZH'
        translator = deepl.Translator(API_KEY)
        result = translator.translate_text(text, target_lang=target_lang)
        print("翻訳前")
        print(text)
        print("翻訳後")
        print(result)
        embed.add_field(name="翻訳前🇺🇸", value=text)
        embed.add_field(name="翻訳後🇨🇳", value=result)
        await interaction.response.send_message(embeds=[embed])

# 韓国語
class ko_en_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【한국어⇛English】 papago API")
        text = self.children[0].value
        output = ('%0A'.join(text.splitlines()))
        source = "ko"
        target = "en"
        data = f"source={source}&target={target}&text={output}"
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            response = json.loads(response_body.decode('utf-8'))
            result = response['message']['result']['translatedText']
            print("翻訳前\n"+text)
            print("翻訳後\n"+result)
        else:
            print("Error Code:" + rescode)
        embed.add_field(name="翻訳前🇰🇷", value=text)
        embed.add_field(name="翻訳後🇺🇸", value=result)
        await interaction.response.send_message(embeds=[embed])

class ko_ja_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【한국어⇛日本語】 papago API")
        text = self.children[0].value
        output = ('%0A'.join(text.splitlines()))
        source = "ko"
        target = "ja"
        data = f"source={source}&target={target}&text={output}"
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            response = json.loads(response_body.decode('utf-8'))
            result = response['message']['result']['translatedText']
            print("翻訳前\n"+text)
            print("翻訳後\n"+result)
        else:
            print("Error Code:" + rescode)
        embed.add_field(name="翻訳前🇰🇷", value=text)
        embed.add_field(name="翻訳後🇯🇵", value=result)
        await interaction.response.send_message(embeds=[embed])


class ko_cn_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【한국어⇛中文】 papago API")
        text = self.children[0].value
        output = ('%0A'.join(text.splitlines()))
        source = "ko"
        target = "zh-CN"
        data = f"source={source}&target={target}&text={output}"
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            response = json.loads(response_body.decode('utf-8'))
            result = response['message']['result']['translatedText']
            print("翻訳前\n"+text)
            print("翻訳後\n"+result)
        else:
            print("Error Code:" + rescode)
        embed.add_field(name="翻訳前🇰🇷", value=text)
        embed.add_field(name="翻訳後🇨🇳", value=result)
        await interaction.response.send_message(embeds=[embed])

# 中国語
class cn_en_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【中文⇛English】 DeepL API")
        text = self.children[0].value
        target_lang = 'EN-US'
        translator = deepl.Translator(API_KEY)
        result = translator.translate_text(text, target_lang=target_lang)
        print("翻訳前")
        print(text)
        print("翻訳後")
        print(result)
        embed.add_field(name="翻訳前🇨🇳", value=text)
        embed.add_field(name="翻訳後🇺🇸", value=result)
        await interaction.response.send_message(embeds=[embed])

class cn_ja_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【中文⇛日本語】 DeepL API")
        text = self.children[0].value
        target_lang = 'JA'
        translator = deepl.Translator(API_KEY)
        result = translator.translate_text(text, target_lang=target_lang)
        print("翻訳前")
        print(text)
        print("翻訳後")
        print(result)
        embed.add_field(name="翻訳前🇨🇳", value=text)
        embed.add_field(name="翻訳後🇯🇵", value=result)
        await interaction.response.send_message(embeds=[embed])

class cn_ko_c(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(
            label="Text", style=discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Translation 【中文⇛한국어】 papago API")
        text = self.children[0].value
        output = ('%0A'.join(text.splitlines()))
        source = "zh-CN"
        target = "ko"
        data = f"source={source}&target={target}&text={output}"
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            response = json.loads(response_body.decode('utf-8'))
            result = response['message']['result']['translatedText']
            print("翻訳前\n"+text)
            print("翻訳後\n"+result)
        else:
            print("Error Code:" + rescode)
        embed.add_field(name="翻訳前🇨🇳", value=text)
        embed.add_field(name="翻訳後🇰🇷", value=result)
        await interaction.response.send_message(embeds=[embed])

# 日本語
@bot.slash_command()
async def ja_en(ctx: discord.ApplicationContext):
    """日本語から英語へ翻訳します。"""
    modal = ja_en_c(title="Translation 【日本語⇛English】")
    await ctx.send_modal(modal)

@bot.slash_command()
async def ja_ko(ctx: discord.ApplicationContext):
    """日本語から한국어へ翻訳します。"""
    modal = ja_ko_c(title="Translation 【日本語⇛한국어】")
    await ctx.send_modal(modal)

@bot.slash_command()
async def ja_cn(ctx: discord.ApplicationContext):
    """日本語から中文へ翻訳します。"""
    modal = ja_cn_c(title="Translation 【日本語⇛中文】")
    await ctx.send_modal(modal)


# 英語
@bot.slash_command()
async def en_ja(ctx: discord.ApplicationContext):
    """Translate from English to Japanese."""
    modal = en_ja_c(title="Translation 【English⇛日本語】")
    await ctx.send_modal(modal)

@bot.slash_command()
async def en_ko(ctx: discord.ApplicationContext):
    """Translates from English to Korean."""
    modal = en_ko_c(title="Translation 【English⇛한국어】")
    await ctx.send_modal(modal)

@bot.slash_command()
async def en_cn(ctx: discord.ApplicationContext):
    """Translates from English to Chinese."""
    modal = en_cn_c(title="Translation 【English⇛中文】")
    await ctx.send_modal(modal)


# 韓国語
@bot.slash_command()
async def ko_en(ctx: discord.ApplicationContext):
    """한국어에서 영어로 번역합니다."""
    modal = ko_en_c(title="Translation 【한국어⇛English】")
    await ctx.send_modal(modal)

@bot.slash_command()
async def ko_ja(ctx: discord.ApplicationContext):
    """한국어에서 일본어로 번역합니다."""
    modal = ko_ja_c(title="Translation 【한국어⇛日本語】")
    await ctx.send_modal(modal)

@bot.slash_command()
async def ko_cn(ctx: discord.ApplicationContext):
    """한국어에서 중국어로 번역합니다."""
    modal = ko_cn_c(title="Translation 【한국어⇛中文】")
    await ctx.send_modal(modal)


# 中国語
@bot.slash_command()
async def cn_en(ctx: discord.ApplicationContext):
    """从中文翻译成英语。"""
    modal = cn_en_c(title="Translation 【中文⇛English】")
    await ctx.send_modal(modal)

@bot.slash_command()
async def cn_ja(ctx: discord.ApplicationContext):
    """从中文翻译成日语。"""
    modal = cn_ja_c(title="Translation 【中文⇛日本語】")
    await ctx.send_modal(modal)

@bot.slash_command()
async def cn_ko(ctx: discord.ApplicationContext):
    """从中文翻译成韩语。"""
    modal = cn_ko_c(title="Translation 【中文⇛한국어】")
    await ctx.send_modal(modal)

bot.run(token)
