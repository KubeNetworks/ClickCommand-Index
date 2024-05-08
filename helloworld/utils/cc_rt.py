"""
CLICKCOMMAND_RT
CLICKCOMMAND RunTime configuration. 样例如下

{
    "cmd": "main",
    "args": {
        "name": "john"
    }
}
"""

import json
import os


clickcommand_rt = json.loads(os.environ.get("CLICKCOMMAND_RT", '{"cmd": "main"}'))
