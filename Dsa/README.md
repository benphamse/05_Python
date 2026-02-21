# DSA Practice Repository

A well-organized collection of Data Structures & Algorithms solutions with AI agent automation support.

## 📁 Project Structure

```
Dsa/
├── algorithm_patterns/           # Solutions organized by solving technique
│   ├── arrays_and_hashing/      # Hash maps, sets, frequency
│   ├── two_pointers/            # Left/right, slow/fast pointers
│   ├── sliding_window/          # Fixed/variable window problems
│   ├── stack/                   # Stack-based solutions
│   ├── binary_search/           # Binary search, divide & conquer
│   ├── linked_list/             # Linked list manipulation
│   ├── trees/                   # Tree traversal & operations
│   ├── heap_priority_queue/     # Heap operations
│   ├── backtracking/            # Backtracking & recursion
│   ├── graphs/                  # Graph algorithms (BFS/DFS)
│   ├── dynamic_programming/     # DP & memoization
│   └── greedy/                  # Greedy algorithms
│
├── data_structures/             # Data structure implementations
│   ├── array/
│   ├── linked_list/
│   ├── stack/
│   ├── queue/
│   ├── hash_table/
│   ├── tree/
│   ├── graph/
│   ├── heap/
│   ├── string/
│   └── matrix/
│
├── .github/
│   └── instructions/            # AI agent instructions & templates
│       ├── AI_PROMPT.md         # Quick AI agent setup
│       ├── AI_AGENT_INSTRUCTIONS.md  # Detailed guidelines
│       ├── WORKFLOW.md          # Step-by-step process
│       ├── EXAMPLES.md          # Filled template examples
│       └── SOLUTION_TEMPLATE.py # Base template
│
└── README.md                    # This file
```

## 🎯 Design Philosophy

### Why Two Organization Systems?

1. **`algorithm_patterns/`** (Primary)
   - Organized by solving technique/pattern
   - Follows LeetCode/NeetCode roadmap style
   - Helps recognize problem patterns
   - Better for interview preparation

2. **`data_structures/`** (Reference)
   - Organized by data structure type
   - Good for implementations
   - Educational reference

### Naming Conventions

**Folders**: `snake_case`

- Examples: `two_pointers`, `dynamic_programming`
- Rationale: Python PEP 8 convention, readable

**Files**: `LC###_PascalCase.py`

- Examples: `LC001_TwoSum.py`, `LC287_FindDuplicate.py`
- Rationale:
  - Easy to search problem number
  - Auto-sort by number
  - Professional appearance
  - Track progress

**Code**: LeetCode-compatible

- Classes: `Solution`
- Methods: `camelCase` (e.g., `twoSum`, `isPalindrome`)
- Rationale: Cross-language consistency with LeetCode

## 🚀 Quick Start

### Manual Usage

1. Create a new solution file:

   ```bash
   touch algorithm_patterns/arrays_and_hashing/LC001_TwoSum.py
   ```

2. Copy from `.github/instructions/SOLUTION_TEMPLATE.py` and fill in:
   - Problem details
   - Implementation
   - Test cases

### AI Agent Usage

**Option 1: Quick Setup**

```
Copy the prompt from .github/instructions/AI_PROMPT.md and paste to your AI agent.
Then provide problem code or number.
```

**Option 2: Detailed Setup**

```
Read .github/instructions/AI_AGENT_INSTRUCTIONS.md and .github/instructions/WORKFLOW.md for full configuration.
```

**Example Interaction**:

```
You: [Paste LeetCode solution code]

AI: Created: algorithm_patterns/arrays_and_hashing/LC287_FindDuplicate.py
    ✓ Complete documentation
    ✓ Test cases included
    ✓ Time/Space complexity: O(n)/O(1)
```

## 📋 File Template Structure

Every solution file includes:

```python
"""
Problem information (number, title, difficulty, link)
Problem description
Algorithm & complexity analysis
"""

from typing import List

class Solution:
    def methodName(self, params) -> returnType:
        """Docstring with description"""
        # Implementation
        pass

# Test cases
if __name__ == "__main__":
    # 3+ test cases with expected outputs
```

## 📊 Category Quick Reference

