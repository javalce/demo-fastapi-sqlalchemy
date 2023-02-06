#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""


from fastapi import Depends

from ..exception.post_exception import PostException
from ..model.post import Post
from ..repository.post_repository import PostRepository


class PostService:
    def __init__(self, repository: PostRepository = Depends()) -> None:
        self.repository = repository

    def find_all(self) -> list[Post]:
        return self.repository.find_all()

    def find_by_id(self, id: int) -> Post:
        post = self.repository.find_by_id(id)

        if post is None:
            raise PostException.not_found(id)

        return post

    def create(self, post: Post) -> Post:
        return self.repository.save(post)

    def update(self, id: int, post: Post) -> Post:
        old_post = self.repository.find_by_id(id)

        if old_post is None:
            raise PostException.not_found(id)

        old_post.title = post.title
        old_post.body = post.body

        return self.repository.save(old_post)

    def delete(self, id: int) -> None:
        exists = self.repository.exists_by_id(id)

        if not exists:
            raise PostException.not_found(id)

        self.repository.delete_by_id(id)
