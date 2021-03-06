import discord
import random
import urllib.request
from bs4 import BeautifulSoup
from random import randrange
from discord.ext import commands
import qrcode
import os
from discord_buttons_plugin import *
from googletrans import Translator
import asyncio
import sys
import pandas
from discord_slash import SlashCommand, cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
bot = commands.Bot(command_prefix='.')
print("Working...")
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

buttons = ButtonsClient(bot)
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game('/도움말'))


#list
Administrator = ['상철이 아니고 상현이', '허당비니', '롤모델이용쿠', '비타민새', 'dark0316']

Random = [
    '길 가다가 개똥 밟을 확률은 ', '길 가다가 넘어질 확률은', '탈모가 될 확률은 ', '고자가 될 확률은 ',
    '오늘 선생님을 만날 확률은 ', '몰폰하다가 걸릴 확률은 ', '몰컴하다가 걸릴 확률은 ', '설사를 할 확률은 ',
    '껌이 신발에 붙을 확률은 ', '애인이 생길 확률은 ', '고백하고 차일 확률은 ', '조폭에게 맞을 확률은 ',
    '휴대폰이 고장날 확률은 ', '샷건을 칠 확률은 ', '게임에서 질 확률은 ', '아이스크림을 먹을 확률은 ',
    '공짜로 얻어먹을 확률은 ', '새 물건이 생길 확률은 ', '구독자가 줄을 확률은 ', '구독자가 늘 확률은 '
]

random2 = [
    '당신의 머머리', '누군가의 발가락', '우아한승재가 먹다남은 쿠킹덤 케이크', '비타민새의 무좀',
    '활동 안하는 잡것들의 코딱지', '방금 갓 토한 따뜻한 토', '방금 이쑤신 사람이 망친 코드',
    '이쑤신개발자의 올라오지 않는 프리미어 프로 강좌', '어쩔티비', '니 미래 모습', '코드를 날린 개발자', '오류', '마기꾼',
    '에러', '어떤 사람', '바보', '외계인', '에일리언', '재미없는 영화', '마해자', '손소독제', '귀염뽀짝한 개발자',
    '마이클 잭슨', '지우개', '연필', '샤프', '자', '필통', '전등', '스탠드', '반딧불이', '저녁 식사',
    '점심 식사', '아침 식사', '라면'
]

food = [
    '뜨끈한 된장국', '뜨끈한 된장찌개', '맛있는 피자', '껍데기가 바삭한 교촌치킨', '따끈따끈한 뿌링클 치킨',
    '아침으로 먹기에 가벼운 시리얼', '목마를때 먹는 콜라', '매콤한 닭도리탕', '쫀득쫀득한 떡볶이', '추억의 카레라이스',
    '세숫대야 냉면', '야식으로 좋은 닭발', '없어서 못 먹는다는 알탕', '맛있는거 옆에 맛있는거 Sprite!',
    '한국인이라면 못참는 김치', '명절에 먹는 간장게장', '매운 맛이 일품인 양념게장', '바삭한 명량핫도그',
    '고소한 고니가 맛있는 동태탕', '전주의 명물! 전주비빔밥', '코카콜라가 뭔데?! 펩시', '따끈한 족발', '매콤한 신라면', '헥헥, 혀가 탄다.. 불닭볶음면!', '라면은 역시 진라면', '라면의 원조! 삼양라면'
]

nonsense = ['**학생들이 싫어하는 피자**는?\n\n||**책 피자**||', '**곰이 다니는 목욕탕 이름**은?\n\n||**곰탕**||', '**신**이 화가 나면?\n\n||**신발끈**||', '**오래될수록 젊어 보이는 것**은?\n\n||**사진**||', '**세상에서 가장 뜨거운 바다**는?\n\n||**열바다**||',
'**세상에서 가장 추운 바다**는?\n\n||**썰렁해**||', "**'개가 사람을 가르친다'** 를 4자로 줄이면?\n\n||**개인지도**||", '**쥐 네 마리**가 모이면 무엇이 될까?\n\n||**쥐포**||', '**황금색 쥐가 사는 구역**은?\n\n||**금쥐구역**||', '**공**이 웃으면?\n\n||**풋볼**||',
'**자동차**가 울면?\n\n||**잉카**||', '**자동차**를 톡 하고 치면?\n\n||**카톡**||', '**다리미가 좋아하는 음식**은?\n\n||**피자**||', '**폭발하기 가장 쉬운 나라**는?\n\n||**부탄**||', '**광부가 가장 많은 나라**는?\n\n||**케냐**||', '**물고기의 반대말**은?\n\n||**불고기**||',
'**육지에 사는 고래**는?\n\n||**술고래**||', '**세상에서 가장 무서운 비**는?\n\n||**낭비**||', '**도둑이 몰래 훔친 돈**은?\n\n||**슬그머니**||', '**몸무게가 가장 많이 나갈 때**는?\n\n||**철들 때**||', '**울다가 다시 웃는 사람**을 다섯 글자로?\n\n||**아까운 사람**||',
'**세상에서 가장 쉬운 숫자**는?\n\n||**십구만(190,000)**||', '**돌잔치를 영어로** 하면?\n\n||**락 페스티벌**||', '**날마다 흑심을 품고 다니는 것**은?\n\n||**연필**||', '**아몬드**가 죽으면?\n\n||**다이아몬드**||', '**곤충의 몸**을 3등분 하면?\n\n||**죽는다**||',
'**무엇이든지 혼자 다 해 먹는 사람**은?\n\n||**자취생**||', '**세상에서 제일 뜨거운 과일**은?\n\n||**천도복숭아**||', '**바나나**가 웃으면?\n\n||**바나나킥**||', '**왕이 헤어질 때 하는 인사**는?\n\n||**바이킹**||', '**경찰서의 반대말**은?\n\n||**경찰 앉아**||',
'**숫자 5가 가장 싫어하는 집**은?\n\n||**오페라 하우스**||', '**동생과 형이 싸우는데 엄마가 동생 편만 드는 세상**은?\n\n||**형편없는 세상**||', '**미국에서 내리는 비**는?\n\n||**USB**||', '**열 명의 스님이 쉬고 있는 것**을 4글자로 줄이면?\n\n||**열중쉬어**||',
'**방금 화장실에서 나온 사람**은?\n\n||**일본 사람**||', '**늘 후회하며 타는 차**는?\n\n||**아차차**||', '**오백**에서 **백**을 빼면?\n\n||**오**||', '**여름마다 일어나는 전쟁**은?\n\n||**더워**||',
'**세상에서 가장 싸가지 없는 헤어스타일**은?\n\n||**버르장머리**||', '**손님이 뜸하면 돈 버는 사람**은?\n\n||**한의사**||', '**병균들 가운데 가장 높은 균**은?\n\n||**대장균**||', '**다 컸는데도 더 크라고 하는 동물**은?\n\n||**자라**||']
@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)
  
