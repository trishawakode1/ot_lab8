# Submission status — read before submitting

| Track | Included in package | Status / limitation |
|---|---|---|
| A Continuous | Gradient descent and momentum on convex/non-convex toy functions | Runnable educational experiment; not the full optimizer list in the assignment |
| B Discrete | Greedy vs exhaustive search for small knapsack | Runnable; ILP/Branch-and-Bound/QUBO coverage remains incomplete |
| C Quantum optimization | Tiny QAOA-inspired Max-Cut parameter grid demo | Classical simulation only; VQE/PQC/QNN/noise/shot study incomplete |
| D Submodular/parallel/distributed | Greedy coverage, multiprocessing timing, simple load distribution | Partial; no full FedAvg/MGDA/GradNorm study |
| E Main case study | Task scheduling with greedy vs exhaustive search on small input | Runnable; replace sample data with documented real/simulated dataset and repeat benchmarks |
| F Compiler | Tiny expression optimizer demonstrating constant folding and dead-code elimination | Educational toy pass; not a complete lexer/parser/code generator compiler |
| G xv6 | Patch plan and benchmark checklist only | NOT IMPLEMENTED/TESTED. Requires xv6 source tree, QEMU and actual patch/diff |
| H DBMS | SQLite query/index demonstration with EXPLAIN QUERY PLAN | Runnable; extend with fair workloads, competing index/join-order methods and storage measurements |
| I Quantum algorithms/QML | Grover search toy state-vector demonstration | Simulation only; QML-vs-classical study and all course algorithms incomplete |
| J Software engineering | Cache/locality and test-priority toy demonstration | Small demonstration; assignment asks a non-trivial codebase (e.g. 1,000+ LOC/public project), not met by this toy |

## Do not misrepresent
This package is useful as a starting point and contains working small experiments, but it does **not** satisfy every detailed requirement in the assignment PDF. In particular, do not claim a completed xv6 patch, real quantum hardware, full Chapter 6 algorithm coverage, full QML comparison, full distributed optimization, or a 1,000+ line codebase.
