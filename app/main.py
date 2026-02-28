from fastapi import FastAPI

from models import ChatCompletionRequest



app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


@app.post("/v1/chat/completions")
async def completions(request: ChatCompletionRequest):
    return request


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
