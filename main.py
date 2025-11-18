
import uvicorn
from fastapi import FastAPI

import post

app = FastAPI()

app.include_router(post.router)

@app.get('/')
def read_root():
    return {"message": "A sample post API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
