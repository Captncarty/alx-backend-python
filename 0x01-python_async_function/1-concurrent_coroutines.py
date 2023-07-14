#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you've written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""


import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns a sorted list of float numbers gotten randomly"""
    wait_random = __import__('0-basic_async_syntax').wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await wait_random(max_delay))
        i += 1

    return sorted(delay_list)
