import asyncio

async def greet():
    print("Hello...")
    await asyncio.sleep(2)  # Simulates waiting (e.g. network call)
    print("...World!")

async def main():
    await asyncio.gather(greet(), greet(), greet())  # All run "together"

asyncio.run(main())