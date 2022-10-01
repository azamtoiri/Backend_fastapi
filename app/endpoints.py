from fastapi import APIRouter, Response, status, HTTPException
from app.schemas import Post
from random import randrange

router = APIRouter()

my_posts = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1
    },
    {
        "title": "favorite foods",
        "content": "I like pizza",
        "id": 2
    }
]


def find_post(id):  # find post
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
    return None


@router.get("/")
def root():
    return {"hello": "You are on main page"}


@router.get("/posts")
def get_posts():
    return {"data": my_posts}


@router.post("/createposts", status_code=status.HTTP_201_CREATED)
def create_posts(body: Post, ):
    post_dict = body.dict()
    post_dict['id'] = randrange(0, 10001)
    my_posts.append(post_dict)
    return {"data": post_dict}


@router.get("/posts/latest")
def get_latest_post():
    last = my_posts[len(my_posts) - 1]
    return {"detail": last}


@router.get("/posts/{id}")
def get_post_id(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} not fount")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f"post with {id} not fount"}
    return {"post_detail": post}


@router.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):  # delete post
    index = find_index(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    # {'message': "post was successfully deleted"}