@slash.slash(name = "파이", description = "삐릭 삐리리릭?")
async def _파이(ctx:SlashContext):
  await ctx.send("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480665499119881834797753566369807426542527862551818417574672890977772793800081647060016145249192173217214772350141441973568548161361157352552133475741849468438523323907394143334547762416862518983569485562099219222184272550254256887671790494601653466804988627232791786085784383827967976681454100953883786360950680064225125205117392984896084128488626945604241.... **삐릭.. 삐리릭.. 펑!**")

@slash.slash(name = "찬반", description = "찬반 명령어는 찬성과 반대, 중립으로 나뉘는 투표를 게시합니다. 기본개형은 /찬반 [내용]:(내용)입니다.")
async def _찬반(ctx:SlashContext, 내용:str): 
  embed = discord.Embed(
    title=(str(내용)),
    description = "과연 결과는?? 두구두구두구..\r\n\r\n👍 - 찬성    🤝 - 중립    👎 - 반대",
    colour=0x7DB249    
  )
  embed.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/zuKJ5T6ZNhAwCkJ-Tx0C5O7QT6gMLCE7IqY3I1hJcHQ/https/media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
  em = await ctx.send(embed=embed)
  await em.add_reaction("👍")
  await em.add_reaction("🤝")
  await em.add_reaction("👎")


