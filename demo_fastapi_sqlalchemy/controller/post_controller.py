#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""

from fastapi import APIRouter, Depends, status

from ..dto.comment_dto import CommentDTO
from ..dto.post_dto import PostDTO
from ..model.post import Post
from ..service.comment_service import CommentService
from ..service.post_service import PostService

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", status_code=status.HTTP_200_OK, response_model=list[PostDTO])
def find_posts(post_service: PostService = Depends()):
    return post_service.find_all()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=PostDTO)
def find_posts(id: int, post_service: PostService = Depends()):
    return post_service.find_by_id(id)


@router.get(
    "/{id}/comments", status_code=status.HTTP_200_OK, response_model=list[CommentDTO]
)
def find_post_comments(id: int, comment_service: CommentService = Depends()):
    return comment_service.find_by_post(id)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=PostDTO)
def create_post(dto: PostDTO, post_service: PostService = Depends()):
    post = Post(**dto.dict())
    return post_service.create(post)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=PostDTO)
def update_post(id: int, dto: PostDTO, post_service: PostService = Depends()):
    post = Post(**dto.dict())
    return post_service.update(id, post)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_post(id: int, post_service: PostService = Depends()):
    post_service.delete(id)
