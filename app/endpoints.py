from fastapi import APIRouter, Response, status, HTTPException, Depends
from app.schemas import Post

from app.db.database import conn, cursor


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
    cursor.execute("""SELECT * FROM posts""")
    post = cursor.fetchall()
    return {"data": post}


@router.post("/createposts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}


@router.get("/posts/latest")
def get_latest_post():
    last = my_posts[len(my_posts) - 1]
    return {"detail": last}


@router.get("/posts/{id}")
def get_post_id(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    po_st = cursor.fetchone()
    # po_st = find_post(id)
    if not po_st:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"po_st with {id} not fount")
    return {"post_detail": po_st}


@router.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
                   (post.title, post.content, post.published, id))
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist")

    return {"data": updated_post}


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):  # delete post
    cursor.execute("""DELETE FROM POSTS WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    # {'message': "post was successfully deleted"}
