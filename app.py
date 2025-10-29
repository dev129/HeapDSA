import streamlit as st
import pandas as pd
import numpy as np
import heapq # We use Python's built-in heap implementation

# --- Configuration and Styling ---
st.set_page_config(
    page_title="Priority Scheduler Project",
    page_icon="🗓️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Tailwind-like styling using Markdown for a clean look
def apply_styles():
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #2563eb; /* Darker blue for action */
            color: black;
            padding: 10px 24px;
            border-radius: 8px;
            border: none;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #1e40af; /* Even darker blue on hover */
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
        }
        
        .css-1d391kg { /* Target for the main container */
            padding-top: 2rem;
        }
        .header-title {
            font-size: 2.5em;
            font-weight: 700;
            color: #1e3a8a; /* Dark blue */
        }
        .card {
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
            background-color: black;
        }
        .dsa-emphasis {
            font-weight: bold;
            color: #ef4444; /* Red emphasis for DSA terms */
        }
        </style>
    """, unsafe_allow_html=True)

apply_styles()

# Initialize session state for the task queue
if 'task_queue' not in st.session_state:
    # Structure: [(priority_value, task_name), ...]
    # Python's heapq is a min-heap, so LOWER priority value means HIGHER priority task.
    st.session_state.task_queue = [
        (3, "Send follow-up email (Low Priority)"),
        (1, "Fix critical server bug (Urgent)"),
        (2, "Review PRs (Medium Priority)"),
    ]
    # Heapify the initial list
    heapq.heapify(st.session_state.task_queue)

# --- Project Functions ---

def home_page():
    st.markdown('<p class="header-title">Project Showcase: Priority Task Scheduler 🗓️</p>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card">
        <h2 style='color: #2563eb;'>1. The Real-World Problem</h2>
        <p>In many applications—from operating systems managing CPU tasks to hospital systems scheduling surgeries—it is critical to process items based on their urgency, not just the order they arrived.</p>
        <p>We need a system that can quickly:
        <ul>
            <li>**Add** a new task with its priority.</li>
            <li>**Retrieve** the single most urgent task immediately.</li>
        </ul>
        </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("The Flawed Approach (List/Array)")
        st.code("""
tasks = [(10, 'Low'), (1, 'High'), (5, 'Medium')]
# To find the highest priority task:
# O(N) linear search
max(tasks, key=lambda x: x[0])
        """, language="python")
        st.error("Finding the highest priority task takes $O(N)$ time, which is too slow for millions of tasks.")

    with col2:
        st.subheader("The DSA Solution (Priority Queue / Min-Heap)")
        st.code("""
import heapq
heapq.heappush(tasks, (1, 'High'))
# To find/retrieve the highest priority task:
# O(1) peek, O(log N) pop
highest_priority_task = heapq.heappop(tasks)
        """, language="python")
        st.success("Retrieving the highest priority task takes $O(1)$ time, and adding/removing is only $O(\log N)$. This is the efficient, scalable solution.")

def priority_scheduler_page():
    st.markdown('<p class="header-title">2. Interactive Project Implementation</p>', unsafe_allow_html=True)

    # --- Add New Task ---
    with st.container():
        st.subheader("Add a New Task")
        colA, colB, colC = st.columns([3, 1, 1])
        
        with colA:
            new_task = st.text_input("Task Description:", placeholder="E.g., Deploy code update")
        with colB:
            # Lower number = Higher priority (Min-Heap convention)
            new_priority = st.number_input("Priority (1=High, 5=Low):", min_value=1, max_value=5, value=3, step=1)
        with colC:
            # Spacer for alignment
            st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True) 
            if st.button("Add Task to Queue"):
                if new_task:
                    # Use heapq.heappush to maintain the heap property
                    heapq.heappush(st.session_state.task_queue, (new_priority, new_task))
                    st.success(f"Added task: '{new_task}' with Priority {new_priority}.")
                else:
                    st.error("Please enter a task description.")

    st.markdown("---")

    # --- Process Task ---
    st.subheader("Process Next Task")
    
    # Process the most urgent task
    def process_next_task():
        if st.session_state.task_queue:
            # Use heapq.heappop to retrieve and remove the smallest (highest priority) item
            processed_task = heapq.heappop(st.session_state.task_queue)
            st.toast(f"✅ Processing: {processed_task[1]} (Priority {processed_task[0]})", icon='🔥')
        else:
            st.error("The task queue is currently empty!")

    st.button("Process Most Urgent Task", on_click=process_next_task)


    st.markdown("### Current Task Queue (Simulated Heap View)")
    if st.session_state.task_queue:
        # Display the current state of the heap
        df = pd.DataFrame(st.session_state.task_queue, columns=['Priority (Lower=Higher Urgency)', 'Task Description'])
        df = df.sort_values(by='Priority (Lower=Higher Urgency)')
        st.dataframe(df, use_container_width=True)
    else:
        st.info("The queue is clear! Great job!")

def dsa_deep_dive_page():
    st.markdown('<p class="header-title">3. DSA Deep Dive: The Min-Heap</p>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="card">
        <h3 style='color: #ef4444;'>Why the Heap is the Right Tool</h3>
        <p>The <span class="dsa-emphasis">Priority Queue</span> abstract data type is best implemented using a <span class="dsa-emphasis">Binary Heap</span>. This project uses a Min-Heap, where the element with the smallest key (our priority number) is always guaranteed to be at the root.</p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Heap Properties")
    st.markdown("""
    A Min-Heap maintains two crucial properties:
    1.  **Heap Property:** For every node $N$, the value of $N$ is less than or equal to the values of its children. This ensures the smallest element is always the root.
    2.  **Structure Property:** The heap is a complete binary tree, meaning all levels are fully filled, except possibly the last level, which is filled from left to right.
    """)
    

    st.subheader("Complexity Analysis")
    st.markdown("The key to the Heap's efficiency is its logarithmic time complexity for fundamental operations:")
    
    complexity_data = {
        'Operation': ['Access Minimum/Maximum (Peek)', 'Insert (Push)', 'Extract Minimum/Maximum (Pop)', 'Search (Worst Case)'],
        'Priority Queue (Heap)': ['$O(1)$', '$O(\log N)$', '$O(\log N)$', '$O(N)$'],
        'Unsorted List/Array': ['$O(N)$', '$O(1)$', '$O(N)$', '$O(N)$'],
        'Sorted List/Array': ['$O(1)$', '$O(N)$', '$O(N)$', '$O(\log N)$'],
    }
    
    df_complexity = pd.DataFrame(complexity_data)
    st.table(df_complexity)

    st.markdown(r"""
        <p>As shown, the Heap offers the best compromise, providing fast insertion and extraction operations—both crucial for a dynamic task scheduler—at $O(\log N)$ time, making the project scalable for large task lists.</p>
    """, unsafe_allow_html=True)


# --- Main Application Logic ---

# Sidebar for navigation
st.sidebar.title("Project Navigation")
page = st.sidebar.radio("Go to:", [
    "1. Problem & DSA Overview", 
    "2. Interactive Implementation", 
    "3. DSA Deep Dive"
])

# Display selected page
if page == "1. Problem & DSA Overview":
    home_page()
elif page == "2. Interactive Implementation":
    priority_scheduler_page()
elif page == "3. DSA Deep Dive":
    dsa_deep_dive_page()

st.sidebar.markdown("---")
st.sidebar.markdown("Project: Priority Task Scheduler (DSA: Min-Heap)")
