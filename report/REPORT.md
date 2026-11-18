# Assignment 8 — Optimize Anything
## Emergency technical report draft

**Student:** [Your name]  
**Roll number:** [Your roll number]  
**Course:** Optimization Techniques  
**Submission date:** [Date]  
**Repository:** [Public GitHub URL]

> **Evidence note:** This report is a draft accompanying small reproducible educational demonstrations. It does not claim that all detailed assignment requirements have been completed. Replace placeholders with actual run outputs, machine details, plots, prompt exports and verified implementations.

## 1. Abstract
This work explores optimization as a process of selecting decisions to improve an objective under constraints. Small experiments demonstrate continuous optimization, discrete selection, greedy submodular coverage, scheduling, a compiler rewrite, a database index, parallel work distribution, data locality and introductory quantum-search/Max-Cut concepts. Results must be interpreted within the limitations stated for each track.

## 2. Chapter 6 syllabus mapping
| Syllabus area | Demonstration | Evidence |
|---|---|---|
| Continuous optimization | GD and momentum on a convex objective; non-convex stationary-point discussion | `tracks/track_a_continuous.py` |
| Discrete optimization | Greedy and exhaustive knapsack | `tracks/track_b_discrete.py` |
| Submodular functions | Greedy maximum coverage | `tracks/track_d_parallel.py` |
| Load balancing | Greedy largest-processing-time assignment | `tracks/track_d_parallel.py` |
| Data locality optimization | Row-major vs column-major traversal | `tracks/track_j_software.py` |
| Synchronization and communication | Threaded work experiment and overhead discussion | `tracks/track_d_parallel.py` |
| Optimization strategy selection | Exact search for small scheduling instances vs heuristic for scale | `tracks/track_e_main_case.py` |

## 3. Track E — Main case study: task scheduling
### Problem
A single processor must execute a set of non-preemptive tasks. Each task has a duration and deadline. The aim is to maximize the number of tasks completed by their deadlines, with total completion time as a secondary criterion.

### Mathematical formulation
Let tasks be indexed by i, with duration p_i and deadline d_i. Let π be a permutation describing execution order and C_i(π) the completion time of task i. The objective is:
Maximize Σ_i 1[C_i(π) ≤ d_i].
For the small benchmark, all tasks execute on one machine, durations are fixed and tasks are non-preemptive. The exhaustive permutation search is an exact baseline for this small instance; it does not scale factorially.

### Methods
- Earliest-deadline-first (EDF) heuristic.
- Exhaustive enumeration for a tiny instance as an exact reference.

### Results
Run `python tracks/track_e_main_case.py` and paste the actual output here. Do not invent measurements. For a stronger study, generate multiple seeded datasets, increase task count, repeat runs and record objective value/runtime.

## 4. Track A — Continuous optimization
The script compares gradient descent and momentum on f(x)=(x−3)^2, whose global minimum is x=3. It also identifies stationary points of a simple non-convex function. This is a teaching demonstration, not complete coverage of SGD, mini-batches, NAG, AdaGrad, RMSProp, Adam, Newton/Gauss–Newton, backpropagation or curvature approximations required by the assignment.

## 5. Track B — Discrete optimization
A 0/1 knapsack instance compares a value-density greedy heuristic with exhaustive enumeration. Exhaustive search supplies an exact answer for the small instance. Extend with ILP, Branch-and-Bound, dynamic programming and a properly formulated QUBO/Ising problem for full coverage.

## 6. Track C — Quantum optimization
The included code is a classical parameter-search surrogate for a tiny Max-Cut example. It is not a faithful QAOA circuit, quantum simulator run or hardware result. Full assignment requirements include QAOA on the Track B QUBO, VQE/PQCs/QNNs and optimizer variants, plus shots/noise/barren-plateau experiments. These remain incomplete.

## 7. Track D — Submodular, parallel and distributed optimization
The code demonstrates greedy maximum coverage, a simple load assignment heuristic and serial-vs-thread execution. It illustrates that parallel overhead and Python runtime characteristics can erase speedup. It does not implement the full required parallelism taxonomy or FedAvg/MGDA/GradNorm comparisons.

## 8. Track F — Compiler optimization
A toy string-level pass demonstrates constant folding and dead assignment removal. It is not a complete compiler. A full implementation must preserve program output and report instruction count, runtime, code size and compile time.

## 9. Track G — xv6 operating-system optimization
Not implemented in this emergency package. A genuine submission requires an xv6 kernel patch, QEMU boot, at least three workloads, `usertests`, before/after metrics and a patch/diff. Do not claim completion without these artifacts.

## 10. Track H — DBMS optimization
A synthetic SQLite workload compares query plans and repeated query timings before/after adding an index. Record actual output, repeat measurements and storage cost. Extend to compare at least two optimization methods against the DBMS default optimizer.

## 11. Track I — Quantum algorithms and QML
The included Grover example is an analytic probability illustration only. It is not a gate-level circuit, hardware experiment or QML model comparison. Full requirements remain incomplete.

## 12. Track J — Software engineering optimization
A matrix traversal experiment illustrates data locality and correctness via checksum equality. It is not a realistic 1,000+ line codebase. Full Track J requires profiling a realistic project, formulating an optimization decision and comparing a Chapter 6 method against a naive baseline.

## 13. AI-assisted development disclosure
Complete the AI tools register and prompt logs using actual records. Include screenshots/chat exports, commit links and manual corrections. Include at least three genuine AI errors and fixes and a comparison of two AI tools on one task. Do not fabricate these records.

## 14. Reproducibility and limitations
Record OS, CPU, RAM, Python version, package versions, date, random seeds, input sizes and repeat counts. Timings are machine-dependent. Use multiple runs and report mean and variability. Simulated/analytic quantum results must not be described as hardware speedups.

## 15. Conclusion
The demonstrations show that optimization requires a well-defined objective, constraints, a baseline, a suitable method and correctness checks. Exact methods are useful for small instances, while heuristics can be more practical at scale. Parallelism and locality depend on overhead and hardware. The package is an educational starting point; the outstanding items in `STATUS.md` must be completed before claiming full compliance.
