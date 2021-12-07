from typing import Any, Sequence
from datetime import datetime

def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    a.append(key)
    
    while True:
        
        if a[i] == key:
            return i if i != len(a) - 1 else -1
        i += 1

a = [i for i in range(1000000)]
start = datetime.now()
print(seq_search(a, 999999))
end = datetime.now()
print(end-start)