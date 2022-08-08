from fastapi import FastAPI

from PersonProfile import PersonProfile
app = FastAPI()

from fastapi.responses import FileResponse

@app.get("/")
def Name():
    return "hello"

@app.get("/data")
def Name():
    return ['docs', 'compile', 'dodo']

@app.get("/main")
def Name():
    return FileResponse('index.html')

@app.get("/game")
def Game():
    return FileResponse('wordle.html')

@app.post("/send")
def Name(data : PersonProfile):
    print(data)
    return 'send complete'