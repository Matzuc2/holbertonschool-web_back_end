from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The created asyncio.Task object.
    """
    return create_task(wait_random(max_delay))
