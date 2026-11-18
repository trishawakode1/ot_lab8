# Track J: data locality demonstration and test prioritization toy.
import random, time
N=500
matrix=[[i+j for j in range(N)] for i in range(N)]
def row_major():
    s=0
    for i in range(N):
        for j in range(N): s+=matrix[i][j]
    return s
def col_major():
    s=0
    for j in range(N):
        for i in range(N): s+=matrix[i][j]
    return s
if __name__=="__main__":
    t=time.perf_counter(); a=row_major(); tr=time.perf_counter()-t
    t=time.perf_counter(); b=col_major(); tc=time.perf_counter()-t
    print("Same checksum:",a==b,a)
    print("Row-major seconds:",tr,"Column-major seconds:",tc)
    print("This illustrates locality only; full Track J needs a realistic 1,000+ LOC/public codebase and optimization formulation.")
