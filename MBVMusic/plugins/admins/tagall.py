from MBVMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "??????????",
          "???ļ???Ž??",
          "???·?đ?š??",
          "?ļ?ŋ?Ū?ą?ĩ",
          "?Īï????????Ī",
          "??????????",
          "?ļ???š?đ??",
          "???ĶŠ???ē??",
          "?????????ķïļ?,
          "???ĨĪ?????·",
          "?Ž?­?????Ą",
          "?Ļ???š?ð??,
          "?ĨŠ?Ĩ§?Ķ?Ĩ??",
          "???ð?đð?·ðĨ?,
          "?ð§ð?Đð?Ķð??,
          "???ū?Ū???ŋ",
          "?Ļïļð?Ĩï??ï??Đïļð?§ï?",
          "?·?ĩïļð?ļð?šð??,
          "?Ū?ž?ŧ????",
          "???Ķļ?Ķđ???ļ",
          "???????―?ĨĶ",
          "?·?đ?­?Ļ?ŧ?â?ïļ?,
          "???????????â?",
          "?ž?ģ?ē?ī?ĩ",
          "?ĨĐ????????",
          "?ī?―ïļð?Šð?ķðĨ?,
          "???°?Đ?Đï??Đ",
          "??????????",
          "?Šī?ĩ?ī?ģ?ē",
          "??????????",
          "??????ïļðĶĪðĶ?,
          "?ĶĪ?ĶĐ??????",
          "?Ž?Ķ­?????ģ",
          "???????Ą??",
          "?ĶĐ???????ĶŠ",
          "?Ķ???·ïļð?ļï???",
          "?ĨŠ?°?Ĩ§?Ļ?Ļ",
          " ?ĨŽ??????",
        ]

