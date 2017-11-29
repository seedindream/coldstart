import os
import json
import time
tm_st = time.time()


postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
response.write("response time "+str(tm_st))
response.close()