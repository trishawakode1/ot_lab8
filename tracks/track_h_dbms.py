# Track H: SQLite index demonstration with EXPLAIN QUERY PLAN.
import sqlite3, time, random
random.seed(7)
con=sqlite3.connect(":memory:")
cur=con.cursor()
cur.execute("CREATE TABLE events(id INTEGER PRIMARY KEY, category INTEGER, payload TEXT)")
cur.executemany("INSERT INTO events(category,payload) VALUES (?,?)",
                [(random.randrange(100), "x"*40) for _ in range(30000)])
con.commit()
def explain():
    return cur.execute("EXPLAIN QUERY PLAN SELECT * FROM events WHERE category=42").fetchall()
if __name__=="__main__":
    print("Plan before index:",explain())
    t=time.perf_counter()
    for _ in range(100): cur.execute("SELECT * FROM events WHERE category=42").fetchall()
    before=time.perf_counter()-t
    cur.execute("CREATE INDEX idx_category ON events(category)")
    print("Plan after index:",explain())
    t=time.perf_counter()
    for _ in range(100): cur.execute("SELECT * FROM events WHERE category=42").fetchall()
    after=time.perf_counter()-t
    print("Measured elapsed seconds (100 queries), before/after:",before,after)
    print("In-memory synthetic benchmark; repeat runs and measure index storage for a defensible result.")