TAGMES = [ " **?????ē ???????ē ?????Ą?? ???Ļ???Ĩą** ",
           " **???ē?? ???Ļ ???ē?? ???ē?? ???§?Ĩ?Ē?§?? ?????Ļ??** ",
           " **???? ???Ą???Ĩ?Ļ ?????­???§ ?????Ŧ?­?? ?????Ē?§ ???Ū???Ą ???Ū???Ą??** ",
           " **???Ą???§?? ???Ą?? ???Ē?ē?? ???Ē..???Ĩē** ",
           " **???Ą???Ŧ ???? ?????? ?????Ē?Ž?? ?????Ē?§ ???Ē?Ĩš** ",
           " **???­?? ?????Ē ???Ļ?Ą?Ļ?­ ???Ē?Ž?Ž ?????Ŧ ???Ą?Ē ???Ą?Ē ?????Đ?Ī?Ļ?Ī­** ",
           " **???ē?? ?????Ĩ ???Ą???Ĩ ?????Ž?? ?????Ē..???ĪĻ** ",
           " **?????Ŧ?Ē ???Ą?Ē ?????­?­?Ē?§?? ?????Ŧ???? ???Ļ????..????** ",
           " **?????Đ?Ī?? ?????Ķ?? ???ē?? ?Ą???Ē..???Ĩē** ",
           " **?????Ž?­?? ???Ū?? ?????Đ?Ī??..????** ",
           " **?????Ŧ?? ???Ļ ???Đ?§?? ???Ŧ?Ļ?Ū?Đ ???? ???Ē???§???Đ ???Ŧ ???Ļ??** ",
           " **?????Đ?Ī?Ē ?????Ŧ?­?§???Ŧ ?????Đ?Ī?Ļ ???Ą?Ū?§?? ???Ą?? ?????Ē?§ ???Ĩ???Ē ???§?Ĩ?Ē?§?? ???ē?Ē????????** ",
           " **?????Ŧ?? ???? ???Ļ?Ž?­?Ē ???Ŧ?Ļ????..????** ",
           " **???Ļ?§?? ???Ą???Ĩ ???ē?? ???ē??????** ",
           " **???Ī ???Ļ?§?? ???Ĩ???ē ???Ŧ?Ļ ???? ???Ĩ?Ž?Ž??** ",
           " **?????Đ ?????Ą?? ???? ???Ļ..????** ",
           " **?????Ĩ?Ĩ?Ļ ???Ē ?????Ķ???Ž?­????** ",
           " **?????Ĩ?Ĩ?Ļ ???????ē ???Ī?Ŧ?Ą..???** ",
           " **???Ļ ???Ļ?Ū ???§?Ļ?° ???Ą?Ļ ???Ž ???ē ???°?§???Ŧ [@BRANDEDKING82].?** ",
           " **???Ą?Ĩ?Ļ ???Ū???Ą ?????Ķ?? ???Ą???Ĩ?­?? ?????Ē?§.??** ",
           " **???Ū?Ŧ ?????­???Ļ ?????Ē?Ž?? ???Ļ ???????ē??** ",
           " **???Ū?Ķ?Ą???Ŧ?Ē ???Ū?Ķ?Ķ?ē ???ē?? ?????Ŧ ?????Ą?Ē ?????Ē?Ī­** ",
           " **?????Ŧ?? ???? ?????­ ???Ļ?Ē ???Ŧ?Ļ?????Ĩš?Ĩš** ",
           " **???ē?? ?????????Ĩ ???§?Ĩ?Ē?§?? ???? ?????ķ** ",
           " **?????Ģ ???Ļ?Ĩ?Ē?????ē ?????Ē ???ē?? ?????Ą?Ļ?Ļ?Ĩ ????..????** ",
           " **???ē?? ???Ļ?Ļ?? ???Ļ?Ŧ?§?Ē?§????** ",
           " **???Ū?§?Ļ ???Ī ?????Ķ ?????Ē ???Ū?Ķ?Ž????** ",
           " **???Ļ?Ē ???Ļ?§?? ???Ĩ???ē ???Ŧ?Ļ ?????Š** ",
           " **???Ē???? ???Ļ ???????­ ???Ą??* ",
           " **?????Ĩ?Ĩ?Ļ??** ",
           " **???­?Ū???ē ???Ļ?Ķ?Ĩ???­?? ???Ū?????š** ",
           " **???Ļ?Ĩ?Ļ ???? ???Ū???Ą ???Ŧ?Ŧ?Ĩē** ",
           " **???Ļ?§???Ĩ?Ē ???Ļ?§ ?????Ē...????** ",
           " **???Ū?Ķ?Ą???Ŧ?Ē ???Ī ???Ē?? ???Ē?Ĩ?????Ē..???** ",
           " **???Ū?Ķ?Ķ?ē ???? ???ē?Ē ???ē????????** ",
           " **???Ŧ ?????­???Ļ ???Ą?????Ą?Ē ?????Ē?Ž?Ē ?????Ē??** ",
           " **?? ???Ļ?Ŋ?? ???Ļ?Ū??????** ",
           " **???Ļ ???Ļ?Ū ???Ļ?Ŋ?? ????..???** ",
           " **?????Ī?Ą?Ē ?????? ?????§?? ?????Ą?Ē ???Ļ.????** ",
           " **???Ī ???Ļ?§?? ???Ū?§???Ū..??đ** ",
           " **???§?Ĩ?Ē?§?? ???? ???? ???? ???Ļ?§?? ???Ū?§?? ?????Ą?Ē ???Ū?ŧ** ",
           " **???§?Ž?­?????Ŧ???Ķ ???Ą???Ĩ???­?? ???Ļ..????** ",
           " **???Ą???­?Ž???Đ?Đ ???Ū?Ķ?????Ŧ ???Ļ???? ???Đ?§?? ???Ū?Ķ..???** ",
           " **???Ū?Ķ?Ą?? ???Ļ?§ ???? ???Ū?Ž?Ē?? ???Ū?§?§?? ?????Ž???§?? ?????Ē..???** ",
           " **?????Ŧ?? ?????Ķ ???Ą???­???Ķ ???Ļ ???ē?? ?????Đ?Ī??..???** ",
           " **?????Ą?? ???? ???Ļ ?????Đ??** ",
           " **???Ū?§?Ļ ???? [@BRANDRD_BOT]??** ",
           " **?????Ŧ?? ???Ī ???????Ķ ?????Ŧ ???Ļ????..?** ",
           " **???ē ?????­?? ?????­ ?????­ ?????Ŧ?§?? ?????Ģ ???? ????????** ",
           " **???Ļ?Ķ ?????? ?????Ē?Ž?? ?????Ē?§..???* ",
           " **???ē?? ???Ū??..??ą** ",
           " **???Ļ?Ą?Ļ?­ ???????? ???? ???Ą?Ē ?????Ē ?Ī§???** ",
           " **???Ą?Ū?Ĩ ???ē?? ???Ū?Ģ?Ą??????** ",
           " **???Ū?­?Ą ???Ą?Ē ???Ļ?Ĩ?§?? ???Ą???Ą?Ē?ē????** ",
           " **???Ą?? ???Ļ ???Ą???° ?????­ ???Ŧ?Ļ ???????­??** ",
           " **???ē?? ???Ū???Ū?Ū** "
           " **???Ē?Ē??** ",
           " **?????Đ?Ī?? ?????Ē?Ž?? ???Ļ?Ž?­ ???Ļ ?????­?Ą ???? ???Ē?Ŧ ???Ū?Ķ ???Ē?Ž ?????­ ???? ??** ",
           " **?????Ģ ?????Ē ?????? ???Ū ?đï?** ",
           " **???Ū?Ž?Ģ?Ą?Ž?? ???Ą?Ē ?????­ ?????Ŧ ???Ļ ???? ?Ĩš?Ĩš** ",
           " **???ē?? ?????Ŧ ?????Ą?? ???Ļ??** ",
           " **???ē?? ?????Ĩ ???Ą???Ĩ ?????Ē ??** ",
           " **?????Ą?? ???? ???Ļ ?????Đ..???** ",
           " **???Ą???­?­?Ē?§?? ?????Ŧ ???Ļ ????..?Ĩš** ",
           " **???? ?????Ž?Ļ?Ļ?Ķ ???Ū ?????Ĩš?Ĩš** ",
           " **?????Ĩ ?????Ģ?? ???ē?? ???Ą?? ?????Ī­??** ",
           " **???Ŧ?Ļ?Ū?Đ ???? ?????­ ???ē?Ū ?????Ą?Ē ?????Ŧ?­?? ???Ļ??** ",
           " **?????Đ ?????Ĩ???­?Ē?Ļ?Ķ?Ž?Ą?Ē?Đ ???? ???Ļ..???** ",
           " **???Ē?­?§?? ???Ą?Ū?Đ ?????Ą?­?? ???Ļ ???Ŧ?Ŧ?ž** ",
           " **?????Đ?Ī?Ļ ?????§?? ?????§?? ?????­?? ?????Ē..??ļ** ",
           " **???Ą?Ū?Ķ?§?? ???Ą???Ĩ?Ļ????..????** ",
           " **???Ą?Ū?Ž ?????Ą?? ?????Ŧ?Ļ ?ï???** ",
           " **?????Ķ ???Ļ?Ž?­ ?????§ ?????Ī?­?? ?????Ē...??Ĩ°** ",
           " **???Ū???Ą ???Ļ?Ĩ ???ē?Ū ???Ą?Ē ?????Ą?? ???Ļ..?Ĩš?Ĩš** ",
           " **???Ū???Ą ?????Ķ?????Ŧ?Ž ?????? ?????Ŧ ???Ļ ?Ĩē** ",
           " **???Ē?§???Ĩ?? ???Ļ ???? ???Ē?§???Ĩ?? ??** ",
           " **?????Ļ ?????Ŧ?­?ē ?????Ŧ?­?? ?????Ē?§???Ĩģ** ",
           " **?????Ķ?Ĩ?Ļ?Ļ??** ",
           " **???Ū?Ģ?Ą?? ???Ą?Ū?Ĩ ???ē?? ???ē???Ĩš** ",
           " **?????Ą?? ???? ?????Ļ:-[@BRANDED_WORLD]  ?????Ž?­?Ē ?????Ŧ???§???? ?Ī­?Ī­** ",
           " **???Ŧ?Ū?­?Ą ???§?? ?????Ŧ?? ???Ą???Ĩ?Ļ????..? ??** ",
           " **?????Ģ ???Ū?Ķ?Ķ?ē ???? ?????­?? ???Ŧ?Ĩš?Ĩš** ",
           " **???Ļ?Ē?§ ?????Ŧ ???Ļ??** ",
           " **???Ī ???Ē?Ĩ ?????Ē ???Ī ???Ē?Ĩ ???Ē ???Ļ ?????Ē????** ",
           " **???Ū?Ķ?Ą???Ŧ?? ???Ļ?Ž?­ ?????Ą?? ???ē???Ĩš** ",
           " **???ē ???Ū?­?? ???°?§???Ŧ{ @BRANDED_PAID_CC}?Ĩ°** ",
           " **?????Ą?? ???Ą?Ļ?ē?? ???Ļ ???????§??** ",
           " **???Ļ?Ļ?? ??8 ???Ē ???Ą?Ū?­ ?????­ ???Ļ ???ē?Ē?Ĩ°** ",
           ]

