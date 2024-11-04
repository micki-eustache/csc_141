import separate_file
separate_file.send_messages()

from separate_file import send_messages
send_messages()

from separate_file import send_messages as sm
sm()

import separate_file as sf
sf.send_messages()

from separate_file import *
send_messages()
