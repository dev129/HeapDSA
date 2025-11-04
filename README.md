# HeapDSA: Priority Task Scheduler 🗓️

## Project Overview

The **HeapDSA: Priority Task Scheduler** is an interactive web application built with Streamlit that demonstrates the power and efficiency of the **Min-Heap** data structure for implementing a **Priority Queue**. This project addresses the common real-world problem of managing tasks or events where processing order is determined by urgency rather than arrival time.

From operating systems scheduling CPU processes to hospital systems prioritizing patient care, the ability to quickly add new prioritized items and retrieve the most urgent one is critical. This application provides a hands-on experience with how a Min-Heap efficiently solves this challenge, offering significant performance improvements over simpler data structures.

## ✨ Features

-   **Interactive Task Management**: Add new tasks with custom priority levels (1=High, 5=Low).
-   **Priority-Based Processing**: Simulate processing the "most urgent" task from the queue with a single click.
-   **Real-time Queue Visualization**: See the current state of the task queue, sorted by priority, reflecting the heap's underlying logic.
-   **DSA Problem & Solution Overview**: Clear explanation of the real-world problem and why traditional approaches fall short.
-   **Deep Dive into Min-Heaps**: Detailed explanation of Min-Heap properties, its advantages, and a comprehensive complexity analysis comparing it with other data structures.
-   **Clean User Interface**: A responsive and intuitive interface built with Streamlit and custom CSS for an enhanced user experience.

## 💡 The Problem: Why Simple Lists Fail

Consider a scenario where you need to manage a list of tasks, each with an associated priority. If you use a simple Python list or array, finding the highest priority task requires iterating through the entire list.

```python
tasks = [(10, 'Low'), (1, 'High'), (5, 'Medium')]
# To find the highest priority task:
# O(N) linear search
max(tasks, key=lambda x: x[0])
```

This approach has a time complexity of **O(N)**, meaning that as the number of tasks (`N`) grows, the time taken to find the most urgent task increases linearly. For systems managing millions of tasks, this becomes prohibitively slow and inefficient.

## 🚀 The Solution: Priority Queue with a Min-Heap

The optimal solution for a priority-based system is a **Priority Queue**, which is most efficiently implemented using a **Binary Heap**. Specifically, this project uses a **Min-Heap**, where the element with the smallest key (our priority number) is always at the root.

Python's built-in `heapq` module provides the necessary heap queue algorithm, allowing us to maintain the heap property efficiently.

```python
import heapq

tasks = [] # Initialize an empty list to be used as a heap
heapq.heappush(tasks, (3, "Send follow-up email")) # (priority, task_description)
heapq.heappush(tasks, (1, "Fix critical server bug"))
heapq.heappush(tasks, (2, "Review PRs"))

# To retrieve and remove the highest priority task (smallest priority value):
# O(log N) pop
highest_priority_task = heapq.heappop(tasks) 
# Result: (1, 'Fix critical server bug')
```

With a Min-Heap, retrieving the highest priority task (peeking at the root) takes **O(1)** time, and adding (`heappush`) or removing (`heappop`) a task takes only **O(log N)** time. This logarithmic complexity ensures scalability and high performance even with very large task queues.

### Min-Heap Properties

A Min-Heap maintains two crucial properties:

1.  **Heap Property**: For every node `N`, the value of `N` is less than or equal to the values of its children. This guarantees that the smallest element is always at the root.
2.  **Structure Property**: The heap is a complete binary tree, meaning all levels are fully filled, except possibly the last level, which is filled from left to right. This property ensures efficient memory usage and allows for array-based representation.

### Complexity Analysis

The efficiency of the Heap is evident when compared to other common data structures:

| Operation                       | Priority Queue (Heap) | Unsorted List/Array | Sorted List/Array |
| :------------------------------ | :-------------------- | :------------------ | :---------------- |
| Access Minimum/Maximum (Peek)   | $O(1)$                | $O(N)$              | $O(1)$            |
| Insert (Push)                   | $O(\log N)$           | $O(1)$              | $O(N)$            |
| Extract Minimum/Maximum (Pop)   | $O(\log N)$           | $O(N)$              | $O(N)$            |
| Search (Worst Case)             | $O(N)$                | $O(N)$              | $O(\log N)$       |

As shown, the Heap offers the best compromise, providing fast insertion and extraction operations—both crucial for a dynamic task scheduler—at $O(\log N)$ time, making the project scalable for large task lists.

## ⚙️ How to Run Locally

Follow these steps to set up and run the Priority Task Scheduler on your local machine.

### Prerequisites

-   Python 3.7+
-   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/HeapDSA.git
    cd HeapDSA
    ```
    *(Note: Replace `your-username` with the actual GitHub username if this project is hosted.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    # If requirements.txt is not present, install manually:
    # pip install streamlit pandas numpy
    ```

### Running the Application

1.  **Navigate to the project directory** (if you're not already there):
    ```bash
    cd HeapDSA
    ```

2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

    This command will open the application in your default web browser, typically at `http://localhost:8501`.

## 📂 Project Structure

```
HeapDSA/
├── app.py              # Main Streamlit application logic
├── README.md           # This file
└── requirements.txt    # (Optional) List of Python dependencies
```

## 🛠️ Technologies Used

-   **Python**: The core programming language.
-   **Streamlit**: For building the interactive web application.
-   **`heapq`**: Python's built-in module for heap queue algorithm (Min-Heap implementation).
-   **Pandas**: For structured data handling and display in the Streamlit app.
-   **NumPy**: Used by Pandas internally, and generally good for numerical operations.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

## 📄 License

This project is open-source and available under the MIT License.

---

**Developed with ❤️ for Data Structures & Algorithms enthusiasts.**
