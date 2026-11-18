# Track A: continuous optimization — GD vs momentum on f(x)=(x-3)^2
def f(x): return (x-3.0)**2
def grad(x): return 2*(x-3.0)
def gd(x0, lr=0.1, steps=50):
    x=x0
    for _ in range(steps): x -= lr*grad(x)
    return x, f(x)
def momentum(x0, lr=0.1, beta=0.8, steps=50):
    x=x0; v=0.0
    for _ in range(steps):
        v=beta*v+grad(x); x-=lr*v
    return x, f(x)
if __name__ == "__main__":
    print("Convex objective f(x)=(x-3)^2; baseline x0=10")
    print("GD:", gd(10))
    print("Momentum:", momentum(10))
    # Non-convex illustration: g(x)=x^4-2x^2
    print("Non-convex objective g(x)=x^4-2x^2 has stationary points x=0,+/-1.")
    print("This simple demonstration does not cover every optimizer listed in the assignment.")