@slash.slash(name = "디엠", description = "파이와의 Direct Message를 시작해요")
async def _디엠(ctx:SlashContext):
  if ctx.author.dm_channel:
    embed = discord.Embed(
      title=(str(ctx.author)[:len(str(ctx.author))-5])+'님, Direct Message 대화방이 이미 존재해요',
      description = "설마 저를 잊으신 건 아니겠죠..? ;(",
      colour=0x7DB249    
    )
    embed.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/zuKJ5T6ZNhAwCkJ-Tx0C5O7QT6gMLCE7IqY3I1hJcHQ/https/media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
    embed.set_footer(text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    await ctx.send(embed=embed)
    channel = await ctx.author.create_dm()
    embed = discord.Embed(
      title=(str(ctx.author)[:len(str(ctx.author))-5])+'님, 여기에요!',
      description = "저 여기 있어요! 혹시 잊으신건 아니겠죠?? **참고로, 통신 명령어는 사용이 불가능하답니다.**",
      colour=0x7DB249    
    )
    embed.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/zuKJ5T6ZNhAwCkJ-Tx0C5O7QT6gMLCE7IqY3I1hJcHQ/https/media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
    embed.set_footer(text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    await channel.send(embed=embed)
  elif ctx.author.dm_channel is None:
    embed = discord.Embed(
      title=(str(ctx.author)[:len(str(ctx.author))-5])+'님, 새로운 Direct Message 대화방을 생성했어요',
      description = "새 Direct Message 대화방을 생성했어요 ;)",
      colour=0x7DB249    
    )
    embed.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/zuKJ5T6ZNhAwCkJ-Tx0C5O7QT6gMLCE7IqY3I1hJcHQ/https/media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
    embed.set_footer(text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    await ctx.send(embed=embed)
    channel = await ctx.author.create_dm()
    embed = discord.Embed(
      title=(str(ctx.author)[:len(str(ctx.author))-5])+'님, 여기에요!',
      description = "새로운 1대1 대화방을 만들었어요! 이곳에서 저와 DM을 주고받으실수 있답니다! **통신 명령어는 사용이 불가능해요.**",
      colour=0x7DB249    
    )
    embed.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/zuKJ5T6ZNhAwCkJ-Tx0C5O7QT6gMLCE7IqY3I1hJcHQ/https/media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
    embed.set_footer(text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    await channel.send(embed = embed)

@slash.slash(name = "패치노트", description = "최근 세 개의 버전의 수정 내역을 출력해요")
async def _패치노트(ctx:SlashContext):
  embed = discord.Embed(
    title='PATCHNOTE',
    description = "**2.3.1**\nHeroku, Github를 통한 24시간 호스팅\nSlash Command 추가\n번역 기능 추가\n룰렛 기능 추가\n도움말 기능 보완\n넌센스 기능 추가\n\n**2.0.0**\n버튼 기능 추가\n가위바위보 기능 추가\n날씨 기능 보완\n기존 명령어에 버튼 추가\n프로필에 서버에 추가 버튼 추가\n.자기소개명령어에도 서버에 추가 버튼 추가\n\n**1.9.2**\n날씨 기능 보완\n날씨 기능 오류 수정\n핑 명령어 추가",
    colour=0x7DB249    
  )
  embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
  embed.set_footer(text="패치노트에는 최근 세 개의 버전만 표기됩니다.\nCopyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
  await ctx.send(embed=embed)

@slash.slash(name = "밥추천", description = "음식 데이터베이스를 바탕으로 랜덤한 음식을 추천해줘요")
async def _밥추천(ctx:SlashContext):
    embed = discord.Embed(
        title='오늘의 밥으로는 ' + random.choice(food) + " 어때?",
        description=
        "내가 알고 있는 음식의 종류로는 대략 30여가지의 음식이 있어. 혹시 네가 알고 있는 색다른 음식이 있다면 개발자에게 보내줘!",
        colour=0x7DB249)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
    await ctx.send(embed=embed)

@slash.slash(name = "도박", description = "가운데의 가로줄이 같은 과일이 나오면 당첨!")
async def _도박(ctx:SlashContext):
  global excel
  excel = 1
  global first
  global sec
  global third
  global fourth
  global fif
  global six
  global sev
  global eig
  global nin
  while excel < 10:
    num = random.randrange(1, 6)
    if excel == 1:
      if num == 1:
        first = ":cherries:"
      elif num == 2:
        first = ":tangerine:"
      elif num == 3:
        first = ":watermelon:"
      elif num == 4:
        first = ":peach:"
      else:
        first = ":crown:"
    elif excel == 2:
      if num == 1:
        sec = ":cherries:"
      elif num == 2:
        sec = ":tangerine:"
      elif num == 3:
        sec = ":watermelon:"
      elif num == 4:
        sec = ":peach:"
      else:
        sec = ":crown:"
    elif excel == 3:
      if num == 1:
        third = ":cherries:"
      elif num == 2:
        third = ":tangerine:"
      elif num == 3:
        third = ":watermelon:"
      elif num == 4:
        third = ":peach:"
      else:
        third = ":crown:"
    elif excel == 4:
      if num == 1:
        fourth = ":cherries:"
      elif num == 2:
        fourth = ":tangerine:"
      elif num == 3:
        fourth = ":watermelon:"
      elif num == 4:
        fourth = ":peach:"
      else:
        fourth = ":crown:"
    elif excel == 5:
      if num == 1:
        fif = ":cherries:"
      elif num == 2:
        fif = ":tangerine:"
      elif num == 3:
        fif = ":watermelon:"
      elif num == 4:
        fif = ":peach:"
      else:
        fif = ":crown:"
    elif excel == 6:
      if num == 1:
        six = ":cherries:"
      elif num == 2:
        six = ":tangerine:"
      elif num == 3:
        six = ":watermelon:"
      elif num == 4:
        six = ":peach:"
      else:
        six = ":crown:"
    elif excel == 7:
      if num == 1:
        sev = ":cherries:"
      elif num == 2:
        sev = ":tangerine:"
      elif num == 3:
        sev = ":watermelon:"
      elif num == 4:
        sev = ":peach:"
      else:
        sev = ":crown:"
    elif excel == 8:
      if num == 1:
        eig = ":cherries:"
      elif num == 2:
        eig = ":tangerine:"
      elif num == 3:
        eig = ":watermelon:"
      elif num == 4:
        eig = ":peach:"
      else:
        eig = ":crown:"
    elif excel == 9:
      if num == 1:
        nin = ":cherries:"
      elif num == 2:
        nin = ":tangerine:"
      elif num == 3:
        nin = ":watermelon:"
      elif num == 4:
        nin = ":peach:"
      else:
        nin = ":crown:"
      
    num = random.randrange(1, 6)
    excel = excel+1
  global ddangcheum
  ddangcheum = "쫘라라라락"

  if fourth == fif and fif == six:
    ddangcheum = "오옹! 당첨이야!! 축하해 :partying_face:"
      
  
  info = ":small_orange_diamond::small_orange_diamond::small_orange_diamond::small_orange_diamond::small_orange_diamond:\n:small_orange_diamond:"+first+sec+third+":small_orange_diamond:\n:small_orange_diamond:"+fourth+fif+six+":small_orange_diamond:\n:small_orange_diamond:"+sev+eig+nin+":small_orange_diamond:\n:small_orange_diamond::small_orange_diamond::small_orange_diamond::small_orange_diamond::small_orange_diamond:"
  embed = discord.Embed(title=ddangcheum, description = info+"\n세개 모두 같은 줄이 나오면 당첨!", colour=0x7DB249)
  embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
  await ctx.send(embed=embed)
  
@slash.slash(name = "운세", description = "오늘의 운세를 랜덤으로 뽑아줘요")
async def _운세(ctx:SlashContext):
    num = random.randrange(1, 101)
    num = str(num)

    embed = discord.Embed(title='오늘의 운세는!', colour=0x7DB249)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
    embed.add_field(name='> 재미로 보는 오늘의 운세!',
                    value='네가 ' + random.choice(Random) + num +
                    '% 야! **재미로만 보는것이니 기분 안 나빠했으면 좋겠어!!**')
    await ctx.send(embed=embed)

@slash.slash(name = "규칙", description = "파이 공식 서버에서 지켜야 할 규칙들을 말해줘요", guild_ids=[933687912103571536])
async def _규칙(ctx:SlashContext):
  embed = discord.Embed(
    title = "이 서버에서 지켜야할 규칙들이야, 한번 자세히 읽어 봐",
    description = "사고팔기 금지 (만일 피해가 발생할 시에는 책임지지 않음)\r\n욕설, 타인에 대해 비방 금지\r\n정치, 사회적 발언 금지\r\n개인 간에 서버에 대한 개인 체팅 금지 (걸릴 시에는 추방)\r\n대화 내용을 캡쳐하여 올리지 않기 (관리자가 승인한 경우, 허용)\r\n봇 해킹 금지(어길시에는 법적 대응, 영구 추방)\r\n\r\n위의 내용을 5회 어길 시 **영구 추방**됩니다.",
    colour = 0x7DB249
  )
  embed.set_thumbnail(url=  "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.png"
    )
  embed.set_footer(text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
  await ctx.send(embed=embed)

@slash.slash(name = "홈페이지", description = "Esusin Laboratory 홈페이지를 방문하세요")
async def _홈페이지(ctx:SlashContext):
  embed = discord.Embed(
    title = "Esusin Laboratory 공식 홈페이지야",
    description = "이곳에는 제작자분의 여러가지 소프트웨어가 있어. 모두 무료야! 아래 버튼을 누르면 홈페이지로 이동이 돼!",
    colour = 0x7DB249
  )
  embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
  await ctx.send(embed=embed)
  await buttons.send(
    content = None,
    channel = ctx.channel.id,
    components = [
      ActionRow([
        Button(
          label = "Esusin Laboratory 홈페이지로 이동",
          style = ButtonType().Link,
          url = "http://esusinlab.bu.to/"
        )
      ])
    ]
  )


@buttons.click
async def button_one(ctx):
  value = random.randrange(1, 4)
  winlose = "none"
  if value == 1:
    value = ":v:"
    winlose = "어이쿠! 비겼네!"
    img = "https://media.discordapp.net/attachments/933687912950808608/962557303364657152/110_20220410123521.png"
  elif value == 2:
    value = ":raised_hand:"
    winlose = "에잇... 졌군..."
    img = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png"
  else:
    value = ":fist:"
    winlose = "하ㅏ하ㅏ 내가 이겼다!!"
    img = "https://media.discordapp.net/attachments/918381996483424306/962556561287413840/110_20220410122834.png"
  embed = discord.Embed(
      title= winlose,
      description= value+" 가위바위보는 randrange 함수를 이용해서 만든 기능이야 절대 닼흐봇을 따라한게 아니라구 크흠..",
      colour=0x7DB249)
  embed.set_thumbnail(url=img)
  await ctx.channel.send(embed = embed)

@buttons.click
async def button_two(ctx):
  value = random.randrange(1, 4)
  winlose = "none"
  if value == 1:
    value = ":v:"
    winlose = "에잇... 졌군..."
    img = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png"
  elif value == 2:
    value = ":raised_hand:"
    winlose = "하ㅏ하ㅏ 내가 이겼다!!"
    img = "https://media.discordapp.net/attachments/918381996483424306/962556561287413840/110_20220410122834.png"
  else:
    value = ":fist:"
    winlose = "어이쿠! 비겼네!"
    img = "https://media.discordapp.net/attachments/933687912950808608/962557303364657152/110_20220410123521.png"
  embed = discord.Embed(
      title= winlose,
      description= value+" 가위바위보는 randrange 함수를 이용해서 만든 기능이야 절대 닼흐봇을 따라한게 아니라구 크흠..",
      colour=0x7DB249)
  embed.set_thumbnail(url=img)
  await ctx.channel.send(embed = embed)

@buttons.click
async def button_three(ctx):
  value = random.randrange(1, 4)
  winlose = "none"
  if value == 1:
    value = ":v:"
    winlose = "하ㅏ하ㅏ 내가 이겼다!!"
    img = "https://media.discordapp.net/attachments/918381996483424306/962556561287413840/110_20220410122834.png"
  elif value == 2:
    value = ":raised_hand:"
    winlose = "어이쿠! 비겼네!"
    img = "https://media.discordapp.net/attachments/933687912950808608/962557303364657152/110_20220410123521.png"
  else:
    value = ":fist:"
    winlose = "에잇... 졌군..."
    img = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png"
  embed = discord.Embed(
      title= winlose,
      description= value+" 가위바위보는 randrange 함수를 이용해서 만든 기능이야 절대 닼흐봇을 따라한게 아니라구 크흠..",
      colour=0x7DB249)
  embed.set_thumbnail(url=img)
  await ctx.channel.send(embed = embed)

@slash.slash(name = "가위바위보", description = "가위바위보 한 판 해요!")
async def _가위바위보(ctx:SlashContext):
    embed = discord.Embed(
        title= '안 내면 진다',
        description="가위바위....\r\n:v: :raised_hand: :fist:",
        colour=0x7DB249)
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.png"
    )
    await ctx.send(embed=embed)
    await buttons.send(
      content = None,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label = "가위",
            style = ButtonType().Primary,
            custom_id="button_one"
          ),
          Button(
            label = "바위",
            style = ButtonType().Primary,
            custom_id="button_two"
          ),
          Button(
            label = "보",
            style = ButtonType().Primary,
            custom_id="button_three"
          )
        ])
      ]
    )
  

@slash.slash(name = "자기소개", description = "파이를 처음 사용할 때 필요할 만한 정보들을 제공해줘요")
async def _자기소개(ctx:SlashContext):
    embed = discord.Embed(
        title='안녕! 만나서 반가워!',
        description="나는 파이라고 해! 나에 대해 궁금해 할 것 같은 항목들을 몇 개 가져와봤어!",
        colour=0x7DB249)
    embed.add_field(name='> 이름', value='파이')
    embed.add_field(name='> 직업', value='디스코드 봇')
    embed.add_field(name='> 시작 구문', value='.')
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.png"
    )
    embed.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    await ctx.send(embed=embed)
    await buttons.send(
      content = None,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label = "파이 자기소개 보기",
            style = ButtonType().Link,
            url = "http://esusinlabpie.bu.to/"
          ),
          Button(
            label = "파이 명령어 모음집(업데이트 중단, /도움말을 사용하세요)",
            style = ButtonType().Link,
            url = "http://esusinlabpiehelp.bu.to/"
          ),
          Button(
            label = "서버에 추가",
            style = ButtonType().Link,
            url = "https://discord.com/api/oauth2/authorize?client_id=960134947698540595&permissions=8&scope=bot"
          )
        ])
      ]
    )

