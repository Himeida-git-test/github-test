from fastapi import APIRouter

router=APIRouter(prefix='/post', tags=["post"])

@router.get('/')
def home() :
    print("Hello World")
    return {"msg" : 'Hello'} 