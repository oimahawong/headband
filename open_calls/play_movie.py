from flask import request, g

from tools.logging import logger   
from neurosdk.cmn_types import *

import sys
import io

def handle_request():
    if g.hb == None:
        return ["Data not Flowing"]

    g.hb.exec_command(SensorCommand.CommandStartSignal)

    return ["Data Flowing"]