@bot.command()
async def 우히히히(ctx):
  await ctx.channel.send("우히ㅣ히")

@slash.slash(name = "관리자", description = "파이의 관리자들을 리스트 형식으로 출력해줘요")
async def _관리자(ctx:SlashContext):
    embed = discord.Embed(title='나에 대한 모든 권한을 가지고 있는 분들이야!',
                          description="이분들은 이분들만의 특별한 명령어를 사용할 수 있어!",
                          colour=0x7DB249)
    embed.add_field(name='> 관리자 목록', value=Administrator)
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.png"
    )
    await ctx.send(embed=embed)


@slash.slash(name = "검색", description = "검색 명령어는 Microsoft Bing에서 검색 결과를 보여줍니다. 기본개형은 /검색 [검색]:(내용)입니다.")
async def _검색(ctx:SlashContext, 검색:str):
    msg = 검색
    thumbnail = msg  
    msg = msg.replace(' ', '%20')
    embed = discord.Embed(title='자, 여기 네가 원하는 결과가 기다리고 있어!', colour=0xff7676)
    await ctx.send(embed=embed)
    await buttons.send(
      content = None,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label = thumbnail+" 검색 결과 보기",
            style = ButtonType().Link,
            url = "https://www.bing.com/search?q=" + msg
          )
        ])
      ]
    )


@slash.slash(name = "스크립트", description = "스크립트 명령어에 관한 도움말을 보여줘요")
async def _스크립트(ctx:SlashContext):
    embed = discord.Embed(
        title=':page_with_curl: 스크립트 명령어에 대해서...',
        description=
        "'스크립트 명령어는 `/(스크립트 지원 명령어) [값]:(인자)`의 형태로 사용 가능...' 이라고 나와 있군..!!",
        colour=0x7DB249)
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.ight=625"
    )
    await ctx.channel.send(embed=embed)


@slash.slash(name = "놀이", description = "놀이 리스트를 보여줘요")
async def _놀이(ctx:SlashContext):
    embed = discord.Embed(title='같이 놀자!', colour=0x7DB249)
    embed.add_field(name='> 놀이 명령어', value='/운세\r\n/밥추천\r\n/도박\r\n/가위바위보')
    embed.add_field(name='> 스크립트 놀이 명령어', value='/더하기')
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.ight=625"
    )
    await ctx.send(embed=embed)


@slash.slash(name = "더하기", description = "더하기 명령어는 리스트에서 랜덤으로 결과값을 반환합니다. /더하기 [내용1]:(내용) [내용2]:(내용)이 기본개형입니다.")
async def _더하기(ctx:SlashContext, 내용1:str, 내용2:str):
    value1 = 내용1
    value2 = 내용2
    embed = discord.Embed(
        title=value1 + "와(과)" + value2 + "을(를) 합성해보자..!!",
        description="||" + random.choice(random2) + "||(이)가 나왔네 ㅋㅋ",
        colour=0x7DB249)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.ight=625")
    await ctx.send(embed=embed)


@slash.slash(name = "유튜브", description = "유튜브 명령어는 유튜브에서 동영상을 검색해줍니다. 기본개형은 /유튜브 [검색]:(내용)입니다.")
async def _유튜브(ctx:SlashContext, 검색:str):
    msg = 검색
    thumbnail = msg
    msg = msg.replace(' ', '%20')
    embed = discord.Embed(title='자, 여기 너가 원하는 YouTube 동영상이 기다리고 있어!',
                          description = "아래의 버튼을 눌러서 YouTube로 이동할 수 있어!",
                          colour=0xff7676)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/929576166740873231/972691405665353769/110_20220508114729.png"
    )
    await ctx.send(embed = embed)
    await buttons.send(
      content = None,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label = thumbnail+' - YouTube',
            style = ButtonType().Link,
            url = "https://www.youtube.com/results?search_query=" + msg
          )
        ])
      ]
    )


