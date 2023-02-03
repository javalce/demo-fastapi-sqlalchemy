#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 2023

@author: javalce
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="demo_fastapi_sqlalchemy.main:create_app", factory=True, reload=True
    )
