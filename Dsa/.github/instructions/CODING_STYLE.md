# Python Coding Style Guide

## Core Principles

### 1. Python 3 Modern Style

- **Minimum Version**: Python 3.12+
- Use latest Python 3.12+ features
- Type hints for all function signatures
- f-strings for string formatting
- Modern syntax and idioms
- **Variable naming**: camelCase for local variables (e.g., `leftHeight`, `rightHeight`)

### 2. No Nested Functions

**Rule**: Never define functions inside other functions. Use class methods instead.

#### ❌ DON'T DO THIS:

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node):  # ❌ Nested function - AVOID
            if not node:
                return 0
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            self.diameter = max(self.diameter, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)

        height(root)
        return self.diameter
```

#### ✅ DO THIS INSTEAD:

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.height(root)
        return self.diameter

    def height(self, node: Optional[TreeNode]) -> int:  # ✅ Class method
        if not node:
            return 0
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        self.diameter = max(self.diameter, leftHeight + rightHeight)
        return 1 + max(leftHeight, rightHeight)
```

### 3. Naming Conventions

**Variable Names**: Use **camelCase** for local variables

```python
# ✅ Correct
leftHeight = self.height(node.left)
rightHeight = self.height(node.right)
maxValue = max(leftHeight, rightHeight)

# ❌ Incorrect
left_height = self.height(node.left)  # Don't use snake_case
right_height = self.height(node.right)
```

**Method Names**: Use **camelCase** (LeetCode style)

```python
def maxDepth(self, root):  # ✅ Correct
def max_depth(self, root):  # ❌ Incorrect
```

**Class Names**: Use **PascalCase**

```python
class TreeNode:  # ✅ Correct
class ListNode:  # ✅ Correct
```

### 4. Organization

- All files go in `data_structures/` folder
- Organize by primary data structure (tree, linked_list, arrays_and_hashing, etc.)
- Use format: `LC###_ProblemName.py`

### 5. Type Hints

Always include type hints:

```python
from typing import Optional, List, Dict, Set

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def method(self, param1: List[int], param2: str) -> Optional[TreeNode]:
        pass
```

### 6. Documentation

- Clear docstrings for all methods
- Include Args and Returns sections
- Comment complex logic

### 7. File Structure

1. Module docstring (problem description, complexity)
2. Imports
3. Helper classes (TreeNode, ListNode, etc.)
4. Solution class
5. Test cases in `if __name__ == "__main__":` block

## Quick Checklist

- [ ] Python 3.12+ syntax and features
- [ ] Type hints on all functions
- [ ] No nested functions (use class methods)
- [ ] camelCase for variable names (leftHeight not left_height)
- [ ] Comments for complex logic
- [ ] File in correct data_structures folder
- [ ] Test cases includedble names (leftHeight not left_height)
- [ ] Comments for complex logic
- [ ] File in correct data_structures folder
- [ ] Test cases included
