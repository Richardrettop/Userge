#!/bin/bash
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/xmtscfTeam >.
#
# This file is part of < https://github.com/xmtscfTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

urlEncode() {
    echo "<code>$(echo "${1#\~}" | sed -E 's/(\\t)|(\\n)/ /g' |
        curl -Gso /dev/null -w %{url_effective} --data-urlencode @- "" | cut -c 3-)</code>"
}