@slash.slash(name = "날씨", description = "날씨 명령어는 해당 지역의 날씨를 실시간으로 알려줍니다. 기본개형은 /날씨 [지역명]:(지역명)입니다.")
async def _날씨(ctx:SlashContext, 지역명:str):
    global msg
    msg = 지역명
    global which
    global status
    global current
    global rain
    global body
    global wet
    global windblow
    global sea
    global url
    which = 0
    status = 0
    current = 0
    rain = 0
    body = 0
    wet = 0
    windblow = 0
    sea = 0
    url = 0
    embed = discord.Embed(
        title=msg+" 지역의 날씨를 가져올게!",
        description=
            "데이터가 많이 있으면 처리하는데 시간이 많이 걸릴 수도 있어! 잠시만 기다려줘!",
        colour=0xB8E9FF)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303364657152/110_20220410123521.png")
    await ctx.channel.send(embed=embed)
    if (msg == "서울"):
        url = "https://weather.naver.com/today/09140104"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "백령도"):
        url = "https://weather.naver.com/today/11720330"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "제주도"):
        url = "https://weather.naver.com/today/14130116"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "춘천"):
        url = "https://weather.naver.com/today/01110675"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "강릉"):
        url = "https://weather.naver.com/today/01150615"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "청주"):
        url = "https://weather.naver.com/today/16111120"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "수원"):
        url = "https://weather.naver.com/today/02113128"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "독도"):
        url = "https://weather.naver.com/today/04940320"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "울릉도"):
        url = "https://weather.naver.com/today/04940320"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "인천"):
        url = "https://weather.naver.com/today/11200510"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "안동"):
        url = "https://weather.naver.com/today/04170690"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "대전"):
        url = "https://weather.naver.com/today/07110101"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "전주"):
        url = "https://weather.naver.com/today/13113135"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "대구"):
        url = "https://weather.naver.com/today/06110101"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "광주"):
        url = "https://weather.naver.com/today/05110101"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "울산"):
        url = "https://weather.naver.com/today/10110101"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "부산"):
        url = "https://weather.naver.com/today/08110580"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "여수"):
        url = "https://weather.naver.com/today/12130127"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "목포"):
        url = "https://weather.naver.com/today/12110152"
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        which = msg
        status = soup.find("span", class_="weather")
        status = status.get_text()
        status = str(status)
        current = soup.find("strong", class_="current")
        current = current.get_text()
        current = str(current)
        current = (current[6:len(current)-2])
        rain = soup.find("ul", class_="box_color")
        rain = rain.get_text()
        rain = str(rain)
    elif (msg == "?"):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title="날씨 데이터베이스에 저장되어 있는 지역들",
            description=
            "서울, 백령도, 제주도, 춘천, 인천, 강릉, 울릉도, 독도, 전주, 대전, 수원, 안동, 울산, 광주, 청주, 목포, 여수, 부산, 울산, 제주도\n\n`/날씨 [지역명]:(지역명)`",
            colour=0xB8E9FF)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
        await ctx.send(embed=embed)
    else:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title=msg+" 지역을 찾을 수 없어 ;(",
            description=
            "서울, 백령도, 제주도, 춘천, 인천, 강릉, 울릉도, 독도, 전주, 대전, 수원, 안동, 울산, 광주, 청주, 목포, 여수, 부산, 울산, 제주도\n\n`/날씨 [지역명]:(지역명)`\n\n`ERROR : valueable varients 'msg' is not int value, line 948, in main.py`",
            colour=0xB8E9FF)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
        await ctx.send(embed=embed)

      
    if not (which == 0):
        current = round(float(current))
        current = str(current)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title=":sunny: 오늘 " + which + "의 날씨는",
                              description="오늘의 날씨는 대체적으로 " + status +
                              "이네요! 기온은 " + current + "°C에요. ;) 더 자세한 내용을 보려면 아래 버튼을 눌러주세요.",
                              colour=0xB8E9FF)
        embed.set_footer(text="Copyright Ⓒ NAVER Corp. All rights reserved.")
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
        await ctx.send(embed=embed)
        await buttons.send(
          content = None,
          channel = ctx.channel.id,
          components = [
            ActionRow([
              Button(
                label = "NAVER에서 보기",
                style = ButtonType().Link,
                url = url
              )
            ])
          ]
        )


@slash.slash(name = "빌보드", description = "저 멀리 바다 건너에 있는 빌보드 차트를 가져와요")
async def _빌보드(ctx:SlashContext):
    embed = discord.Embed(
        title="빌보드 차트에서 데이터를 가져오는 중이야!",
        description=
            "데이터가 많이 있으면 처리하는데 시간이 많이 걸릴 수도 있어! 잠시만 기다려줘!",
        colour=0xB8E9FF)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303364657152/110_20220410123521.png")
    await ctx.channel.send(embed = embed)    
    url = "https://www.billboard.com/charts/hot-100/"
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    s = soup.find('a', class_='c-title__link lrv-a-unstyle-link')
    s = s.get_text()
    s = str(s)
    s = s[11:len(s) - 8]
    q = s.replace(' ', '%20')
    i = (
        "현재의 빌보드 차트 1위는 " + s +
        "이야! **저 멀리 바다 건너**에서 데이터를 가져오느라 조금 늦었네.. 미안!"
        )
  
    
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="[TOP 1] " + s, description=i, colour=0x000000)
    embed.set_footer(
        text=
        "Billboard is a part of Penske Media Corporation. © 2022 Billboard Media, LLC. All Rights Reserved."
    )
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
    await ctx.send(embed=embed)
    await buttons.send(
      content = None,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label = "Billboard Hot 100",
            style = ButtonType().Link,
            url = "https://www.billboard.com/charts/hot-100/"
          ),
          Button(
            label = "YouTube에서 보기",
            style = ButtonType().Link,
            url = "https://www.youtube.com/results?search_query="+q
          )
        ])
      ]
    )
@slash.slash(name = "뉴스", description = "최신 뉴스를 랜덤으로 배달해줘요")
async def _뉴스(ctx:SlashContext):
    embed = discord.Embed(
        title="새 소식 전달중..!",
        description=
            "데이터가 많이 있으면 처리하는데 시간이 많이 걸릴 수도 있어! 잠시만 기다려줘!",
        colour=0xB8E9FF)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303364657152/110_20220410123521.png")
    await ctx.channel.send(embed=embed)
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104"
    page = urllib.request.urlopen(url)
    html = page.read().decode('cp949')
    soup = BeautifulSoup(html, 'html.parser')
    s = soup.find('a', class_='cluster_text_headline nclicks(cls_wor.clsart)')
    s = s.get_text()
    s = str(s)
    i = soup.find('div', class_='cluster_text_lede')
    i = i.get_text()
    i = str(i)
  
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=s, description=i, colour=0xDDECCA)
    embed.set_footer(text="Copyright Ⓒ NAVER Corp. All rights reserved.")
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
    await ctx.send(embed=embed)
    await buttons.send(
      content = None,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label = "NAVER 뉴스로 이동",
            style = ButtonType().Link,
            url = url
          )
        ])
      ]
    )


