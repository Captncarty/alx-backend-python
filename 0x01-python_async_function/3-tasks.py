#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.
Write a function (do not create an async function, use the regular
function syntax to do this) task_wait_random that takes an integer
max_delay and returns a asyncio.Task.
"""


import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function that creates a task for the scheduler"""

    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))
