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
bot = commands.Bot(command_prefix='.')
print("Working...")

buttons = ButtonsClient(bot)
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game('.도움말'))


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
@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)
  
@bot.command()
async def 파이(ctx):
  await ctx.channel.send("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480665499119881834797753566369807426542527862551818417574672890977772793800081647060016145249192173217214772350141441973568548161361157352552133475741849468438523323907394143334547762416862518983569485562099219222184272550254256887671790494601653466804988627232791786085784383827967976681454100953883786360950680064225125205117392984896084128488626945604241.... **삐릭.. 삐리릭.. 펑!**")

@bot.command()
async def 찬반(ctx,*, query):  
  embed = discord.Embed(
    title=(str(ctx.message.content)[4:]),
    description = "과연 결과는?? 두구두구두구..\r\n\r\n👍 - 찬성    🤝 - 중립    👎 - 반대",
    colour=0x7DB249    
  )
  embed.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/zuKJ5T6ZNhAwCkJ-Tx0C5O7QT6gMLCE7IqY3I1hJcHQ/https/media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
  em = await ctx.channel.send(embed=embed)
  await em.add_reaction("👍")
  await em.add_reaction("🤝")
  await em.add_reaction("👎")

@bot.command()
async def QR(ctx,*, query):
  global qrmade
  qrmade = str(ctx.message.content)[4:]
  if qrmade == "?":
    
        embed = discord.Embed(
          title='QR 코드에 대해 알아보고 싶다고?',
          description=
          "내용을 입력하면 QR 코드를 생성할 수 있는 명령어야!\n\n`.QR (내용)`\n `(내용)`에는 글자를 입력해도 되고, 링크를 넣어도 돼!\n\n`ex) .QR 이 QR코드는 메시지를 출력합니다.`\n`.QR m.naver.com`",
          colour=0xff7676)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
        await ctx.channel.send(embed=embed)
  else:
    img = qrcode.make(qrmade)
    img.save(os.path.dirname(os.path.realpath(__file__))+"\qr.png")
    file = discord.File(os.path.dirname(os.path.realpath(__file__))+"\qr.png")

    embed = discord.Embed(
      title=(qrmade+"에 관한 QR코드"),
      description = "완성이야!",
      colour=0x7DB249    
    )
    embed.set_thumbnail(url=f"attachment://{file.filename}")
    await ctx.channel.send(embed=embed, file=file)