| Category                | Key Indicators             | Example Problems        |
| ----------------------- | -------------------------- | ----------------------- |
| **Arrays & Hashing**    | Hash map, set, O(1) lookup | Two Sum, Group Anagrams |
| **Two Pointers**        | Left/right or slow/fast    | Valid Palindrome, 3Sum  |
| **Sliding Window**      | Contiguous subarray        | Longest Substring       |
| **Stack**               | LIFO, nested structures    | Valid Parentheses       |
| **Binary Search**       | Sorted, O(log n)           | Binary Search           |
| **Linked List**         | Node manipulation          | Reverse List            |
| **Trees**               | Tree traversal             | Inorder Traversal       |
| **Heap**                | Top K, priority            | Kth Largest             |
| **Backtracking**        | All solutions              | Permutations            |
| **Graphs**              | BFS/DFS                    | Number of Islands       |
| **Dynamic Programming** | Overlapping subproblems    | Coin Change             |
| **Greedy**              | Local optimal              | Jump Game               |

## 🤖 AI Agent Features

The included AI configuration enables:

- ✅ Automatic problem categorization
- ✅ Consistent file naming
- ✅ Complete documentation generation
- ✅ Test case creation
- ✅ Complexity analysis
- ✅ Code style compliance

## 📚 AI Agent Instructions

All AI agent documentation is in [.github/instructions/](.github/instructions/):

1. **[`.github/instructions/AI_PROMPT.md`](.github/instructions/AI_PROMPT.md)**
   - Quick copy-paste prompt for AI agents
   - Essential rules and format
   - 5-minute setup

2. **[`.github/instructions/AI_AGENT_INSTRUCTIONS.md`](.github/instructions/AI_AGENT_INSTRUCTIONS.md)**
   - Comprehensive guidelines
   - Naming conventions explained
   - Quality checklist

3. **[`.github/instructions/WORKFLOW.md`](.github/instructions/WORKFLOW.md)**
   - Step-by-step process
   - Decision trees
   - Edge case handling

4. **[`.github/instructions/EXAMPLES.md`](.github/instructions/EXAMPLES.md)**
   - Filled template examples
   - Multiple difficulty levels
   - Placeholder reference

5. **[`.github/instructions/SOLUTION_TEMPLATE.py`](.github/instructions/SOLUTION_TEMPLATE.py)**
   - Base template file
   - Copy and customize

## 🎓 Best Practices

### When Solving Problems

1. **Understand**: Read problem, identify pattern
2. **Plan**: Choose algorithm, analyze complexity
3. **Code**: Implement with clear variable names
4. **Test**: Run multiple test cases
5. **Document**: Add comments, docstrings
6. **Optimize**: Review for improvements

### File Organization

- Place files in PRIMARY category only (avoid duplicates)
- Use descriptive but concise file names
- Include problem number for easy reference
- Add meaningful test cases (edge cases!)

### Code Quality

- Follow PEP 8 (except camelCase for LeetCode methods)
- Use type hints
- Write clear comments
- Include Big O analysis
- Test edge cases

## 🔧 Customization

### For Different Platforms

**HackerRank**: Use `HR###_ProblemName.py`
**CodeForces**: Use `CF###_ProblemName.py`
**Custom**: Use `Custom_ProblemName.py`

### Adding New Categories

To add a new algorithm pattern:

1. Create folder in `algorithm_patterns/`
2. Use `snake_case` naming
3. Update category list in documentation

## 📈 Progress Tracking

### By Pattern

Count files in each `algorithm_patterns/` subfolder to see progress.

### By Difficulty

Add difficulty tags to track Easy/Medium/Hard completion.

### Example Tracker Script

```python
# count_solutions.py
import os
from pathlib import Path

patterns_dir = Path("algorithm_patterns")
for category in sorted(patterns_dir.iterdir()):
    if category.is_dir():
        count = len(list(category.glob("*.py")))
        print(f"{category.name}: {count} problems")
```

## 🤝 Contributing

When adding solutions:

1. Follow naming conventions
2. Use template structure
3. Include test cases
4. Add documentation
5. Verify category placement

## 📝 Notes

- **Hybrid Approach**: Uses snake_case folders (Python convention) with PascalCase files (professional look)
- **LeetCode Compatible**: Method signatures match LeetCode exactly
- **AI-Friendly**: Structured for automation while maintaining readability
- **Interview Ready**: Organized by patterns employers ask about

## 🔗 Resources

- [LeetCode](https://leetcode.com/)
- [NeetCode](https://neetcode.io/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

## ⚖️ License

Free to use for personal learning and practice.

---

**Last Updated**: 2026-02-21
**Version**: 1.0.0
**Maintainer**: AI Agent + Human Collaboration

- [PEP 8 Style Guide](https://pep8.org/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

## ⚖️ License

Free to use for personal learning and practice.

---

**Last Updated**: 2026-02-21
**Version**: 1.0.0
**Maintainer**: AI Agent + Human Collaboration
**Maintainer**: AI Agent + Human Collaboration
