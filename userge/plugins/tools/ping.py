# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/xmtscf >.
#
# This file is part of < https://github.com/xmtscf/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from datetime import datetime
from userge import userge, Message


@userge.on_cmd(
    "ping", about={'header': "verifique quanto tempo leva para executar ping no seu userbot"})
async def pingme(message: Message):
    start = datetime.now()
    await message.edit('`Pong!`')
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**Pong!**\n`{m_s} ms`")
