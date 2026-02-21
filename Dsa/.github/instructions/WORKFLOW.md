# DSA Solution Creation Workflow

## Quick Start Workflow

### Step 1: Receive Problem

```
INPUT: User provides LeetCode problem (code, number, or description)
```

### Step 2: Extract Information

- [ ] LeetCode problem number
- [ ] Problem title/name
- [ ] Difficulty level (Easy/Medium/Hard)
- [ ] Problem description (brief)
- [ ] Main algorithm/technique used

### Step 3: Determine Category

**Primary Pattern Decision Tree:**

```
Does it use hash map/set for O(1) lookup?
└─ Yes → arrays_and_hashing/

Does it use two pointers technique?
└─ Yes → two_pointers/

Does it use sliding window?
└─ Yes → sliding_window/

Does it use stack/deque for LIFO operations?
└─ Yes → stack/

Does it involve binary search/divide-conquer?
└─ Yes → binary_search/

Does it manipulate linked list nodes?
└─ Yes → linked_list/

Does it involve tree traversal/operations?
└─ Yes → trees/

Does it use heap/priority queue?
└─ Yes → heap_priority_queue/

Does it use backtracking/recursion with state?
└─ Yes → backtracking/

Does it involve graph traversal (BFS/DFS)?
└─ Yes → graphs/

Does it use dynamic programming/memoization?
└─ Yes → dynamic_programming/

Does it use greedy approach?
└─ Yes → greedy/
```

### Step 4: Generate File Name

**Format**: `LC{number}_{PascalCaseName}.py`

**Examples:**

