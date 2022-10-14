# from sqlalchemy.orm import Session
#
# from src import schemas
# from src.db.models import Item
#
#
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Folder).offset(skip).limit(limit).all()
#
#
# def get_item(db: Session, item: list):
#     return db.query(Folder).filter(Folder.item == item)
#
#
# def get_node(db: Session, node_id: str):
#     return db.query(Folder).filter(Folder.id == node_id).first()
#
#
# def delete_id(db: Session, node_id: str):
#     db_model = get_items(db, node_id)
#     if db_model is None:
#         return False
#     db.delete(db_model)
#     db.commit()
#     return True
