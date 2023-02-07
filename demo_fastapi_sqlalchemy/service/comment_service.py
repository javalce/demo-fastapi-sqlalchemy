#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""

from fastapi import Depends

from ..exception.comment_exception import CommentException
from ..model.comment import Comment
from ..repository.comment_repository import CommentRepository


class CommentService:
    def __init__(self, repository: CommentRepository = Depends()) -> None:
        self.repository = repository

    def find_all(self) -> list[Comment]:
        return self.repository.find_all()

    def find_by_id(self, id: int) -> Comment:
        comment = self.repository.find_by_id(id)

        if comment is None:
            raise CommentException.not_found(id)

        return comment

    def find_by_post(self, id_post: int) -> list[Comment]:
        return self.repository.find_by_id_post(id_post)

    def create(self, comment: Comment) -> Comment:
        if comment.id is not None:
            exists = self.repository.exists_by_id(comment.id)
            if exists:
                raise CommentException.resource_already_exists(comment.id)

        return self.repository.save(comment)

    def update(self, id: int, comment: Comment) -> Comment:
        old_comment = self.repository.find_by_id(id)

        if old_comment is None:
            raise CommentException.not_found(id)

        old_comment.email = comment.email
        old_comment.body = comment.body
        old_comment.name = comment.name

        return self.repository.save(old_comment)

    def delete(self, id: int) -> None:
        exists = self.repository.exists_by_id(id)

        if not exists:
            raise CommentException.not_found(id)

        self.repository.delete_by_id(id)
