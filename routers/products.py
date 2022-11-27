from typing import Union
from fastapi import APIRouter


router = APIRouter(tags=["Product API"])


@router.get("/products")
def get_items():
    return []


@router.post("/products")
def create_item():
    return {}


@router.get("/product/{item_id}")
def get_item(item_id: int, sortby: Union[str, None] = None):
    return {"item_id": item_id}


@router.patch("product/{item_id}")
def update_item(item_id: int):
    return {"item_id": item_id}


@router.delete("/product/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id}