from subprocess import Popen, PIPE
#Popen("mpg123 test.mp3", shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()
Popen("mpg123 test.mp3", shell=True)
Popen("notify-send -i evince HEAD test.mp3", shell=True)
