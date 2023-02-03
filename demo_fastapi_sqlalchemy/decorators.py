#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 2023

@author: javalce
"""

import time
from functools import wraps
from typing import Any, Callable


def timeit(func: Callable[..., Any]):
    @wraps(func)
    def timeit_wrapper(*args: Any, **kwargs: Any):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper
