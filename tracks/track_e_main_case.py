# Track E: task scheduling. Greedy earliest-deadline-first vs exact subset search.
tasks=[("Report",3,5),("Lab",2,3),("Quiz",1,2),("Project",4,7)] # name,duration,deadline
def edf():
    t=0; met=0; order=[]
    for name,d,deadline in sorted(tasks,key=lambda x:x[2]):
        t+=d; met+=t<=deadline; order.append(name)
    return order,met,t
def brute():
    import itertools
    best=None
    for perm in itertools.permutations(tasks):
        t=0; met=0
        for name,d,deadline in perm:
            t+=d; met+=t<=deadline
        score=(met,-t)
        if best is None or score>best[0]: best=(score,[x[0] for x in perm],t)
    return best
if __name__=="__main__":
    print("Decision: task order; objective: maximize on-time completions, then minimize completion time.")
    print("Constraints: one machine, non-preemptive tasks, durations fixed.")
    print("Greedy EDF:",edf())
    print("Exact enumeration:",brute())
    print("Strategy: exact search is feasible for tiny n; use heuristics/ILP for larger instances.")
