#!C:\Users\handa\PycharmProjects\BlueJIntelliJ\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'BlueJIntelliJ','console_scripts','BlueJIntelliJ'
__requires__ = 'BlueJIntelliJ'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('BlueJIntelliJ', 'console_scripts', 'BlueJIntelliJ')()
    )