- Problem: "Two Sum" (#1) → `LC001_TwoSum.py`
- Problem: "Find Duplicate Number" (#287) → `LC287_FindDuplicate.py`
- Problem: "Longest Substring Without Repeating Characters" (#3) → `LC003_LongestSubstring.py`

**Rules:**

- Pad number with zeros to 3 digits
- Use PascalCase for problem name
- Shorten long names (keep under 4 words)
- Remove common words: "the", "a", "an"

### Step 5: Create File Using Template

1. Load `SOLUTION_TEMPLATE.py`
2. Fill in placeholders:
   - `{PROBLEM_NUMBER}`
   - `{PROBLEM_TITLE}`
   - `{DIFFICULTY}`
   - `{PROBLEM_LINK}`
   - `{PROBLEM_DESCRIPTION}`
   - `{ALGORITHM_NAME}`
   - `{TIME_COMPLEXITY}`
   - `{SPACE_COMPLEXITY}`
   - `{METHOD_NAME}`
   - `{IMPLEMENTATION}`
   - `{TEST_CASES}`

3. Save to appropriate folder

### Step 6: Verify and Respond

- [ ] File created in correct location
- [ ] All template fields filled
- [ ] Code syntax is valid
- [ ] Test cases are relevant
- [ ] Inform user of file location

---

## Detailed Workflow with Examples

### Example 1: Two Sum Problem

**Input:**

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []
```

**Process:**

1. **Extract**: LeetCode #1, "Two Sum", Easy
2. **Category**: Hash map → `arrays_and_hashing/`
3. **Filename**: `LC001_TwoSum.py`
4. **Algorithm**: Hash Map
5. **Complexity**: O(n) time, O(n) space
6. **Generate**: Use template
7. **Save**: `Dsa/algorithm_patterns/arrays_and_hashing/LC001_TwoSum.py`

### Example 2: Find Duplicate Number

**Input:**

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
```

**Process:**

1. **Extract**: LeetCode #287, "Find the Duplicate Number", Medium
2. **Category**: Uses cycle detection but classified as `arrays_and_hashing/`
3. **Filename**: `LC287_FindDuplicate.py`
4. **Algorithm**: Floyd's Cycle Detection
5. **Complexity**: O(n) time, O(1) space
6. **Generate**: Use template with cycle detection notes
7. **Save**: `Dsa/algorithm_patterns/arrays_and_hashing/LC287_FindDuplicate.py`

---

## Handling Edge Cases

### When Problem Fits Multiple Categories

**Rule**: Choose the PRIMARY technique used

Example: "Find Duplicate Number"

- Uses cycle detection (linked_list technique)
- But operates on array (arrays category)
- **Decision**: Place in `arrays_and_hashing/` (matches LeetCode categorization)
- **Note**: Add comment explaining the technique

### When Problem Number is Missing

- Ask user for problem number
- Or use descriptive name: `FindDuplicate.py`
- **Recommended**: Always include LC number for consistency

### When Problem is Original (not from LeetCode)

- Use format: `Custom_{ProblemName}.py`
- Or: `Practice_{ProblemName}.py`

### When User Requests Data Structure Implementation

- Place in `data_structures/` folder
- Example: LinkedList implementation → `data_structures/linked_list/LinkedList.py`

---

## Response Templates

### Standard Response

```
Created file: LC{number}_{Name}.py in algorithm_patterns/{category}/

File includes:
✓ Complete header documentation
✓ Type hints
✓ Solution implementation
✓ Test cases with expected outputs
✓ Time/Space complexity analysis
```

### With Special Note

```
Created file: LC{number}_{Name}.py

Note: While this problem uses {technique_A}, it's categorized under
{category_B} following LeetCode's classification system.
```

### When Clarification Needed

```
I need more information to create the file:
- LeetCode problem number?
- Difficulty level?
- Any specific test cases you want included?
```

---

## Automation Checklist

For each problem submission:

- [x] Identify problem number and title
- [x] Determine difficulty
- [x] Analyze algorithm/pattern
- [x] Choose correct category
- [x] Generate proper filename
- [x] Fill template with all details
- [x] Add meaningful test cases
- [x] Calculate time/space complexity
- [x] Create file in correct location
- [x] Confirm with user

---

## Common Patterns Quick Reference

| Pattern              | Key Indicators              | Example Problems             |
| -------------------- | --------------------------- | ---------------------------- |
| **Arrays & Hashing** | Hash map, set, frequency    | Two Sum, Group Anagrams      |
| **Two Pointers**     | Left/right, slow/fast       | Valid Palindrome, 3Sum       |
| **Sliding Window**   | Window of elements          | Longest Substring            |
| **Stack**            | LIFO, nested structures     | Valid Parentheses            |
| **Binary Search**    | Sorted array, O(log n)      | Binary Search                |
| **Linked List**      | Node manipulation           | Reverse List, Merge Lists    |
| **Trees**            | Tree traversal              | Inorder, Level Order         |
| **Heap**             | Top K, priority             | Kth Largest Element          |
| **Backtracking**     | All solutions, permutations | Permutations, N-Queens       |
| **Graphs**           | BFS, DFS, connected         | Number of Islands            |
| **DP**               | Overlapping subproblems     | Climbing Stairs, Coin Change |
| **Greedy**           | Local optimal               | Jump Game                    |

- [x] Create file in correct location
- [x] Confirm with user

---

## Common Patterns Quick Reference

| Pattern              | Key Indicators              | Example Problems             |
| -------------------- | --------------------------- | ---------------------------- |
| **Arrays & Hashing** | Hash map, set, frequency    | Two Sum, Group Anagrams      |
| **Two Pointers**     | Left/right, slow/fast       | Valid Palindrome, 3Sum       |
| **Sliding Window**   | Window of elements          | Longest Substring            |
| **Stack**            | LIFO, nested structures     | Valid Parentheses            |
| **Binary Search**    | Sorted array, O(log n)      | Binary Search                |
| **Linked List**      | Node manipulation           | Reverse List, Merge Lists    |
| **Trees**            | Tree traversal              | Inorder, Level Order         |
| **Heap**             | Top K, priority             | Kth Largest Element          |
| **Backtracking**     | All solutions, permutations | Permutations, N-Queens       |
| **Graphs**           | BFS, DFS, connected         | Number of Islands            |
| **DP**               | Overlapping subproblems     | Climbing Stairs, Coin Change |
| **Greedy**           | Local optimal               | Jump Game                    |
