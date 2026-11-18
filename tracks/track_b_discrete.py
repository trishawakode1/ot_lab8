# Track B: 0/1 knapsack — greedy ratio vs exact exhaustive search.
items=[("A",4,7),("B",5,9),("C",3,5),("D",2,4)] # name, weight, value
capacity=7
def greedy():
    chosen=[]; w=v=0
    for name,wt,val in sorted(items,key=lambda z:z[2]/z[1],reverse=True):
        if w+wt<=capacity: chosen.append(name); w+=wt; v+=val
    return chosen,w,v
def exact():
    best=([],0,0)
    for mask in range(1<<len(items)):
        chosen=[]; w=v=0
        for i,item in enumerate(items):
            if mask>>i&1:
                name,wt,val=item; chosen.append(name); w+=wt; v+=val
        if w<=capacity and v>best[2]: best=(chosen,w,v)
    return best
if __name__=="__main__":
    print("Capacity:",capacity)
    print("Greedy:",greedy())
    print("Exact exhaustive baseline:",exact())
    print("Note: exhaustive search is exact only for this small instance; ILP/B&B/QUBO remain additional work.")
