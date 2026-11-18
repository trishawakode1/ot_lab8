# Track F: tiny expression rewrite demonstration (constant folding + dead assignment).
def optimize(program):
    out=[]
    for line in program:
        if line.strip()=="x = 2 + 3": line="x = 5"
        if line.strip()=="unused = 99": continue
        out.append(line)
    return out
if __name__=="__main__":
    source=["x = 2 + 3","unused = 99","print(x)"]
    optimized=optimize(source)
    print("Before:",source)
    print("After:",optimized)
    print("Passes: constant folding and dead assignment elimination (toy string-level demo).")
    print("A full compiler, semantic equivalence test suite and code-generation metrics are still required.")
