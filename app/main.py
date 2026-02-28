from os import lstat

from fastapi import FastAPI, Header
import uuid
from random import randint

from models import ChatCompletionRequest



app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


@app.post("/v1/chat/completions")
async def completions(request: ChatCompletionRequest,
                      x_request_id: str = Header(None)):
    if not x_request_id:
        x_request_id = str(uuid.uuid4())

    # echo last message in the chat
    for msg in reversed(request.messages):
        role = msg.role
        last_msg = msg.content

    # mocking calculation for token usage for now
    prompt_tokens = len(last_msg)
    completion_tokens = len(last_msg) # we're just echoing the last message back for now
    total_tokens = prompt_tokens + completion_tokens

    return {
        "request-id": x_request_id,
        "choices": [{"messages": {"role": role, "content": last_msg}, "finish_reason": "stop"}],
        "usage": {"prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens, "total_tokens": total_tokens}
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
