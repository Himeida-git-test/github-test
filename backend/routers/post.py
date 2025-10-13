from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter(
    prefix="/posts",
    tags=['Post']
)

class Post(BaseModel):
    id: int
    title: str
    content: str

class PostCreate(BaseModel):
    title: str
    content: str

fake_posts_db: Dict[int, Post] = {
    1: Post(id=1, title="첫 번째 게시글", content="안녕하세요! FastAPI 예시입니다."),
    2: Post(id=2, title="점심 메뉴 추천", content="오늘은 무엇을 먹을까요?"),
    3: Post(id=3, title="오늘의 날씨", content="날씨가 매우 맑습니다."),
}
latest_post_id = 3

@router.get("/", response_model=List[Post])
def get_all_posts():
    return list(fake_posts_db.values())

@router.get("/{post_id}", response_model=Post)
def get_post_by_id(post_id: int):
    post = fake_posts_db.get(post_id)
    if not post:
      
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="게시글을 찾을 수 없습니다.")
    return post

@router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(post_create: PostCreate):
    global latest_post_id
    latest_post_id += 1 # 

    new_post = Post(
        id=latest_post_id,
        title=post_create.title,
        content=post_create.content
    )
    fake_posts_db[new_post.id] = new_post
    return new_post


@router.put("/{post_id}", response_model=Post)
def update_post(post_id: int, post_update: PostCreate):
    post = fake_posts_db.get(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="수정할 게시글을 찾을 수 없습니다.")

    post.title = post_update.title
    post.content = post_update.content
    return post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):

    if post_id not in fake_posts_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="삭제할 게시글을 찾을 수 없습니다.")
    
    del fake_posts_db[post_id]
    return