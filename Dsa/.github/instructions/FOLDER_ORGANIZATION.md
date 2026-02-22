# Folder Organization Guide

## Two Options for Organizing Solutions

You have two folders available:

### 1. `algorithm_patterns/` - Organize by Solving Technique

Focus on **HOW** you solve the problem

**Best for**: Learning patterns and techniques

**Folders**:

- `arrays_and_hashing/` - Hash map techniques
- `two_pointers/` - Two pointer patterns
- `sliding_window/` - Sliding window technique
- `binary_search/` - Binary search patterns
- `stack/` - Stack-based solutions
- `backtracking/` - Backtracking algorithms
- `heap_priority_queue/` - Heap-based solutions
- `graphs/` - Graph algorithms (BFS, DFS, etc.)
- `dynamic_programming/` - DP patterns
- `greedy/` - Greedy algorithms
- `tree/` - Tree algorithm patterns

### 2. `data_structures/` - Organize by Data Structure

Focus on **WHAT** you're working with

**Best for**: Understanding data structures

**Folders**:

- `arrays_and_hashing/` - Array and hash table problems
- `linked_list/` - Linked list problems
- `stack/` - Stack problems
- `queue/` - Queue problems
- `tree/` - Tree problems
- `heap/` - Heap problems
- `graph/` - Graph problems
- `string/` - String problems
- `matrix/` - Matrix/2D array problems

## Decision Guide

### Use `algorithm_patterns/` when:

- You want to focus on learning solving techniques
- The pattern/technique is more important than the data structure
- Examples:
  - Two Sum → `algorithm_patterns/arrays_and_hashing/`
  - 3Sum → `algorithm_patterns/two_pointers/`
  - Longest Substring → `algorithm_patterns/sliding_window/`
  - Permutations → `algorithm_patterns/backtracking/`

### Use `data_structures/` when:

- You want to focus on mastering data structures
- The data structure is the main focus
- Examples:
  - Two Sum → `data_structures/arrays_and_hashing/`
  - Reverse Linked List → `data_structures/linked_list/`
  - Invert Binary Tree → `data_structures/tree/`
  - Valid Parentheses → `data_structures/stack/`

## Both Are Valid!

You can use **BOTH** folders and organize problems in different ways:

- Same problem can exist in both folders
- Choose based on what you want to emphasize
- No wrong choice - it's about your learning preference

## Quick Examples

| Problem            | algorithm_patterns/  | data_structures/    |
| ------------------ | -------------------- | ------------------- |
| Two Sum            | arrays_and_hashing/  | arrays_and_hashing/ |
| 3Sum               | two_pointers/        | arrays_and_hashing/ |
| Valid Parentheses  | stack/               | stack/              |
| Invert Binary Tree | tree/                | tree/               |
| Longest Substring  | sliding_window/      | string/             |
| Number of Islands  | graphs/              | graph/              |
| Climbing Stairs    | dynamic_programming/ | -                   |
| Find Duplicate     | arrays_and_hashing/  | arrays_and_hashing/ |

## AI Agent Behavior

When you provide a problem, the AI will:

1. Detect which folder you're currently using (if any)
2. Ask for your preference if unclear
3. Use the appropriate category based on your choice
4. Place the solution in the correct folder

## AI Agent Behavior

When you provide a problem, the AI will:

1. Detect which folder you're currently using (if any)
2. Ask for your preference if unclear
3. Use the appropriate category based on your choice
4. Place the solution in the correct folderur choice
5. Place the solution in the correct folder
