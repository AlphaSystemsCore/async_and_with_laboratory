# Async and With Laboratory

A practical Python laboratory exploring synchronous execution, asynchronous programming, and resource management using context managers.

## About This Laboratory

This laboratory was created to understand why asynchronous programming exists, what limitations it addresses, and why it should not automatically be the first choice for every application.

Rather than jumping directly into `async` and `await`, I started by running synchronous code to observe its behavior and understand its limitations.

I also explored Python's `with` statement to understand how context managers help manage resources and ensure proper cleanup.

The goal is to understand the concepts through practical experiments rather than simply memorizing syntax.

## Learning Objectives

- Understand how synchronous code executes.
- Identify the limitations of synchronous execution when dealing with I/O-bound operations.
- Understand asynchronous programming and why it is useful.
- Learn how `async`, `await`, and `asyncio` work together.
- Understand the difference between concurrency and parallelism.
- Explore Python's `with` statement and context managers.
- Understand how resources are acquired, used, and released.
- Learn when to use `with` versus `async with`.
- Develop the ability to choose an appropriate execution model based on the problem.

## Experiments

### 1. Understanding Synchronous Execution

**Objective:** Observe how synchronous code executes operations and identify its limitations.

I started by running synchronous code to understand how a program executes operations sequentially.

In synchronous execution, when an operation must finish before the next operation can proceed, the program waits for that operation to complete.

This behavior is straightforward and easy to understand, but it can become inefficient when a program performs multiple independent I/O operations.

For example, when making several HTTP requests sequentially, the program waits for each response before proceeding to the next request.

**What I learned:**

- Synchronous code is straightforward and predictable.
- Operations can block progress while waiting for external resources.
- Sequential I/O operations can increase total execution time.
- Synchronous execution remains appropriate for many applications.

### 2. Exploring Asynchronous Programming

**Objective:** Understand how asynchronous programming allows multiple operations to make progress without waiting for each operation to finish sequentially.

After observing synchronous execution, I explored asynchronous programming using Python's `async` and `await` syntax.

Asynchronous programming allows a coroutine to suspend while waiting for an operation to complete, giving the event loop an opportunity to run other tasks.

Consider the following example:

```python
import asyncio


async def perform_task(name: str, delay: float) -> None:
    print(f"{name} started")

    await asyncio.sleep(delay)

    print(f"{name} completed")


async def main() -> None:
    await asyncio.gather(
        perform_task("Task A", 2),
        perform_task("Task B", 2),
        perform_task("Task C", 2),
    )


asyncio.run(main())
```

In this example:

- `async def` defines a coroutine function.
- `await` suspends the current coroutine while an awaitable operation is in progress.
- `asyncio.sleep()` allows other tasks to run while the coroutine waits.
- `asyncio.gather()` schedules multiple awaitables and waits for their results.
- `asyncio.run()` starts the event loop and runs the main coroutine.

The three tasks can overlap their waiting periods instead of waiting for each task to finish before starting another.

**What I learned:**

- Asynchronous programming is useful for coordinating concurrent I/O operations.
- Coroutines can suspend and resume during execution.
- The event loop coordinates the execution of asynchronous tasks.
- Asynchronous programming does not automatically make every operation faster.
- Blocking operations can prevent other tasks from making progress on the same event-loop thread.

### 3. Understanding Why Async Is Not Automatically the First Choice

**Objective:** Understand when asynchronous programming is appropriate and when synchronous execution is sufficient.

One of the central questions in this laboratory was:

**Why should I use asynchronous programming if synchronous programming already works?**

The answer depends on the workload, concurrency requirements, libraries, and complexity of the application.

For example, a script that reads a small file and prints its contents might not benefit from asynchronous programming.

However, a backend application handling many concurrent HTTP requests may benefit from asynchronous I/O when its dependencies support it.

| Workload | Possible approach | Reason |
|---|---|---|
| Simple scripts | Synchronous | Simple and easy to maintain |
| Sequential operations | Synchronous or asynchronous | The next operation may depend on the previous result |
| Multiple independent HTTP requests | Asynchronous | Requests can overlap their waiting periods |
| Many concurrent network connections | Asynchronous | Can coordinate numerous I/O operations efficiently |
| CPU-intensive calculations | CPU-parallel techniques when appropriate | Async alone does not execute CPU-bound calculations in parallel |
| Blocking database or file operations | Synchronous or suitable offloading techniques | Blocking operations can stall an event loop |

**What I learned:**

- Asynchronous programming introduces additional concepts and complexity.
- The performance benefits depend on the workload.
- I/O-bound workloads often benefit more than CPU-bound workloads.
- Asynchronous code requires compatible libraries or appropriate strategies for blocking operations.
- Choosing the right execution model requires understanding the problem first.

The objective is not to use async everywhere, but to understand when it provides a meaningful advantage.

### 4. Resource Management with `with`

**Objective:** Understand how Python context managers help manage resources and perform cleanup.

After exploring execution models, I investigated Python's `with` statement.

Programs frequently acquire resources that must be released after use. Examples include:

- Files
- Database connections
- Locks
- Network clients
- Other objects that support context management

Without proper resource management, resources may remain open when an operation finishes or an exception occurs.