@slash.slash(name = "코로나", description = "일일 코로나 확진자를 보여줘요")
async def _코로나(ctx:SlashContext):
    embed = discord.Embed(
        title="네이버에서 검색해보고 있어, 좀만 기다려 봐!",
        description=
            "데이터가 많이 있으면 처리하는데 시간이 많이 걸릴 수도 있어! 잠시만 기다려줘!",
        colour=0xB8E9FF)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303364657152/110_20220410123521.png")
    await ctx.channel.send(embed=embed)
    url = "https://search.naver.com/search.naver?ie=UTF-8&query=covid-19&sm=chr_hty"
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    cur = soup.find("p", class_="info_num")
    cur = cur.get_text()
    cur = str(cur)
    severe = soup.find("li", class_="info_02")
    severe = severe.get_text()
    severe = (str(severe)[7:len(severe) - 1])
    new = soup.find("li", class_="info_03")
    new = new.get_text()
    new = (str(new)[6:len(new) - 1])
    die = soup.find("li", class_="info_04")
    die = die.get_text()
    die = (str(die)[6:len(die) - 1])
  
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=":mask: 마스크와 손씻기만으로도 코로나 감염을 예방할 수 있습니다",
                          colour=0xDDECCA)
    embed.add_field(name='**일일 확진자**', value=cur + "명")
    embed.add_field(name='**위중증 환자**', value=severe + "명")
    embed.add_field(name='**신규 입원**', value=new + "명")
    embed.add_field(name='**일일 사망자**', value=die + "명")
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
    embed.set_footer(text="Copyright Ⓒ NAVER Corp. All rights reserved.")
    await ctx.send(embed=embed)
    await buttons.send(
      content = None,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label = "NAVER에서 보기",
            style = ButtonType().Link,
            url = url
          )
        ])
      ]
    )


@slash.slash(name = "롤", description = "롤 명령어를 사용하면 op.gg에서 해당 소환사에 대한 정보를 출력해줍니다. 기본개형은 /롤 [소환사]:(소환사명)입니다.")
async def _롤(ctx:SlashContext, 소환사:str):
    msg = 소환사
    msg = msg.replace(' ', '%20')
    embed = discord.Embed(title='휴.. opgg에서 네가 바란 것을 찾았어',
                          description = "참고로 난 소규모 서버라 이런것 하나 검색하는 데 렉이 많이 걸려",
                          colour=0xff7676)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561287413840/110_20220410122834.png")
    await ctx.send(embed=embed)
    await buttons.send(
      content = None,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label = "op.gg로 이동",
            style = ButtonType().Link,
            url = "https://www.op.gg/summoner/userName=" + msg
          )
        ])
      ]
    )


@slash.slash(name = "정보", description = "소프트웨어 정보를 보여줘요")
async def _정보(ctx:SlashContext):
    embed = discord.Embed(
        title='정보',
        colour=0x7DB249)
    embed.add_field(name='> 소프트웨어 버전', value='`2.2.3` **Waiotapu**')
    embed.add_field(name='> 언어 버전', value='`Python® Discord.py Module Version 1.7.3`')
    embed.add_field(name='> 라이센스', value='`Official`')
    embed.add_field(name='> 빌드', value='`Build 22096.87.21`')
    embed.set_footer(
        text=
        "Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.\n소프트웨어가 최신 버전입니다."
    )
    await ctx.send(embed=embed)

@slash.slash(name = "핑", description = "파이의 현재 상태를 보여줘요")
async def _핑(ctx:SlashContext):
    print(str(bot.latency * 1000))
    if round(bot.latency * 1000) <= 50:
        embed=discord.Embed(title="요즘 탁구를 배우고 있어!", description = f"지금 나의 핑은 **{round(bot.latency *1000)}**ms야! 메시지의 색깔에 따라서 지금 서버의 상태를 간단하게 확인할수 있어!", color=0x44ff44)
    elif round(bot.latency * 1000) <= 100:
        embed=discord.Embed(title="요즘 탁구를 배우고 있어!", description = f"지금 나의 핑은 **{round(bot.latency *1000)}**ms야! 메시지의 색깔에 따라서 지금 서버의 상태를 간단하게 확인할수 있어!", color=0xffd000)
    elif round(bot.latency * 1000) <= 200:
        embed=discord.Embed(title="요즘 탁구를 배우고 있어!", description = f"지금 나의 핑은 **{round(bot.latency *1000)}**ms야! 메시지의 색깔에 따라서 지금 서버의 상태를 간단하게 확인할수 있어!", color=0xff6600)
    else:
        embed=discord.Embed(title="요즘 탁구를 배우고 있어!", description = f"지금 나의 핑은 **{round(bot.latency *1000)}**ms야! 메시지의 색깔에 따라서 지금 서버의 상태를 간단하게 확인할수 있어!", color=0x990000)
    
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561287413840/110_20220410122834.png")
    embed.set_footer(
        text=
        "Copyright Ⓒ 2017-2022 Esusinlab All rights reserved."
    )
    await ctx.send(embed=embed)

#관리자
@slash.slash(name = "삭제", description = "삭제 명령어는 숫자의 갯수만큼 메시지를 삭제합니다. 기본개형은 /삭제 [메시지 개수]:(숫자)입니다")
async def _삭제(ctx:SlashContext, 메시지_개수:str):
    if ctx.author.name in Administrator:
      msg = int(메시지_개수)
      if msg > 19:
        embed = discord.Embed(
            title='미안해 ;(',
            description=
            "미안하지만, '.삭제' 명령어는 남용을 방지하기 위해 한번에 20개 이상 삭제할 수 없어..\n`ERROR : valueable varients 'msg' is not int value, line 1195, in main.py`",
            colour=0xff7676)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
        await ctx.send(embed=embed)
      elif msg < 20:
        await ctx.channel.purge(limit=msg)
        embed = discord.Embed(
            title='작업을 완료하였어요',
            description=
            "메시지 "+str(msg)+"개를 삭제했어요",
            colour=0xff7676)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title='미안해 ;(',
            description=
            "> 미안하지만, '.삭제'는 관리자 전용 명령어야. 그래서 너의 권한으로는 '.삭제'명령어를 사용할 수 없어..",
            colour=0xff7676)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
        embed.add_field(name='> 관리자 목록', value='.관리자')
        await ctx.channel.send(embed=embed)


#관리자
@slash.slash(name = "얼차려", description = "파이가 모든 유저들을 맨션해요")
async def _얼차려(ctx:SlashContext):
    if ctx.author.name in Administrator:
        await ctx.send("@everyone 다들 얼차렷!")

    else:
        embed = discord.Embed(
            title='미안해 ;(',
            description=
            "> 미안하지만, '/얼차려'는 관리자 전용 명령어야. 그래서 너의 권한으로는 '/얼차려'명령어를 사용할 수 없어..",
            colour=0xff7676)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
        embed.add_field(name='> 관리자 목록', value='.관리자')
        await ctx.send(embed=embed)


