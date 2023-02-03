#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2023

@author: javalce
"""

from typing import List

from fastapi import APIRouter, Depends

from ..decorators import timeit
from ..dto import UserDTO
from ..service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", status_code=200, response_model=List[UserDTO])
@timeit
def find_users(user_service: UserService = Depends()):
    return user_service.find_all()


@router.get("/{id_user}", status_code=200, response_model=UserDTO)
@timeit
def find_user(id_user: int, user_service: UserService = Depends()):
    return user_service.find_by_id(id_user)
