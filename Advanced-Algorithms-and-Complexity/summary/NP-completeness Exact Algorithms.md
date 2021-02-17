**NP-completeness: Exact Algorithms**

**3-Satisfiability (3-SAT)**

Input: A set of clauses, each containing at most three literals.

Output: Find a satisfying assignment

**Backtracking**

Construct a solution piece by piece. Backtrack if the current partial solution cannot be extended to a valid solution. Try to guess the Boolean value of variable, and reduce the clauses into simpler form. If the reduced clauses under a guess is empty, go back to previous guess and pick another solution.

```
SolveSAT(F):
if F has no clauses:
	return "sat"
if F contains an empty clause:
	return "unsat"
x <- unassigned variable of F
if SolveSAT(F[x <- 0]) = "sat": 
	return "sat"
if SolveSAT(F[x <- 1]) = "sat":
	return "sat"
return "unsat"
```

**Local Search**

Start with a candidate solution, and iteratively move from the current candidate to its neighbor trying to improve the candidate. Let $F$ be a 3-CNF formula over variables $x_1, x_2,..., x_n$. A candidate solution is a truth assignment to these variables, that is, a vector from $\{0, 1\}^n$.

**Hamming distance**

Hamming distance (or just distance) between two assignments $\alpha, \beta \in \{0, 1\}^n$ is the number of bits where they differ: $dist(\alpha, \beta) = |\{i: \alpha_i \ne \beta_i\}|$.

**Hamming ball**

Hamming ball with center $\alpha \in \{0, 1\}^n$ and radius $r$, denoted by $\mathcal{H}(\alpha, r)$, is the set of all truth assignments from $\{0, 1\}^n$ at distance at most $r$  from $\alpha$.

**Example of Hamming ball**

$$\mathcal{H}(1011, 0) = \{1011\}$$

$\mathcal{H}(1011, 1)=\{1011, 0011, 1111, 1001, 1010\}$

$\mathcal{H}(1011, 1)=\{1011, 0011, 1111, 1001, 1010, 0111, 0001, 0010, 1101, 1110, 1000\}$

**Lemma**

Assume that $\mathcal{H}(\alpha, r)$ contains a satisfying assignment $\beta$ for $F$. We can then find a (possibly different) satisfying assignment in time $O(|F|\cdot 3^r)$.

Proof:

If $\alpha$ satisfies $F$, return $\alpha$. Otherwise, take an unsatisfied clause e.g. ($x_i \or \bar{x}_j \or x_k$). Let $\alpha$ assigns $x_i = 0, x_j = 1, x_k = 0$. Let $\alpha^i, \alpha^j, \alpha^k$ be assignments resulting from $\alpha$ by flipping the i-th, j-th, k-th bit, respectively. Crucial observation: at least one of them is closer to $\beta$ than $\alpha$. Hence, there are at most $3^r$ recursive calls.

```
CheckBall(F, alpha, r):
if alpha satisfies F:
	return alpha
if r = 0:
	return "not found"
x_i, x_j, x_k <- variables of unsatisfied clause
alpha_i, alpha_j, alpha_k <- alpha with bits i, j, k flipped
CheckBall(F, alpha_i, r - 1)
CheckBall(F, alpha_j, r - 1)
CheckBall(F, alpha_k, r - 1)
if a satisfying assignment is found:
	return it
else:
	return "not found"
```

Assume that $F$ has a satisfying assignment $\beta$. If it has more 1's than 0's then it has distance at most $\frac{n}{2}$ from all-1's assignment. Otherwise, it has distance at most $\frac{n}{2}$ from all-0's assignment. Thus, it suffices to make two calls: `CheckBall(F, 11...1, n/2)` and `CheckBall(F, 00...0, n/2)`.

Running time analysis: $O(|F|\cdot3^{\frac{n}{2}}) \approx O(|F|\cdot 1.733^n)$. It is still exponential but faster than brute force search which requires traversing through all $2^n$ assignments.

**Traveling salesman problem (TSP)**

Input: A complete graph with weights on edges and a budget $b$.

Output: A cycle that visits each vertex exactly once and has total weight at most $b$.

**Brute force solution:** Suppose we have $n$ vertices, we can search for $(n-1)!$  different arrangements and compute the total weight to pick the smallest.

**Dynamic programming**

For a subset of vertices $S \subset \{1,2,...,n\}$ containing the vertex 1 and a vertex $i \in S$, let $C(S, i)$ be the length of the shortest path that starts at 1, ends at $i$ and visits all vertices from $S$ exactly once.

$C(\{1\}, 1) = 0$ and $C(S, 1)=\infin$ when $|S|>1$.  It is because a path starts at 1 must also end at 1, and a path start at $S$ cannot be end at 1 unless $S$ only contains 1. 

Consider the second-to-last vertex $j$ on the required shortest path from 1 to $i$ visiting all vertices from $S$. The subpath from 1 to $j$ is the shortest one visiting all vertices from $S-\{i\}$ exactly once. Otherwise, it exists another subpath that is the shortest, and the current path from 1 to $i$ is not the shortest. Hence, $C(S, i)=min_{j\in S, j\ne i}\{C(S-\{i\}, j) + d_{ji}\}$ .

```
TSP(G):
C({1}, 1) <- 0
for s from 2 to n:
	for all L in S as a subset of {1, 2, ..., n} of size s:
		C(S, L) <- inf
		for all i in S, i != L:
			for all j in S, j != i:
				C(S, i) <- min{C(S, i), C(S - {i}, j) + d[j][i]}
return min_i {C({1, ..., n}, i) + d[i][1]}
```

**Implementation remark:** How to iterate through all subsets of $\{1, ..., n\}$? There is a natural one-to-one correspondence between integers in the range from $0$ and $2^n-1$ and subsets of $\{0,...,n-1\}$:$k\leftrightarrow\{i:\text{i-th bit of } k \text{ is } 1\}$. 

**Example:**

| $k$  | $\text{bin(}k\text{)}$ | $\{i:\text{i-th bit of } k \text{ is } 1\}$ |
| ---- | ---------------------- | ------------------------------------------- |
| 0    | 000                    | $\{\empty\}$                                |
| 1    | 001                    | $\{0\}$                                     |
| 2    | 010                    | $\{1\}$                                     |
| 3    | 011                    | $\{0, 1\}$                                  |
| 4    | 100                    | $\{2\}$                                     |
| 5    | 101                    | $\{0, 2\}$                                  |
| 6    | 110                    | $\{1, 2\}$                                  |
| 7    | 111                    | $\{0, 1, 2\}$                               |

To find an integer $k$ for $S-\{j\}$:

```
k^(1 << j)
```

**Branch-and-bound:**

It can be viewed as a generalization of backtracking for optimization problems.

**Branching:**

1. Grow a tree of partial solutions.
2. At each node of the recursion tree, check whether the current partial solution can be extended to a solution which is better than the best solution found so far.
3. If not, don't continue this branch.

**Bound:**

1. Initialize the best solution before growing the tree using heuristics. (Bound the worst solution).
2. The length of an optimal TSP cycle is at least $1/2\sum_{v\in V}(\text{two min length edges adjacent to } v)$, the length of a minimum spanning tree.