from fastapi import APIRouter

router = APIRouter(prefix='/users', tags=['User'])

@router.get('/')
def login():
    return "로그인"