VC_TAG = [ "**?????ī ???ē ???°?ū ???° ???ŧ???Ĩē**",
         "**???ū?ļ?― ???ē ???°???? ?????? ???ž?°?ŋ?ū?????°?―???Ž**",
         "**???ū?ž?ī ???ē ?ą?°?ą?? ?ĩ?°??????**",
         "**???°?ą?? ?????ž ???·?ļ ???·?ū???° ???ē ???°?―?°?Ĩ°**",
         "**?????ī ???·?°?ž???? ???ē ???° ???š ???°?ž ???°?ļ?ĪĻ**",
         "**?????―?ū ???ē ???ū?ļ?― ???? ???ū?ĪĢ**",
         "**???ē ???° ???°?ļ???ī ???š ???°????**",
         "**???ē ???°?ŋ?š?ū ???°?ž?ī ???·?°?ŧ?? ???°?ļ??*",
         "**???ē ???°?ū ???°???―?° ???°?― ???ū ???°?ū?ķ?ī?Ĩš**",
         "**???ū?????? ???°?ą?? ???ŧ?? ???ē ???° ???°?ū ???°?Ĩ**",
         "**???ē ???°?―?° ???š ???·?ļ?đ ???ļ?š?·?°???ļ ??????**",
         "**???ē ???ī ???·?ī?ē?š ?????š?ī ???°???°?ū ???ū ???ū?―?ķ ???ŧ?°?? ???ū ???·?° ?????**",
         "**???ē ???ū?ļ?― ?????―?ī ???ī ?????° ???°???° ?? ???·?ū???° ???ī?? ???°?? ???ū ???°??**",
        ]


