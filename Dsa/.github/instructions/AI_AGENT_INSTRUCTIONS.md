# AI Agent Instructions for DSA Problem Solutions

## Project Structure

```
Dsa/
├── algorithm_patterns/     # Organize by solving techniques
│   ├── arrays_and_hashing/
│   ├── two_pointers/
│   ├── sliding_window/
│   ├── stack/
│   ├── binary_search/
│   ├── backtracking/
│   ├── heap_priority_queue/
│   ├── graphs/
│   ├── dynamic_programming/
│   ├── greedy/
│   └── tree/
└── data_structures/        # Organize by data structure type
    ├── array/
    ├── arrays_and_hashing/
    ├── linked_list/
    ├── stack/
    ├── queue/
    ├── hash_table/
    ├── tree/
    ├── graph/
    ├── heap/
    ├── string/
    └── matrix/
```

**Note**: You can organize solutions in EITHER folder based on preference:

- `algorithm_patterns/` - Focus on the solving technique/pattern
- `data_structures/` - Focus on the primary data structure used

## Naming Conventions

### Folder Names

- **Style**: `snake_case` (Python PEP 8 convention)
- **Examples**: `arrays_and_hashing`, `two_pointers`, `dynamic_programming`
- **Rationale**: Readability for multi-word folder names

### File Names

- **Style**: `LC###_PascalCase.py` (Java-inspired style)
- **Format**: `LC{problem_number}_{ProblemName}.py`
- **Examples**:
  - `LC001_TwoSum.py`
  - `LC049_GroupAnagrams.py`
  - `LC287_FindDuplicate.py`
- **Rationale**:
  - Easy to search LeetCode problem
  - Auto-sort by problem number
  - Track progress visually
  - Professional appearance

### Class and Method Names

- **Class**: Use LeetCode's default `Solution` class
- **Methods**: Use `camelCase` (matching LeetCode interface)
- **Rationale**: Maintains compatibility with LeetCode platform

## File Template Structure

Every solution file MUST include:

1. **Header Comment Block**
   - LeetCode problem number and title
   - Difficulty level
   - Problem link
   - Brief problem description
   - Algorithm/approach name
   - Time complexity
   - Space complexity

2. **Imports**
   - Standard library imports
   - Type hints from `typing`

3. **Solution Class**
   - LeetCode-compatible `Solution` class
   - Well-commented implementation
   - Clear variable names

4. **Test Cases**
   - `if __name__ == "__main__":` block
   - At least 3 test cases
   - Expected output shown in comments

## Code Style Guidelines

### Python Style

- **Python 3.12+ Style**: Use modern Python 3.12+ features and conventions
- **Type Hints**: Always use type hints for function signatures (from `typing` module)
- **No Nested Functions**: Define helper methods as class methods instead of nested functions
- **Variable Naming**: Use camelCase for local variables (e.g., `leftHeight`, `rightHeight`, not `left_height`)
- **PEP 8**: Follow PEP 8 for code formatting (except variable naming - use camelCase)
- **Descriptive Names**: Write clear, descriptive variable names
- **Comments**: Add inline comments for complex logic

### Nested Functions Rule

❌ **DON'T** use nested functions:

```python
class Solution:
    def method(self, root):
        def helper(node):  # Nested function - AVOID
            pass
        return helper(root)
```

✅ **DO** use class methods:

```python
class Solution:
    def method(self, root):
        return self.helper(root)

    def helper(self, node):  # Class method - PREFERRED
        pass
```

### Documentation

- Clear explanation of algorithm approach
- Big O analysis in header
- Comments for non-obvious steps

### Testing

- Include edge cases
- Show expected vs actual output
- Use print statements for verification

## Category Assignment Rules

You can organize solutions in EITHER `algorithm_patterns/` OR `data_structures/` folder.

### algorithm_patterns/ (Organize by Technique)