@slash.slash(name = "도움말", description = "파이의 도움말을 페이지 형식으로 보여줘요")
async def _도움말(ctx:SlashContext):
  global msg
  global msge
  global event
  global embed
  global embed_page_2
  global embed_page_3
  global embed_page_4
  global embed_page_5
  global page_num
  global msg2
  msg2 = 0
  if True:
    page_num = 1
    embed = discord.Embed(
        title='1페이지',
        description="파이 디스코드 봇을 사용해주셔서 감사합니다.\n 귀하는 현재 **5쪽 중 1쪽**에 위치해 있습니다.",
        colour=0x7DB249)
    embed.add_field(name="/도움말", value="도움말 명령어는 이 메시지를 띄웁니다. 도움말 명령어에 대해 자세히 알아보려면 `/도움말`을 입력하십시오.", inline = False)
    embed.add_field(name="/자기소개", value="자기소개 명령어는 봇에 대한 간단한 정보를 보여줍니다. 세부 내용을 보려면 `/정보`명령어를 입력하십시오.", inline = False)
    embed.add_field(name="/관리자", value="관리자 명령어는 관리자 권한이 부여된 사용자의 리스트를 출력합니다.", inline = False)
    embed.add_field(name="/정보", value="정보 명령어는 봇의 세부적인 정보를 띄웁니다. 보다 간단한 정보는 `/자기소개`명령어 문서를 참고하십시오.", inline = False)
    embed.add_field(name="/스크립트", value="스크립트 명령어는 조합 가능한 명령어를 사용하는 방법을 출력합니다.", inline = False)
    embed.add_field(name="/더하기", value="더하기 명령어는 리스트에서 랜덤으로 결과값을 반환합니다. `/더하기 [내용1]:(내용) [내용2]:(내용)`이 기본개형입니다.", inline = False)
    embed.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    
    embed_page_2 = discord.Embed(
        title='2페이지',
        description="파이 디스코드 봇을 사용해주셔서 감사합니다.\n 귀하는 현재 **5쪽 중 2쪽**에 위치해 있습니다.",
        colour=0x7DB249)
    embed_page_2.add_field(name="/롤", value="롤 명령어를 사용하면 op.gg에서 해당 소환사에 대한 정보를 출력해줍니다. 기본개형은 `/롤 [소환사]:(소환사명)`입니다.", inline = False)
    embed_page_2.add_field(name="/검색", value="검색 명령어는 Microsoft Bing에서 검색 결과를 보여줍니다. 기본개형은 `/검색 [검색]:(내용)`입니다.", inline = False)
    embed_page_2.add_field(name="/유튜브", value="유튜브 명령어는 유튜브에서 동영상을 검색해줍니다. 기본개형은 `/유튜브 [검색]:(내용)`입니다.", inline = False)
    embed_page_2.add_field(name="/날씨", value="날씨 명령어는 해당 지역의 날씨를 실시간으로 알려줍니다. 기본개형은 `/날씨 [지역명]:(지역명)`입니다. 자세한 내용을 보려면 `/날씨 [지역명]:?` 명령어를 사용하십시오.", inline = False)
    embed_page_2.add_field(name="/운세", value="운세 명령어는 오늘의 운세를 랜덤으로 출력합니다.", inline = False)
    embed_page_2.add_field(name="/밥추천", value="밥추천 명령어는 밥을 랜덤으로 추천해줍니다.", inline = False)
    embed_page_2.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    embed_page_3 = discord.Embed(
        title='3페이지',
        description="파이 디스코드 봇을 사용해주셔서 감사합니다.\n 귀하는 현재 **5쪽 중 3쪽**에 위치해 있습니다.",
        colour=0x7DB249)
    embed_page_3.add_field(name="/빌보드", value="빌보드 명령어는 실시간으로 갱신되는 빌보드 차트 1위 음악을 알려주며, 그 음악을 유튜브에서 찾아 줍니다.", inline = False)
    embed_page_3.add_field(name="/코로나", value="코로나 명령어는 매일 갱신되는 코로나 확진자 수와 일일 사망자 수 등을 출력합니다.", inline = False)
    embed_page_3.add_field(name="/뉴스", value="뉴스 명령어는 현재 업로드된 가장 최근 기사를 출력합니다. 명령어를 사용하면 나오는 버튼을 눌러 뉴스 페이지로 이동할 수 있습니다.", inline = False)
    embed_page_3.add_field(name="/패치노트", value="패치노트 명령어는 최근 업데이트 내역을 출력합니다.", inline = False)
    embed_page_3.add_field(name="/홈페이지", value="홈페이지 명령어는 파이 디스코드 봇 제조사 홈페이지를 띄웁니다.", inline = False)
    embed_page_3.add_field(name="/찬반", value="찬반 명령어는 찬성과 반대, 중립으로 나뉘는 투표를 게시합니다. 기본개형은 `/찬반 [내용]:(내용)`입니다.", inline = False)
    embed_page_3.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    embed_page_4 = discord.Embed(
        title='4페이지',
        description="파이 디스코드 봇을 사용해주셔서 감사합니다.\n 귀하는 현재 **5쪽 중 4쪽**에 위치해 있습니다.",
        colour=0x7DB249)
    embed_page_4.add_field(name="/핑", value="핑 명령어는 현재 봇의 핑을 출력합니다. 서버의 상태에 따라 메시지 색깔이 달라집니다.", inline = False)
    embed_page_4.add_field(name="/디엠", value="디엠 명령어는 파이 디스코드 봇과의 1:1 대화방을 생성합니다.", inline = False)
    embed_page_4.add_field(name="/룰렛", value="룰렛 명령어는 항목을 랜덤으로 뽑아줍니다. 기본개형은 `/룰렛 [항목]:(항목1)/(항목2)/(항목3)/....../(항목n)`입니다.", inline = False)
    embed_page_4.add_field(name="/가위바위보", value="가위바위보 명령어는 버튼을 눌러 봇과 가위바위보 대결을 하는 게임입니다.", inline = False)
    embed_page_4.add_field(name="/놀이", value="놀이 명령어는 플레이 가능한 게임 리스트를 출력합니다.", inline = False)
    embed_page_4.add_field(name="/도박", value="도박 명령어는 랜덤으로 나오는 과일의 가운데 세 줄이 왕관이면 당첨이 되는 게임입니다.", inline = False)
    embed_page_4.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    embed_page_5 = discord.Embed(
        title='5페이지',
        description="파이 디스코드 봇을 사용해주셔서 감사합니다.\n 귀하는 현재 **5쪽 중 5쪽**에 위치해 있습니다.",
        colour=0x7DB249)
    embed_page_5.add_field(name="/번역", value="번역 명령어는 여러 가지의 언어로 번역을 해 주는 명령어입니다. 기본개형은 `/번역 [내용]:(내용) [언어명]:(언어명)`입니다.", inline = False)
    embed_page_5.add_field(name="/넌센스", value="넌센스 명령어는 재미있는 넌센스 퀴즈를 내 주는 명령어입니다.", inline = False)
    embed_page_5.add_field(name="/삭제", value="삭제 명령어는 숫자의 갯수만큼 메시지를 삭제합니다. 기본개형은 `/삭제 [메시지 개수]:(숫자)`이며, 관리자만 사용할 수 있습니다. 삭제 명령어는 남용 방지를 위해 한번에 19개 까지만 삭제 가능합니다.", inline = False)
    embed_page_5.add_field(name="/얼차려", value="얼차려 명령어는 서버에 있는 모두를 맨션합니다. 이 명령어는 관리자만 사용할 수 있습니다.", inline = False)
    embed_page_5.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    
    msge = await ctx.send(embed = embed)
    await buttons.send(content = None, channel = ctx.channel.id, components = [ActionRow([Button(label = "이전 페이지", style = ButtonType().Primary, custom_id="help_prior"),Button(label = "다음 페이지", style = ButtonType().Primary, custom_id="help_next")])])
    
    event = await bot.wait_for("button_click", timeout=60.0)

