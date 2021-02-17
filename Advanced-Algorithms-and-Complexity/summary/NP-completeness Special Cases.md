**NP-completeness: Special Cases**

**Remark:** NP-complete problem does not exclude an efficient algorithm for special cases of the problem.

**2-Satisfiability (2-SAT)**

Input: A set of clauses, each containing at most two literals.

Output: Find a satisfying assignment

Consider a clause $(l_1 \or l_2)$. For 2-SAT problem, we cannot have both $l_1=0$ and $l_2 = 0$. In other words, if $l_1 = 0$, then $l_2 = 1$ and if $l_2 = 0$ then $l_1=1$.

**Implication**

Implication is a binary logical operation denoted by $\Rightarrow$ and defined by the following truth table:

| $x$  | $y$  | $x\Rightarrow y$ |
| ---- | ---- | ---------------- |
| 0    | 0    | 1                |
| 0    | 1    | 1                |
| 1    | 0    | 0                |
| 1    | 1    | 1                |

**Implication graph**

For a 2-CNF formula, its implication graph is constructed as follows:

1. For each variable $x$, introduce two vertices labeled by $x$ and $\bar{x}$.
2. For each 2-clause $(l_1 \or l_2)$, introduce two directed edges $\bar{l}_1 \rightarrow l_2$ and $\bar{l}_2 \rightarrow l_1$.
3. For each 1-clause $(l)$, introduce an edge $\bar{l} \rightarrow l$.

We need to assign Boolean values to all variables such that all implication holds in the graph i.e. there is no edge from 1 to 0.

**Skew-symmetric**

The graph is skew-symmetric: if there is an edge $l_1 \rightarrow l_2$, then there is an edge $\bar{l}_2 \rightarrow \bar{l}_1$.  To generalize this property to paths: if there is a path from $l_1$ to $l_2$, then there is a path from $\bar{l}_2$ to $\bar{l}_1$.

**Lemma (Transitivity)**

If all the edges are satisfied by an assignment and there is a path from $l_1$ to $l_2$, then it cannot be the case that $l_1=1$ and $l_2 = 0$. 

Proof: Based on implication graph, if $l_1=1$, then there is an edge connected from $l_1$ to another literal $l_k$. The relationship is an implication. So, $l_k =1$; otherwise, there will be a contradiction. Thus, it is impossible to have $l_2 = 0$.

**Strongly Connected Components (SCCs)**

1. All variables lying in the same SCC of the implication graph should be assigned the same value.
2. In particular, if a SCC contains a variable together with its negation, then the formula is unsatisfiable. (SCC: every vertex is reachable (there exists a path/a walk) from every other vertex. If it contains a variable together with its negation, a contradiction will be reached.)
3. It turns out that otherwise the formula is satisfiable.

```
# 2SAT(2-CNF F) algorithm
# Running time: O(|F|)
# Aspvall, Plass & Tarjan (1979)

construct the implication graph G
find SCC's of G
for all variables x:
	if x and the negation of x, denoted by ~x, lie in the same SCC of G:
		return "unsatisfiable"
find a topological ordering of SCC's
for all SCC's C in reverse order:
	if literals of C are not assigned yet:
		set all of them to 1
		set their negations to 0
return the satisfying assignment 
```

**Lemma: The algorithm 2SAT is correct.**

Proof: When a literal is set to 1, all the literals that are reachable from it have already been set to 1 (since we process SCC's in reverse topological order). When a literal is set to 0, all the literals it is reachable from have already been set to 0 (by skew-symmetry).

**Maximum independent set in a tree**

Input: A tree, T.

Output: An independent set (i.e. a subset of vertices no two of which are adjacent) of maximum size.

```
# Running time: O(|T|) because there is at most |T| nodes for removal
function PartyGreedy(T):
while T is not empty:
	take all the leaves to the solution
	remove them and their parents from T
return the constructed solution
```

**Maximum weighted independent set in trees**

Input: A tree, T, with weights on vertices.

Output: An independent set (i.e. a subset of vertices no two of which are adjacent) of maximum total weight.

**Subproblem**

Let $D(v)$ be the maximum weight of an independent set in a subtree rooted at node $v$. To construct independent set with maximum weights from this subtree, we can either take:

1. The node $v$ and the grandchildren of $v$.

2. The children of $v$.

So, we have the following recurrence relation: 
$$
D(v) = max\{w(v) + \sum_{\text{grandchildren } w \text{ of } v} D(w), \sum_{\text{children } w \text{ of } v}D(w)\}
$$



```
function FunParty(v):
if D(v) = inf:
	if v has no children:
		D(v) <- w(v)
	else:
		m1 <- w(v)
		for all children u of v:
			for all children w of u:
				m1 <- m1 + FunParty(w)
		m0 <- 0
		for all children u of v:
			m0 <- m0 + FunParty(u)
	D(v) <- max(m1, m0)
return D(v)
```

