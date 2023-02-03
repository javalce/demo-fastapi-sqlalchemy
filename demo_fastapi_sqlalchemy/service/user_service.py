#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2023

@author: javalce
"""

from typing import List

from fastapi import Depends

from ..decorators import timeit
from ..exception.user_exception import UserNotFound
from ..model.user import User
from ..repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository = Depends()) -> None:
        self._repository: UserRepository = user_repository

    def find_all(self) -> List[User]:
        return self._repository.find_all()

    def find_by_id(self, id: int) -> User:
        self._repository.exists_by_id(id)
        user = self._repository.find_by_id(id)

        if user is None:
            raise UserNotFound(id)

        return user
