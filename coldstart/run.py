import os
import json
import time
import subprocess

tm_st = time.time()

cmdCommand = 'powershell D:\\home\\site\\wwwroot\\coldstart\\record.exe' #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), shell=True,stdout=subprocess.PIPE)
output5, error = process.communicate()
tm_finish = time.time()

# postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
response.write("response time "+str(tm_st)+"finish "+str(tm_finish)+"@\n"+output5)
response.close()