- **arrays_and_hashing/**: Hash maps, frequency counting, sets
- **two_pointers/**: Left/right pointers, fast/slow pointers
- **sliding_window/**: Fixed/variable window problems
- **stack/**: Stack-based solutions, monotonic stack
- **binary_search/**: Binary search, divide and conquer
- **backtracking/**: DFS with backtracking, permutations
- **heap_priority_queue/**: Heap operations, priority queue, top K
- **graphs/**: Graph traversal, BFS, DFS, shortest path
- **dynamic_programming/**: DP, memoization, tabulation
- **greedy/**: Greedy algorithms, interval problems
- **tree/**: Tree traversal patterns, tree algorithms

### data_structures/ (Organize by Data Structure)

- **arrays_and_hashing/**: Hash maps, frequency counting, sets, array problems
- **linked_list/**: Linked list manipulation, cycle detection, node operations
- **stack/**: Stack-based solutions, monotonic stack, LIFO operations
- **queue/**: Queue operations, FIFO, deque
- **tree/**: Binary trees, BST, tree traversal, tree operations
- **heap/**: Heap operations, priority queue, top K problems
- **graph/**: Graph traversal, BFS, DFS, shortest path
- **string/**: String manipulation, pattern matching
- **matrix/**: Matrix operations, 2D array problems

**Rule**: Choose the folder and category based on:

1. User preference (if specified)
2. PRIMARY technique used (for algorithm_patterns)
3. PRIMARY data structure used (for data_structures)

## Workflow for Creating Solution Files

1. **Identify Problem Details**
   - LeetCode number
   - Problem name
   - Difficulty
   - Main technique/pattern OR data structure used

2. **Determine Category**
   - Ask user or determine from context which folder to use
   - If algorithm_patterns: choose by primary solving technique
   - If data_structures: choose by primary data structure
   - Place in appropriate folder

3. **Create File**
   - Use naming format: `LC###_ProblemName.py`
   - Apply template structure

4. **Write Solution**
   - Add header documentation
   - Implement solution with Python 3.12+ style
   - Use class methods instead of nested functions
   - Include type hints
   - Add comments for clarity
   - Include test cases

5. **Verify**
   - No nested functions used
   - All type hints present
   - Run test cases
   - Check output matches expected results
   - Ensure code follows style guidelines

## Example Categories for Common Problems

### algorithm_patterns/ examples:

- Two Sum (1) → `arrays_and_hashing/`
- Valid Palindrome (125) → `two_pointers/`
- Longest Substring (3) → `sliding_window/`
- Valid Parentheses (20) → `stack/`
- Binary Search (704) → `binary_search/`
- Permutations (46) → `backtracking/`
- Number of Islands (200) → `graphs/`
- Climbing Stairs (70) → `dynamic_programming/`

### data_structures/ examples:

- Two Sum (1) → `arrays_and_hashing/`
- Add Two Numbers (2) → `linked_list/`
- Longest Substring (3) → `string/`
- Valid Parentheses (20) → `stack/`
- Merge K Sorted Lists (23) → `heap/`
- Invert Binary Tree (226) → `tree/`
- Number of Islands (200) → `graph/`
- Find Duplicate (287) → `arrays_and_hashing/`

## Response Format

When user provides a problem/code, respond with:

1. Confirm category placement
2. Create file with full template
3. Mention file location
4. Note any special categorization considerations

## Quality Checklist

Before finalizing a file, ensure:

- [ ] Correct naming format (LC###\_ProblemName.py)
- [ ] Complete header documentation
- [ ] Python 3.12+ style with type hints
- [ ] NO nested functions (use class methods)
- [ ] camelCase for variable names (leftHeight not left_height)
- [ ] Code is well-commented
- [ ] Test cases included
- [ ] Big O analysis provided
- [ ] File placed in correct folder (algorithm_patterns/ OR data_structures/)
- [ ] Code follows PEP 8 (except camelCase for methods/variables per LeetCode style)
