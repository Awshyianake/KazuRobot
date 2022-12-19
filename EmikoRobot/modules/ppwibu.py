import os

import random

from telethon.tl.types import InputMessagesFilterPhotos

from EmikoRobot.events import register

from EmikoRobot import telethn as tbot, ubot2               

@register(pattern="^/ppwibu ?(.*)")

async def _(event):

    memeks = await event.reply("Sabar Sayang, Lagi Kazu Cari...🔍") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@ppanimeee", filter=InputMessagesFilterPhotos

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Nih Wibu PP Lu Udah Dapet😝", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit(" Jomblo mah jomblo ajh mek 😏")
