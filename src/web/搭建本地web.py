import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse, FileResponse
import subprocess

app = FastAPI(concurrency_limit=500)

# 自动裁剪
@app.get("/file/{file_name}")
def calcToken(file_name: str):
    file = "C:/Windows/Path1/%s" % (file_name[0:-4])
    header = {'content-disposition':"inline;filename=%s" % file_name, 'Content-Type':get_content_type(file)}
    # return FileResponse(r"E:\temp/%s" % (file_name[0:-4]), headers=header)
    return FileResponse(file, headers=header)

def get_content_type(file):
    cmd_p = subprocess.Popen('ffmpeg -i %s -hide_banner' % file, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd_result = ""
    for i in cmd_p.stdout.readlines():
        cmd_result += i.decode()
    for i in cmd_p.stderr.readlines():
        cmd_result += i.decode()
    if "mpegts" in cmd_result:
        return "video/MP2T"
    elif "mpeg" in cmd_result:
        return "video/mpeg"
    elif "mp4" in cmd_result:
        return 'video/mp4'
    else:
        return 'video/mp4'

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8000, workers=1)