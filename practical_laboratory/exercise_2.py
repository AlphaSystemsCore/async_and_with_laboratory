# compare sequential and concurrent executions
import asyncio

async def delete_files(filename):
    
    print(f"Starting execution {filename}....")
    await asyncio.sleep(2)
    print(f"Deletion completed {filename}...")
    
   


async def main():
    start = time.perf_counter()
    await delete_files("backup.txt")
    await delete_files("backup-22.txt")
    await delete_files("backup-003.txt")
    end = time.perf_counter() - start
    print(f"Sequential Execution Time: {end.:3f}")


asyncio.run(main())