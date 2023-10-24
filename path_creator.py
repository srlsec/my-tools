import os

cwd = os.getcwd()

url = "ws.kseb.in/SafetyApp/jkj/downloadDoc?doc_id=35620&bolist=true"

fullname = os.path.join(cwd, url)
path, basename = os.path.split(fullname)
if not os.path.exists(path):
    os.makedirs(path)

with open(fullname, 'w') as f:
    f.write('test\n')