Consider this example:

```python
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python resource management.")
```

The `with` statement uses a context manager to manage the file's lifecycle.

When execution leaves the block, Python invokes the context manager's exit mechanism. For a file opened this way, that means the file is closed, including when an exception occurs inside the block.

A context manager implements the methods `__enter__()` and `__exit__()`.

**What I learned:**

- Resources have lifecycles that must be managed.
- Context managers provide a structured way to acquire and release resources.
- The `with` statement helps prevent resource leaks.
- Cleanup can occur even when an exception interrupts the block.
- Resource management makes code cleaner and more reliable.

### 5. Exploring `async with`

**Objective:** Understand how asynchronous resource management differs from ordinary context management.

Python also provides `async with` for resources that implement the asynchronous context manager protocol.

Consider an example using HTTPX:

```python
import asyncio
import httpx


async def fetch_data(url: str) -> None:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        print(response.status_code)
        print(response.text)


asyncio.run(fetch_data("https://example.com"))
```

This example combines asynchronous execution with resource management.

**Understanding each component:**

- `async def` defines a coroutine.
- `async with` manages the lifecycle of the asynchronous HTTP client.
- `httpx.AsyncClient()` creates an asynchronous HTTP client.
- `await client.get(url)` performs an asynchronous HTTP request.
- `response.status_code` accesses the HTTP response status.
- `asyncio.run()` runs the main coroutine.

When execution leaves the `async with` block, the asynchronous client's cleanup mechanism runs.

An asynchronous context manager implements `__aenter__()` and `__aexit__()`, which may perform asynchronous setup and cleanup.

**What I learned:**

- `with` and `async with` both support structured resource management.
- `with` uses the synchronous context manager protocol.
- `async with` uses the asynchronous context manager protocol.
- `async with` is appropriate for resources whose lifecycle is managed asynchronously.
- Resource management and asynchronous execution solve different problems but can work together.

## Key Concepts

| Concept | Purpose |
|---|---|
| Synchronous execution | Executes operations according to ordinary sequential control flow |
| Asynchronous programming | Allows coroutines to suspend while other tasks make progress |
| `async def` | Defines a coroutine function |
| `await` | Suspends a coroutine until an awaitable operation can provide its result |
| `asyncio` | Provides Python's asynchronous programming infrastructure |
| Event loop | Coordinates asynchronous tasks and callbacks |
| Concurrency | Allows multiple tasks to make progress over overlapping periods |
| Parallelism | Allows multiple operations to execute simultaneously |
| `with` | Manages resources through the synchronous context manager protocol |
| `async with` | Manages resources through the asynchronous context manager protocol |
| Context manager | Defines how a resource or operation is entered and exited |

## Technologies Used

- Python
- `asyncio`
- `httpx`
- Context managers
- Synchronous programming
- Asynchronous programming
- HTTP communication

## Running the Experiments

### 1. Clone the Repository

```bash
git clone https://github.com/AlphaSystemsCore/async_and_with_laboratory.git
cd <repository-directory>
```

Replace the placeholders with your repository URL and directory name.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Linux:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install httpx
```

### 5. Run an Experiment

```bash
python your_experiment.py
```

Replace `your_experiment.py` with the filename of the experiment you want to run.

## Lessons Learned

This laboratory helped me explore several important programming concepts:

1. **Understand before optimizing:** Learn how the existing execution model behaves before introducing a more complex alternative.
2. **Synchronous execution has its place:** Not every operation needs asynchronous programming.
3. **Async is useful for I/O-bound concurrency:** Independent operations can overlap their waiting periods when the relevant libraries support asynchronous execution.
4. **Concurrency is not parallelism:** Multiple tasks making progress concurrently does not necessarily mean they execute simultaneously.
5. **Resources require proper cleanup:** Files, connections, and other resources must be released appropriately.
6. **Context managers simplify cleanup:** The `with` statement provides a structured resource-management mechanism.
7. **Asynchronous resources need appropriate management:** `async with` supports resources that implement the asynchronous context manager protocol.
8. **Understand the trade-offs:** Good engineering means selecting a solution based on requirements rather than following a trend.

## Future Improvements

Potential extensions to this laboratory include:

- Benchmark synchronous and asynchronous HTTP requests under the same conditions.
- Measure execution time for different numbers of concurrent requests.
- Explore what happens when blocking functions are called inside asynchronous code.
- Investigate asynchronous database access.
- Implement a custom context manager using `__enter__()` and `__exit__()`.
- Implement an asynchronous context manager using `__aenter__()` and `__aexit__()`.
- Explore exception handling and cleanup behavior.
- Examine how connection pooling affects HTTP request performance.

## Conclusion

The purpose of this laboratory is to develop a practical understanding of Python's execution models and resource-management mechanisms.

By starting with synchronous execution, investigating its limitations, exploring asynchronous programming, and examining context managers, I aim to understand not only how these features work but also why they exist.

The central lesson is that good engineering requires more than knowing the syntax. It requires understanding the problem, evaluating possible solutions, and choosing an appropriate approach based on correctness, performance, complexity, and maintainability.

**Approach:** Experiment, observe, measure, and reason before drawing conclusions.