# compare sequential and concurrent executions
import asyncio
import time

async def delete_files(filename):
    
    print(f"Starting execution {filename}....")
    await asyncio.sleep(2)
    print(f"Deletion completed {filename}...")
    
async def main():
    # concurrent execution 
    start = time.perf_counter()
    await asyncio.gather(
        delete_files("backup.txt"),
        delete_files("backup_1.txt"),
        delete_files("backup_2.txt")
    )
    print(f"Concurrent execution time: {time.perf_counter() - start:.3f}")


# async def main():
#     sequential implementation
#     start = time.perf_counter()
#     await delete_files("backup.txt")
#     await delete_files("backup-22.txt")
#     await delete_files("backup-003.txt")
#     end = time.perf_counter() - start
#     print(f"Sequential Execution Time: {end:.3f}")

# metrics;
# sequential execution took: 6.006 seconds
# concurrent execution took: 2.002 seconds

asyncio.run(main())