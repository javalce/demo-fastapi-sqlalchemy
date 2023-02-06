#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""
from fastapi import APIRouter, Depends, status

from ..dto.comment_dto import CommentDTO
from ..dto.post_dto import PostDTO
from ..model.comment import Comment
from ..service.comment_service import CommentService
from ..service.post_service import PostService

router = APIRouter(prefix="/comments", tags=["comments"])


@router.get("", status_code=status.HTTP_200_OK, response_model=list[CommentDTO])
def find_comments(comment_service: CommentService = Depends()):
    return comment_service.find_all()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CommentDTO)
def find_comment(id: int, comment_service: CommentService = Depends()):
    return comment_service.find_by_id(id)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=CommentDTO)
def create_comment(dto: CommentDTO, comment_service: CommentService = Depends()):
    comment = Comment(**dto.dict())
    return comment_service.create(comment)


@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=CommentDTO)
def update_comment(
    id: int, dto: CommentDTO, comment_service: CommentService = Depends()
):
    comment = Comment(**dto.dict())
    return comment_service.update(id, comment)


@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=None)
def delete_comment(id: int, comment_service: CommentService = Depends()):
    comment_service.delete(id)