@bot.command()
async def 디엠(ctx):
  if ctx.author.dm_channel:
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
    channel = await ctx.author.create_dm()
    embed = discord.Embed(
      title=(str(ctx.author)[:len(str(ctx.author))-5])+'님, 여기에요!',
      description = "새로운 1대1 대화방을 만들었어요! 이곳에서 저와 DM을 주고받으실수 있답니다! **통신 명령어는 사용이 불가능해요.**",
      colour=0x7DB249    
    )
    embed.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/zuKJ5T6ZNhAwCkJ-Tx0C5O7QT6gMLCE7IqY3I1hJcHQ/https/media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
    embed.set_footer(text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    await channel.send(embed = embed)

@bot.command()
async def 패치노트(ctx):
  embed = discord.Embed(
    title='PATCHNOTE',
    description = "**2.0.0**\n버튼 기능 추가\n가위바위보 기능 추가\n날씨 기능 보완\n기존 명령어에 버튼 추가\n프로필에 서버에 추가 버튼 추가\n.자기소개명령어에도 서버에 추가 버튼 추가\n\n**1.9.2**\n날씨 기능 보완\n날씨 기능 오류 수정\n핑 명령어 추가\n\n**1.9.1**\n삭제 명령어 남용 방지 기능 추가\n찬반 기능 중립 추가\n주식 기능 지원 중단\n서비스 경량화&서버렉 감소\n파이 전용 도움말&자기소개 홈페이지 업로드",
    colour=0x7DB249    
  )
  embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
  embed.set_footer(text="패치노트에는 최근 세 개의 버전만 표기됩니다.\nCopyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
  await ctx.channel.send(embed=embed)

@bot.command()
async def 밥추천(ctx):
    embed = discord.Embed(
        title='오늘의 밥으로는 ' + random.choice(food) + " 어때?",
        description=
        "내가 알고 있는 음식의 종류로는 대략 30여가지의 음식이 있어. 혹시 네가 알고 있는 색다른 음식이 있다면 개발자에게 보내줘!",
        colour=0x7DB249)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
    await ctx.channel.send(embed=embed)

@bot.command()
async def 도박(ctx):
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
  await ctx.channel.send(embed=embed)
  
@bot.command()
async def 운세(ctx):
    num = random.randrange(1, 101)
    num = str(num)

    embed = discord.Embed(title='오늘의 운세는!', colour=0x7DB249)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
    embed.add_field(name='> 재미로 보는 오늘의 운세!',
                    value='네가 ' + random.choice(Random) + num +
                    '% 야! **재미로만 보는것이니 기분 안 나빠했으면 좋겠어!!**')
    await ctx.channel.send(embed=embed)

@bot.command()
async def 규칙(ctx):
  embed = discord.Embed(
    title = "이 서버에서 지켜야할 규칙들이야, 한번 자세히 읽어 봐",
    description = "사고팔기 금지 (만일 피해가 발생할 시에는 책임지지 않음)\r\n욕설, 타인에 대해 비방 금지\r\n정치, 사회적 발언 금지\r\n개인 간에 서버에 대한 개인 체팅 금지 (걸릴 시에는 추방)\r\n대화 내용을 캡쳐하여 올리지 않기 (관리자가 승인한 경우, 허용)\r\n봇 해킹 금지(어길시에는 법적 대응, 영구 추방)\r\n\r\n위의 내용을 5회 어길 시 **영구 추방**됩니다.",
    colour = 0x7DB249
  )
  embed.set_thumbnail(url=  "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.png"
    )
  embed.set_footer(text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
  await ctx.channel.send(embed=embed)

@bot.command()
async def 홈페이지(ctx):
  embed = discord.Embed(
    title = "Esusin Laboratory 공식 홈페이지야",
    description = "이곳에는 제작자분의 여러가지 소프트웨어가 있어. 모두 무료야! 아래 버튼을 누르면 홈페이지로 이동이 돼!",
    colour = 0x7DB249
  )
  embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303553425498/110_20220410122834.png")
  await buttons.send(
    content = None,
    embed = embed,
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

@bot.command()
async def 가위바위보(ctx):
    embed = discord.Embed(
        title= '안 내면 진다',
        description="가위바위....\r\n:v: :raised_hand: :fist:",
        colour=0x7DB249)
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.png"
    )
    await buttons.send(
      content = None,
      embed = embed,
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
  

@bot.command()
async def 자기소개(ctx):
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
    await buttons.send(
      content = None,
      embed = embed,
      channel = ctx.channel.id,
      components = [
        ActionRow([
          Button(
            label = "파이 자기소개 보기",
            style = ButtonType().Link,
            url = "http://esusinlabpie.bu.to/"
          ),
          Button(
            label = "파이 명령어 모음집",
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

@bot.command()
async def 관리자(ctx):
    embed = discord.Embed(title='나에 대한 모든 권한을 가지고 있는 분들이야!',
                          description="이분들은 이분들만의 특별한 명령어를 사용할 수 있어!",
                          colour=0x7DB249)
    embed.add_field(name='> 관리자 목록', value=Administrator)
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.png"
    )
    await ctx.channel.send(embed=embed)


@bot.command()
async def 검색(ctx, *, query):
    msg = (ctx.message.content)
    msg = (msg[4:])
    thumbnail = msg  
    msg = msg.replace(' ', '%20')
    embed = discord.Embed(title='자, 여기 너가 원하는 결과가 기다리고 있어!', colour=0xff7676)
    await buttons.send(
      content = None,
      embed = embed,
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


@bot.command()
async def 스크립트(ctx):
    embed = discord.Embed(
        title=':page_with_curl: 스크립트 명령어에 대해서...',
        description=
        "'스크립트 명령어는 `.(스크립트 지원 명령어) (인자)`의 형태로 사용 가능...' 이라고 나와 있군..!!",
        colour=0x7DB249)
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.ight=625"
    )
    await ctx.channel.send(embed=embed)


@bot.command()
async def 놀이(ctx):
    embed = discord.Embed(title='같이 놀자!', colour=0x7DB249)
    embed.add_field(name='> 놀이 명령어', value='.운세\r\n.밥추천\r\n.도박\r\n.가위바위보')
    embed.add_field(name='> 스크립트 놀이 명령어', value='.더하기')
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.ight=625"
    )
    await ctx.channel.send(embed=embed)


@bot.command()
async def 더하기(ctx, *, query):
    msg = (ctx.message.content)
    msg = (msg[5:])
    if "+" in msg:
        local = msg.find('+')
        value1 = (msg[0:local])
        local = int(local)
        local = local + 1
        value2 = (msg[local:])
        embed = discord.Embed(
            title=value1 + "와(과)" + value2 + "을(를) 합성해보자..!!",
            description="||" + random.choice(random2) + "||(이)가 나왔네 ㅋㅋ",
            colour=0x7DB249)
        embed.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.ight=625"
        )
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='더하기 기호는 +가 있어야만 이용할수 있어!',
                              description="예를 들어보면, **.더하기 A+B** 이렇게 말이야!",
                              colour=0x7DB249)
        embed.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/933687912950808608/962326782793617458/download20220406195534.ight=625"
        )
        await ctx.channel.send(embed=embed)


@bot.command()
async def 유튜브(ctx, *, query):
    msg = (ctx.message.content)
    msg = (msg[5:])
    thumbnail = msg
    msg = msg.replace(' ', '%20')
    embed = discord.Embed(title='자, 여기 너가 원하는 YouTube 동영상이 기다리고 있어!',
                          description = "아래의 버튼을 눌러서 YouTube로 이동할 수 있어!",
                          colour=0xff7676)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/929576166740873231/972691405665353769/110_20220508114729.png"
    )
    await buttons.send(
      content = None,
      embed = embed,
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


@bot.command()
async def 날씨(ctx, *, query):
    global msg
    msg = (ctx.message.content)
    msg = (msg[4:])
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
            "서울, 백령도, 제주도, 춘천, 인천, 강릉, 울릉도, 독도, 전주, 대전, 수원, 안동, 울산, 광주, 청주, 목포, 여수, 부산, 울산, 제주도\n\n`.날씨 (지역이름)`",
            colour=0xB8E9FF)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
        await ctx.channel.send(embed=embed)
    else:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title=msg+" 지역을 찾을 수 없어 ;(",
            description=
            "서울, 백령도, 제주도, 춘천, 인천, 강릉, 울릉도, 독도, 전주, 대전, 수원, 안동, 울산, 광주, 청주, 목포, 여수, 부산, 울산, 제주도\n\n`.날씨 (지역이름)`\n\n`ERROR : valueable varients 'msg' is not int value, line 949, in main.py`",
            colour=0xB8E9FF)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/933687912950808608/962557303113011210/download20220406195534.png")
        await ctx.channel.send(embed=embed)

      
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
      
        await buttons.send(
          content = None,
          embed = embed,
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


@bot.command()
async def 빌보드(ctx):
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
    await buttons.send(
      content = None,
      embed = embed,
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
@bot.command()
async def 뉴스(ctx):
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
    await buttons.send(
      content = None,
      embed = embed,
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


@bot.command()
async def 코로나(ctx):
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
    await buttons.send(
      content = None,
      embed = embed,
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


@bot.command()
async def 롤(ctx, *, query):
    msg = (ctx.message.content)
    msg = (msg[3:])
    msg = msg.replace(' ', '%20')
    embed = discord.Embed(title='휴.. opgg에서 네가 바란 것을 찾았어',
                          description = "참고로 난 소규모 서버라 이런것 하나 검색하는 데 렉이 많이 걸려",
                          colour=0xff7676)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561287413840/110_20220410122834.png")
    await buttons.send(
      content = None,
      embed = embed,
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


@bot.command()
async def 정보(ctx):
    file = discord.File(os.path.dirname(os.path.realpath(__file__))+"\;thanks.png")
    embed = discord.Embed(
        title='정보',
        colour=0x7DB249)
    embed.add_field(name='> 소프트웨어 버전', value='`2.2.3` **Waiotapu**')
    embed.add_field(name='> 언어 버전', value='`Python® Discord.py Module Version 1.7.3`')
    embed.add_field(name='> 라이센스', value='`Official`')
    embed.add_field(name='> 빌드', value='`Build 22096.87.21`')
    embed.set_thumbnail(url=f"attachment://{file.filename}")
    embed.set_footer(
        text=
        "Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.\n소프트웨어가 최신 버전입니다."
    )
    await ctx.channel.send(embed=embed, file = file)

@bot.command()
async def 핑(ctx):
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
@bot.command()
async def 삭제(ctx,*, query):
    if ctx.author.name in Administrator:
      msg = (ctx.message.content)
      msg = (msg[4:])
      msg = int(msg)
      if msg > 19:
        embed = discord.Embed(
            title='미안해 ;(',
            description=
            "미안하지만, '.삭제' 명령어는 남용을 방지하기 위해 한번에 20개 이상 삭제할 수 없어..\n`ERROR : valueable varients 'msg' is not int value, line 1195, in main.py`",
            colour=0xff7676)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
        await ctx.channel.send(embed=embed)
      elif msg < 20:
        
        await ctx.channel.purge(limit=msg+1)

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
@bot.command()
async def 얼차려(ctx):
    if ctx.author.name in Administrator:
        await ctx.channel.send("@everyone 다들 얼차렷!")

    else:
        embed = discord.Embed(
            title='미안해 ;(',
            description=
            "> 미안하지만, '.얼차려'는 관리자 전용 명령어야. 그래서 너의 권한으로는 '.삭제'명령어를 사용할 수 없어..",
            colour=0xff7676)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
        embed.add_field(name='> 관리자 목록', value='.관리자')
        await ctx.channel.send(embed=embed)


@bot.command()
async def 도움말(ctx):
  global msg
  msg = (ctx.message.content[5:])
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
    embed.add_field(name=".도움말", value="도움말 명령어는 이 메시지를 띄웁니다. 도움말 명령어에 대해 자세히 알아보려면 `.도움말 ?`을 입력하거나, `.도움말 (페이지 번호)`를 입력하십시오.", inline = False)
    embed.add_field(name=".자기소개", value="자기소개 명령어는 봇에 대한 간단한 정보를 보여줍니다. 세부 내용을 보려면 `.정보`명령어를 입력하십시오.", inline = False)
    embed.add_field(name=".관리자", value="관리자 명령어는 관리자 권한이 부여된 사용자의 리스트를 출력합니다.", inline = False)
    embed.add_field(name=".정보", value="정보 명령어는 봇의 세부적인 정보를 띄웁니다. 보다 간단한 정보는 `.자기소개`명령어 문서를 참고하십시오.", inline = False)
    embed.add_field(name=".스크립트", value="스크립트 명령어는 조합 가능한 명령어를 사용하는 방법을 출력합니다.", inline = False)
    embed.add_field(name=".더하기", value="더하기 명령어는 리스트에서 랜덤으로 결과값을 반환합니다. `.더하기 (내용)+(내용)`이 기본개형입니다. 자세한 내용을 보려면 `.더하기 ?`명령어를 사용하십시오.", inline = False)
    embed.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    
    embed_page_2 = discord.Embed(
        title='2페이지',
        description="파이 디스코드 봇을 사용해주셔서 감사합니다.\n 귀하는 현재 **5쪽 중 2쪽**에 위치해 있습니다.",
        colour=0x7DB249)
    embed_page_2.add_field(name=".롤", value="롤 명령어를 사용하면 op.gg에서 해당 소환사에 대한 정보를 출력해줍니다. 기본개형은 `.롤 (소환사명)`입니다.", inline = False)
    embed_page_2.add_field(name=".검색", value="검색 명령어는 Microsoft Bing에서 검색 결과를 보여줍니다. 기본개형은 `.검색 (내용)`입니다.", inline = False)
    embed_page_2.add_field(name=".유튜브", value="유튜브 명령어는 유튜브에서 동영상을 검색해줍니다. 기본개형은 `.유튜브 (내용)`입니다.", inline = False)
    embed_page_2.add_field(name=".날씨", value="날씨 명령어는 해당 지역의 날씨를 실시간으로 알려줍니다. 기본개형은 `.날씨 (지역명)`입니다. 자세한 내용을 보려면 `.날씨 ?` 명령어를 사용하십시오.", inline = False)
    embed_page_2.add_field(name=".운세", value="운세 명령어는 오늘의 운세를 랜덤으로 출력합니다.", inline = False)
    embed_page_2.add_field(name=".밥추천", value="밥추천 명령어는 밥을 랜덤으로 추천해줍니다.", inline = False)
    embed_page_2.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    embed_page_3 = discord.Embed(
        title='3페이지',
        description="파이 디스코드 봇을 사용해주셔서 감사합니다.\n 귀하는 현재 **5쪽 중 3쪽**에 위치해 있습니다.",
        colour=0x7DB249)
    embed_page_3.add_field(name=".빌보드", value="빌보드 명령어는 실시간으로 갱신되는 빌보드 차트 1위 음악을 알려주며, 그 음악을 유튜브에서 찾아 줍니다.", inline = False)
    embed_page_3.add_field(name=".코로나", value="코로나 명령어는 매일 갱신되는 코로나 확진자 수와 일일 사망자 수 등을 출력합니다.", inline = False)
    embed_page_3.add_field(name=".뉴스", value="뉴스 명령어는 현재 업로드된 가장 최근 기사를 출력합니다. 명령어를 사용하면 나오는 버튼을 눌러 뉴스 페이지로 이동할 수 있습니다.", inline = False)
    embed_page_3.add_field(name=".패치노트", value="패치노트 명령어는 최근 업데이트 내역을 출력합니다.", inline = False)
    embed_page_3.add_field(name=".홈페이지", value="홈페이지 명령어는 파이 디스코드 봇 제조사 홈페이지를 띄웁니다.", inline = False)
    embed_page_3.add_field(name=".찬반", value="찬만 명령어는 찬성과 반대, 중립으로 나뉘는 투표를 게시합니다. 기본개형은 `.찬반 (내용)`입니다.", inline = False)
    embed_page_3.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    embed_page_4 = discord.Embed(
        title='4페이지',
        description="파이 디스코드 봇을 사용해주셔서 감사합니다.\n 귀하는 현재 **5쪽 중 4쪽**에 위치해 있습니다.",
        colour=0x7DB249)
    embed_page_4.add_field(name=".핑", value="핑 명령어는 현재 봇의 핑을 출력합니다. 서버의 상태에 따라 메시지 색깔이 달라집니다.", inline = False)
    embed_page_4.add_field(name=".디엠", value="디엠 명령어는 파이 디스코드 봇과의 1:1 대화방을 생성합니다.", inline = False)
    embed_page_4.add_field(name=".QR", value="QR명령어는 QR코드를 생성합니다. 기본개형은 `.QR (내용)`입니다. 자세한 내용을 보려면 `.QR ?`명령어를 사용하십시오.", inline = False)
    embed_page_4.add_field(name=".가위바위보", value="가위바위보 명령어는 버튼을 눌러 봇과 가위바위보 대결을 하는 게임입니다.", inline = False)
    embed_page_4.add_field(name=".놀이", value="놀이 명령어는 플레이 가능한 게임 리스트를 출력합니다.", inline = False)
    embed_page_4.add_field(name=".도박", value="도박 명령어는 랜덤으로 나오는 과일의 가운데 세 줄이 왕관이면 당첨이 되는 게임입니다.", inline = False)
    embed_page_4.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    embed_page_5 = discord.Embed(
        title='5페이지',
        description="파이 디스코드 봇을 사용해주셔서 감사합니다.\n 귀하는 현재 **5쪽 중 5쪽**에 위치해 있습니다.",
        colour=0x7DB249)
    embed_page_5.add_field(name=".번역", value="번역 명령어는 여러 가지의 언어로 번역을 해 주는 명령어입니다. 기본개형은 `.번역 (내용)/(언어명)`입니다. 번역 명령어에 관한 문서를 보려면 `.번역 ?`를 입력하십시오.", inline = False)
    embed_page_5.add_field(name=".삭제", value="삭제 명령어는 숫자의 갯수만큼 메시지를 삭제합니다. 기본개형은 `.삭제 (숫자)`이며, 관리자만 사용할 수 있습니다. 삭제 명령어는 남용 방지를 위해 한번에 19개 까지만 삭제 가능합니다.", inline = False)
    embed_page_5.add_field(name=".얼차려", value="얼차려 명령어는 서버에 있는 모두를 맨션합니다. 이 명령어는 관리자만 사용할 수 있습니다.", inline = False)
    embed_page_5.set_footer(
        text="Copyright Ⓒ 2017-2022 Esusinlab All rights reserved.")
    
    msge = await ctx.channel.send(embed = embed)
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

@bot.command()
async def 번역(ctx,*,query):
  msg = (ctx.message.content[4:])
  r1 = msg.count('/')
  if r1 == 1:
    global langtrans
    translator = Translator()
    r2 = msg.split('/')
    content = msg[:msg.find('/')]
    lang = r2[1]
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
      await ctx.channel.send(embed=embed)
      
    else:
      embed = discord.Embed(title=lang+'언어는 번역할 수 없어 ;(', description='번역 기능은 `.번역 (내용)/(언어명)`으로 사용할 수 있어! 구글 번역기 API를 이용하여 개발이 되었고, 사용할 수 있는 언어는 다음과 같아!\n**한국어**\n**중국어 번체**\n**중국어 간체**\n**일본어**\n**영어**', colour=0xff7676)
      embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
      await ctx.channel.send(embed=embed)
    
    

  elif msg == "?":
    embed = discord.Embed(title='번역 기능에 대해 자세히 알아봐!', description='번역 기능은 `.번역 (내용)/(언어명)`으로 사용할 수 있어! 구글 번역기 API를 이용하여 개발이 되었고, 사용할 수 있는 언어는 다음과 같아!\n**한국어**\n**중국어 번체**\n**중국어 간체**\n**일본어**\n**영어**', colour=0xff7676)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
    await ctx.channel.send(embed=embed)
  else:
    embed = discord.Embed(title='이런!', description='어이쿠! 번역 기능은 `.번역 (내용)/(언어명)`으로 사용할 수 있어! 자세한 내용은 `.번역 ?`을 입력해 봐!\n\n`ERROR : parameter "r1" is already defined, line 1385, in main.py`', colour=0xff7676)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/918381996483424306/962556561081897000/110_20220410122100.png")
    await ctx.channel.send(embed=embed)
    
#입장추방
def find_first_channel(channels):
    position_array = [i.position for i in channels]

    for i in channels:
        if i.position == min(position_array):
            return i
@bot.command()
async def on_member_join(self, member):
  msg = "<@{}>님이 서버에 들어오셨어요. 다 같이 <@{}>님을 환영하는 건 어떤가요?".format(str(member.id))
  await find_first_channel(member.guild.text_channels).send(msg)
  return None
@bot.command()
async def on_member_remove(self, member):
  msg = "<@{}>님이 서버에서 나가거나 추방되었습니다.".format(str(member.id))
  await find_first_channel(member.guild.text_channels).send(msg)
  return None
bot.run(os.environ['token'])