from pathlib import Path
import subprocess, sys
scripts = sorted(Path("tracks").glob("track_*.py"))
for script in scripts:
    print("\n" + "="*72 + "\nRUNNING", script, "\n" + "="*72)
    subprocess.run([sys.executable, str(script)], check=False)
