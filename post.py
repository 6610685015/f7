from uuid import uuid4 as uuid

from fastapi import APIRouter, HTTPException

from models import Post

posts = []

router = APIRouter()

@router.get('/posts')
def get_posts():
    return posts

@router.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.model_dump())
    return posts[-1]

@router.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post has been deleted succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@router.put('/posts/{post_id}')
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"]= updatedPost.model_dump()["title"]
            posts[index]["content"]= updatedPost.model_dump()["content"]
            posts[index]["author"]= updatedPost.model_dump()["author"]
            return {"message": "Post has been updated succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")


