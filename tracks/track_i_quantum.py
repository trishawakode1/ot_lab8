# Track I: Grover search educational probability-amplification illustration.
# This is an analytic toy demonstration, not a gate-level circuit or hardware execution.
import math
N=16
marked=1
theta=math.asin(1/math.sqrt(N))
print("Search space N =",N,"marked states =",marked)
for r in range(5):
    p=math.sin((2*r+1)*theta)**2
    print(f"Grover iterations={r}: success probability={p:.4f}")
print("Compare classical unstructured search: up to N checks in worst case.")
print("Full assignment additionally asks for circuits, QML-vs-classical comparison and broader course algorithms.")