@buttons.click
async def help_next(ctx):
  global page_num
  global event
  global msg2
  page_num = page_num+1
  if page_num == 6:
    page_num = 1
  if page_num == 1:
    await msge.edit(embed = embed)
  elif page_num == 2:
    await msge.edit(embed = embed_page_2)
  elif page_num == 3:
    await msge.edit(embed = embed_page_3)
  elif page_num == 4:
    await msge.edit(embed = embed_page_4)
  elif page_num == 5:
    await msge.edit(embed = embed_page_5)
  await ctx.reply("다음 페이지로 넘겼습니다.")
  await event.respond(type=6)

@buttons.click
async def help_prior(ctx):
  global page_num
  global event
  page_num = page_num-1
  if page_num == 0:
    page_num = 5
  if page_num == 1:
    await msge.edit(embed = embed)
  elif page_num == 2:
    await msge.edit(embed = embed_page_2)
  elif page_num == 3:
    await msge.edit(embed = embed_page_3)
  elif page_num == 4:
    await msge.edit(embed = embed_page_4)
  elif page_num == 5:
    await msge.edit(embed = embed_page_5)
  await ctx.reply("이전 페이지로 넘겼습니다.")
  await event.respond(type=6)

@slash.slash(name = "번역", description = "번역 명령어는 여러 가지의 언어로 번역을 해 주는 명령어입니다. 번역 명령어에 관한 문서를 보려면 `/도움말`을 참조하십시오.")
async def _번역(ctx:SlashContext, 내용:str, 언어명:str):
  r1 = 1
  if r1 == 1:
    global langtrans
    translator = Translator()
    content = 내용
    lang = 언어명
    if lang == "한국어" or lang == "일본어" or lang == "중국어 번체" or  lang == "중국어 간체" or lang == "영어":
      if lang == "한국어":
        langtrans = "ko"
      elif lang == "일본어":
        langtrans = "ja"
      elif lang == "중국어 번체":
        langtrans = "zh-tw"
      elif lang == "중국어 간체":
        langtrans = "zh-cn"
      elif lang == "영어":
        langtrans = "en"
      result = translator.translate(content, dest=langtrans)
      print(result)
      embed = discord.Embed(title=content+'를 '+lang+'로 번역해봤어!', description=content+'를 '+lang+'로 번역한 결과는 **'+str(result.text)+'['+str(result.pronunciation)+']**야!', colour=0xff7676)
      embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
      await ctx.send(embed=embed)
      
    else:
      embed = discord.Embed(title=lang+' 언어는 번역할 수 없어 ;(', description='번역 기능은 `/번역 [내용]:(내용) [언어명]:(언어명)`으로 사용할 수 있어! 구글 번역기 API를 이용하여 개발이 되었고, 사용할 수 있는 언어는 다음과 같아!\n**한국어**\n**중국어 번체**\n**중국어 간체**\n**일본어**\n**영어**', colour=0xff7676)
      embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
      await ctx.send(embed=embed)


@slash.slash(name = "룰렛", description = "항목을 입력하면 랜덤으로 뽑아줍니다. 기본개형은 /룰렛 [항목]:(항목1)/(항목2)/(항목3)/....../(항목n)입니다.")
async def _룰렛(ctx:SlashContext, 항목:str):
  global rullet
  global rulletcount
  global rulletposition
  rullet = 항목.split('/')
  rulletcount = len(rullet)
  selection = random.randrange(0, rulletcount)
  selectioncontent = rullet[selection]
  rulletposition = selection
  global output
  global cursur
  output = "0"
  cursur = 0
  for x in range(rulletposition):
    output = output + rullet[cursur]+"\n"
    cursur = cursur+1
  output = output +"**"+ rullet[rulletposition] +"** :point_left:\n"
  print(rulletposition)
  if rulletcount > rulletposition:
    for x in range(rulletcount - rulletposition - 1):
      cursur = cursur+1
      output = output + rullet[cursur]+"\n"
  
    embed = discord.Embed(title="또르르륵...탁!",
                          description = output[1:],
                          colour=0xDDECCA)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
  await ctx.send(embed = embed)

@slash.slash(name = "넌센스", description = "파이가 넌센스 퀴즈를 내요")
async def _넌센스(ctx:SlashContext):
  content = nonsense[random.randrange(0, len(nonsense))]
  embed = discord.Embed(title="한 번 맞춰봐!!",
                        description = content,
                        colour=0xDDECCA)
  embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
  await ctx.send(embed = embed)

@slash.slash(name = "영화", description = "네이버에서 영화를 검색해줍니다. 기본개형은 /룰렛 [영화제목]:(영화제목)입니다.")
async def _영화(ctx:SlashContext, 영화제목:str):
  client_id = os.environ['id']
  client_secret = os.environ['secret']

  movie=영화제목
  header_parms = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
  url = f"https://openapi.naver.com/v1/search/movie.json?query={movie}"
  res = requests.get(url, headers=header_parms)
  data = res.json()

  title=data['items'][0]['title'].strip('</b>')
  link=data['items'][0]['link']
  date=data['items'][0]['pubDate']
  director=data['items'][0]['director'].split('|')[0]
  actors=data['items'][0]['actor'].split('|')[:-1]
  rating=float(data['items'][0]['userRating'])
  await ctx.send(title+link+date+director+str(actors)+str(float(rating)))
  directstr = "0**"+str(director)+"**"
  actstr = "0"
  for i in actors:
    if len(actors) > 1:
      actstr = actstr+"**"+i+"**, "
    else:
      actstr = actstr+"**"+i+"**"
  embed = discord.Embed(title=":popcorn: "+title,
                        colour=0xDDECCA)
  embed.add_field(name='**개봉 연도**', value=str(date), inline=False)
  embed.add_field(name='**감독**', value=directstr[1:], inline = False)
  embed.add_field(name='**배우**', value=actstr[1:], inline = False)
  embed.add_field(name='**평점**', value=str(rating), inline = False)
  embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
  embed.set_footer(text="Copyright Ⓒ NAVER Corp. All rights reserved.")
  await ctx.send(embed=embed)
  await buttons.send(
    content = None,
    channel = ctx.channel.id,
    components = [
      ActionRow([
        Button(
          label = "NAVER에서 이 영화 보기",
          style = ButtonType().Link,
          url = link
        )
      ])
    ]
  )
bot.run(os.environ['token'])