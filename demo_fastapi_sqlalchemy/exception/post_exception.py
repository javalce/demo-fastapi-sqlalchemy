#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 2023

@author: javalce
"""

from .exception import NotFoundException, ResourceAlreadyExistsException


class PostException:
    @classmethod
    def not_found(cls, id: int) -> NotFoundException:
        return NotFoundException(f"Post with id '{id}' not found")

    @classmethod
    def resource_already_exists(cls, id: int) -> ResourceAlreadyExistsException:
        return ResourceAlreadyExistsException(f"Post with id '{id}' already exists")
