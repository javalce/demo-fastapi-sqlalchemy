#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2023

@author: javalce
"""


from fastapi import FastAPI

from . import settings
from .controller import comment_controller, post_controller
from .database import DBSessionMiddleware


def create_app() -> FastAPI:
    app = FastAPI(title="Demo FastAPI + SQLAlchemy")

    app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)

    app.include_router(post_controller.router)
    app.include_router(comment_controller.router)

    return app
