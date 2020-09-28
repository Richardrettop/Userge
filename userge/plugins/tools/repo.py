# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/xmtscf >.
#
# This file is part of < https://github.com/xmtscf/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from userge import userge, Message, Config, versions, get_version


@userge.on_cmd("repo", about={'header': "obter link de repo e detalhes"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
**Oi**, __Este é o__ 🔥 **Userge do @xmtscf** 🔥

    __A tecnologia está aos nossos olhos!__

• **Versão do userge** : `{get_version()}`
• **Licença** : {versions.__license__}
• **Copyright** : {versions.__copyright__}
• **Repositório** : [xmtscf/Userge]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
