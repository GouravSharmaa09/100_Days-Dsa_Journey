# **🚀 100 Days of DSA Mastery (Python)**

Welcome to my DSA repository! I am documenting my daily progress, logic building, and problem-solving journey. Currently, I have mastered **Bit Manipulation** and am deep-diving into **Advanced Recursion & Backtracking**.

## **📈 Progress Overview**
- **Current Status:** Day 37 / 100 
- **Current Topic:** Advanced Recursion & Combinations 🔄
- **Language:** Python 🐍
- **Goal:** Crack top-tier product companies by mastering problem-solving patterns.

---

## **📅 Recent Milestones**

### **🔄 Day 36 - 37: Combination & Subset Mastery**
- **Day 37: Subset Sum I & Combination Sum II**
    - **Subset Sum I:** Optimized recursion by passing `total` as an accumulator instead of building subset lists ($O(2^N)$).
    - **Combination Sum II (LC #40):** Mastered **Duplicate Pruning** using `Sort + Loop-based recursion` and the `if i > index and nums[i] == nums[i-1]` skip logic.
- **Day 36: Combination Sum I & Parentheses Generation**
    - **Combination Sum I (LC #39):** Implemented **Infinite Supply** logic where the same index can be picked multiple times.
    - **Generate Parentheses (LC #22):** Mastered **Pruned Backtracking** using Open/Close bracket counts to ensure only valid strings are generated.

### **🔄 Day 32 - 35: Recursion Patterns (The Brain-Bender)**
- **Day 35:** Mastered **Recursion Return Types**: 
    - **Counting Subsequences** (Return `1` or `0` logic).
    - **Boolean Recursion** (Exist or Not - Short-circuiting technique).
    - **Constraint Generation**: Binary strings with no consecutive 1s.
- **Day 34:** Deep dive into **Subsets & Subsequences** (LC #78 & #90). Mastered **Pick and Non-Pick** strategy.

### **⚡ Day 30 - 31: Bit Manipulation Mastery**
- **Optimal Patterns:** Solved **Minimum Bit Flips** and **Power of 2** check using the $O(1)$ trick: `n & (n-1) == 0`.
- **Set Bit Magic:** Implemented **Brian Kernighan’s Algorithm**.

### **🔗 Day 26 - 29: Singly Linked List (The Core)**
- **Day 29:** Mastered **Odd-Even Indexing** (LC #328) and **Remove Nth Node From End** (LC #19).
- **Day 28:** **Cycle Detection** & Starting Point of Loop (LC #141 & #142).

---

## **🧩 Problem Solving Patterns Mastered**
- [x] **Pick & Non-Pick:** Fundamental strategy for subsequences and power sets.
- [x] **Infinite Supply Pattern:** Handling unlimited use of elements in combinations.
- [x] **Duplicate Pruning:** Using sorting and index comparison to avoid redundant recursive branches.
- [x] **Short-circuiting Recursion:** Using `True/False` or early `return` to optimize search.
- [x] **Accumulator Pattern:** Passing running totals as parameters to save space.

---

## **📂 Repository Structure**
- `Linked_List/` : Singly Linked List operations and LeetCode challenges.
- `Bit_Manipulation/` : Basic and Advanced bitwise tricks.
- `Recursion/` : Subsets, Combinations, Target Sums, and Backtracking.

---
*“Consistency is the key. Day 37 done, 63 more to go. The logic is getting sharper every day!”* 🚀