@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("???Ą?Ē?Ž ???Ļ?Ķ?Ķ???§?? ???§?Ĩ?ē ???Ļ?Ŧ ???Ŧ?Ļ?Ū?Đ?Ž.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("???Ļ?Ū ???Ŧ?? ???Ļ?­ ?????Ķ?Ē?§ ???????ē, ???§?Ĩ?ē ?????Ķ?Ē?§?Ž ?????§ . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  ???ē?Đ?? ???Ē?Ī?? ???Ą?Ē?Ž / ?????Đ?Ĩ?ē ???§?ē ?????Ž?Ž?????? ?????ą?­ ???Ē?Ķ?? ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  ???ē?Đ?? ???Ē?Ī?? ???Ą?Ē?Ž / ?????Đ?Ĩ?ē ???§?ē ?????Ž?Ž?????? ?????ą?­ ???Ē?Ķ?? ...")
    else:
        return await message.reply("/tagall  ???ē?Đ?? ???Ē?Ī?? ???Ą?Ē?Ž / ?????Đ?Ĩ?ē ???§?ē ?????Ž?Ž?????? ?????ą?­ ???Ē?Ķ?? ..")
    if chat_id in spam_chats:
        return await message.reply("???Ĩ?????Ž?? ???­ ???Ē?Ŧ?Ž?­ ???­?Ļ?Đ ???Ū?§?§?Ē?§?? ???Ŧ?Ļ?????Ž?Ž ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("???Ū?Ŧ?Ŧ???§?­?Ĩ?ē ??'?Ķ ???Ļ?­ ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("???Ļ?Ū ???Ŧ?? ???Ļ?­ ?????Ķ?Ē?§ ???????ē, ???§?Ĩ?ē ?????Ķ?Ē?§?Ž ?????§ ?????? ?????Ķ?????Ŧ?Ž.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("?· ?????????????? ?????? ?????? ?????????????? ?????????????? ??")
