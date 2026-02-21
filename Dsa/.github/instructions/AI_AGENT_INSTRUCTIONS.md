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
│   ├── linked_list/
│   ├── trees/
│   ├── heap_priority_queue/
│   ├── backtracking/
│   ├── graphs/
│   ├── dynamic_programming/
│   └── greedy/
└── data_structures/        # Organize by data structure type
    ├── array/
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

- Follow PEP 8 for code formatting
- Use type hints for function signatures
- Write descriptive variable names
- Add inline comments for complex logic

### Documentation

- Clear explanation of algorithm approach
- Big O analysis in header
- Comments for non-obvious steps

### Testing

- Include edge cases
- Show expected vs actual output
- Use print statements for verification

## Category Assignment Rules

When creating a new solution file, determine the PRIMARY category:

### algorithm_patterns/

- **arrays_and_hashing**: Hash maps, frequency counting, sets
- **two_pointers**: Left/right pointers, fast/slow pointers
- **sliding_window**: Fixed/variable window problems
- **stack**: Stack-based solutions, monotonic stack
- **binary_search**: Search, bisect, divide and conquer
- **linked_list**: Linked list manipulation, cycle detection
- **trees**: Binary trees, BST, tree traversal
- **heap_priority_queue**: Heap operations, priority queue
- **backtracking**: DFS with backtracking, permutations
- **graphs**: Graph traversal, BFS, DFS, shortest path
- **dynamic_programming**: DP, memoization, tabulation
- **greedy**: Greedy algorithms, interval problems

### data_structures/

Use this for foundational implementations:

- Data structure implementations (Node, LinkedList, etc.)
- Core operations and utilities
- Educational/reference code

## Workflow for Creating Solution Files

1. **Identify Problem Details**
   - LeetCode number
   - Problem name
   - Difficulty
   - Main technique/pattern

2. **Determine Category**
   - Primary algorithm pattern
   - Place in appropriate algorithm_patterns folder

3. **Create File**
   - Use naming format: `LC###_ProblemName.py`
   - Apply template structure

4. **Write Solution**
   - Add header documentation
   - Implement solution with comments
   - Include test cases

5. **Verify**
   - Run test cases
   - Check output matches expected results
   - Ensure code follows style guidelines

## Example Categories for Common Problems

- Two Sum (1) → `arrays_and_hashing/`
- Add Two Numbers (2) → `linked_list/`
- Longest Substring (3) → `sliding_window/`
- Container With Most Water (11) → `two_pointers/`
- Valid Parentheses (20) → `stack/`
- Merge K Sorted Lists (23) → `heap_priority_queue/`
- Binary Search (704) → `binary_search/`
- Permutations (46) → `backtracking/`
- Climbing Stairs (70) → `dynamic_programming/`
- Number of Islands (200) → `graphs/`
- Find Duplicate (287) → `arrays_and_hashing/` (uses cycle detection but classified as array)

## Response Format

When user provides a problem/code, respond with:

1. Confirm category placement
2. Create file with full template
3. Mention file location
4. Note any special categorization considerations

## Quality Checklist

Before finalizing a file, ensure:

- [ ] Correct naming format
- [ ] Complete header documentation
- [ ] Type hints present
- [ ] Code is well-commented
- [ ] Test cases included
- [ ] Big O analysis provided
- [ ] File placed in correct category
- [ ] Code follows PEP 8 (except camelCase methods for LeetCode compatibility)

## Quality Checklist

Before finalizing a file, ensure:

- [ ] Correct naming format
- [ ] Complete header documentation
- [ ] Type hints present
- [ ] Code is well-commented
- [ ] Test cases included
- [ ] Big O analysis provided
- [ ] File placed in correct category
- [ ] Code follows PEP 8 (except camelCase methods for LeetCode compatibility)
- [ ] Code follows PEP 8 (except camelCase methods for LeetCode compatibility)
