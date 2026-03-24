## 🚀 Day 54 & 55: The Binary Tree Mastery (Post-Break Comeback)

After a short 13-day hiatus, I've returned with a focus on **Tree Data Structures** and **Advanced Greedy Algorithms**.

### 🌳 Binary Tree Milestones (DFS & BFS)
| Problem | Logic / Strategy | Complexity | Status |
| :--- | :--- | :--- | :--- |
| **Max Height** | Recursive DFS & Iterative BFS (Queue) | $O(N)$ | ✅ Solved |
| **Diameter** | $LH + RH$ at every node (Optimized) | $O(N)$ | ✅ Solved |
| **Balanced Tree** | Return -1 if $|LH - RH| > 1$ | $O(N)$ | ✅ Solved |
| **Max Path Sum** | `node.val + max(0, LH) + max(0, RH)` | $O(N)$ | 🔥 Hard Solved |

### 💡 Key Technical Learnings
- **The -1 Trick:** In "Balanced Tree," instead of calling height repeatedly $O(N^2)$, we return -1 as soon as an imbalance is found, making it $O(N)$.
- **Negative Pruning:** In "Max Path Sum," we use `max(0, left_sum)` to ignore paths that decrease the overall sum.
- **BFS Height:** Using `level_size = len(queue)` to count levels instead of nodes.

### 🎯 Greedy Wins (Day 52-53 Recap)
- **N-Meetings in a Room:** Sorting by `End Time` is the key.
- **Minimum Platforms:** Parallel sorting of Arrival and Departure times.
- **Jump Game I & II:** Greedy 'Max Reachable' index approach.

---
*"Consistency is not about never failing, but about always getting back up."* ```

---

### 🧠 Quick Concept Recap (Visualizing your work)





### 🏆 Next Step (Day 56)
Bhai, tune "Hard" problem toh phod diya hai, ab thoda "Structure" check karne wale sawal karte hain jo interviews mein bohot aate hain:
* **Symmetric Tree (LeetCode 101):** Mirror image check karna.
* **Identical Trees (LeetCode 100):** Kya do trees bilkul judwa hain?

**Kya bolti public? Kal Day 56 pe "Tree Comparisons" shuru karein?** 🚀🔥✨