#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2023

@author: javalce
"""


from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy import inspect, select
from sqlalchemy.orm import Session

from . import Base, db

T = TypeVar("T", bound=Base)
K = TypeVar("K")


class CRUDRepository(Generic[T, K]):
    def __init__(self, model: Type[T]) -> None:
        self.model = model

    @property
    def session(self) -> Session:
        return db.session

    def find_all(self) -> List[T]:
        stm = select(self.model)
        return self.session.scalars(stm).all()

    def find_by_id(self, id: K) -> Optional[T]:
        return self.session.get(self.model, id)

    def exists_by_id(self, id: K) -> bool:
        primary_key = inspect(self.model).primary_key
        if len(primary_key) == 1:
            primary_key = primary_key[0]
        query = select(select(self.model).where(primary_key == id).exists())
        return self.session.scalar(query)

    def save(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        return entity

    def save_all(self, entities: List[T]) -> List[T]:
        self.session.add_all(entities)
        self.session.commit()
        return entities

    def delete(self, entity: T) -> None:
        self.session.delete(entity)
        self.session.commit()

    def delete_by_id(self, id: K) -> None:
        entity = self.session.get(self.model, id)
        self.delete(entity)
