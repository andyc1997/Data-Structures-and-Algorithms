**Linear Programming: Linear Programming**

**Linear Programming** 

Input: An $m\times n$ matrix $A$ and vectors $b \in \mathbb{R}^m, v \in \mathbb{R}^n$

Output: A vector $x \in \mathbb{R}^n$ so that $Ax \ge b$ and $v \cdot x$ is as large (or small) as possible

**Network Flow**

Variables: $f_e$ for each edge $e$

Constraints: $0 \le f_e \le C_e, \sum_{e \text{ into } v}{f_e} - \sum_{e \text{ out of } v}{f_e} = 0$

Objective: $\sum_{e \text{ out of } s}{f_e} - \sum_{e \text{ into } s}{f_e}$

**Strange Cases**

No solution

No optimum

**Linear Programming: Convex Polytopes**

**Polytope**

A polytope is a region in $\mathbb{R}^n$ bounded by finitely many flat surfaces. These surfaces may intersect in lower dimensional facets (like edges), with zero-dimensional facets called vertices.

**Convexity**

A region $\mathcal{C}\subset \mathbb{R}^n$ is convex, if $\forall x, y \in \mathcal{C}$, the line segment connecting $x$ and $y$ is contained in $\mathcal{C}$.

**Lemma**

An intersection of halfspaces is convex.

**Proof:**

- Defined by $Ax \ge b$
- Need for $x, y \in \mathcal{C}$ and $t \in [0, 1]$, $tx+(1-t)y \in \mathcal{C}$
- $A(tx+(1-t)y)=tAx+(1-t)Ay \ge tb+(1-t)b=b$

**Theorem**

The region defined by a system of linear inequalities is always a convex polytope.

**Separation Lemma**

Let $\mathcal{C}$ be a convex region and $x \notin \mathcal{C}$ a point. Then, there is a hyperplane $H$ separating $x$ from $C$.

**Extreme Points**

A linear function on a polytope takes its minimum/maximum values on vertices

**Intuition of Proof:**

The corners are the only extreme points. Optima must be there.

Linear function on segment takes extreme values on ends. So, optima can be obtained by pushing linear function towards the corners. By repeatedly pushing to lower dimensional facet, it will eventually end at a vertex.

**Linear Programming: Duality**

**Dual Program**

Given the linear program (the primal): $\min {v \cdot x} \\ \text{ s.t. } Ax \ge b$

The dual linear program is the linear program: $\max {y \cdot b} \\ \text{ s.t. } y^TA=v, y \ge 0$

**Intuition**

Suppose we have the following linear program:
$$
\min v_1x_1+v_2x_2 +...+v_nx_n \text{ s.t. }\\
a_{11}x_1+a_{12}x_2+...+a_{1n}x_n \ge b_1
\\
\cdot \cdot \cdot
\\
a_{m1}x_1+a_{m2}x_2+...+a_{mn}x_n \ge b_m
$$
Let $c_i \ge 0$, we can then combine constraints:
$$
c_1 \cdot (a_{11}x_1+a_{12}x_2+...+a_{1n}x_n) \ge c_1 \cdot b_1
\\
\cdot \cdot \cdot
\\
c_m \cdot (a_{m1}x_1+a_{m2}x_2+...+a_{mn}x_n) \ge c_m \cdot b_m
$$
Let $w_i=\sum_{j=1}^m c_ja_{ji}, t=\sum_{j=1}^m c_j b_j$. We can write
$$
\sum_{i=1}^n w_ix_i \ge t
$$
Let $v_i=w_i$, we have
$$
\sum_{i=1}^n {v_ix_i} \ge t
$$
By letting $v_i=w_i$, we need to find $c_i \ge 0$ so that $v_i=\sum_{j=1}^m c_ja_{ji}\forall i$, and $t=\sum_{j=1}^m c_jb_j$ as large as possible.

**Dual bounds**

$\forall x$ such that $Ax \ge b$, $x \cdot v = y^T Ax \ge y^Tb=y \cdot b$

**Theorem**

A linear program and its dual always have the same (numerical) answer.

Theorem (Complementary Slackness)

Consider a primal LP: $\min v \cdot x \\ \text{ s.t. } Ax \ge b$

and its dual LP: $\max y \cdot b \\ \text{ s.t. } y^TA=v, y \ge 0$

Then, in the solutions, $y_i > 0$ only if the $i$-th equation in $x$ is tight.

**Linear Programming: Simplex Method**

```
Simplex:
Start at vertex p
repeat:
	for each equation through p
		relax equation to get edge
		if edge improves objective:
			replace p by other end
			break
	if no improvement: return p
```

```
OtherEndOfEdge:
Vertex p defined by n equations
Relax one, write general solution as p + t*w (Gaussian elimination)
Relaxed inequality requires t >= 0
For each other inequality in system:
	largest t so p + tw satisfies
Let t_0 be the smallest such t
return p + t_0*w
```

