# compare sequential and concurrent executions

async def delete_files(filename):
    print(f"Starting execution {filename}....")
    asyncio.sleep(2)
    print(f"Deletion completed {filename}...")


    