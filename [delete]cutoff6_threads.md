# Thread Diagram 

```
Level 0:                      [ main ]                                  (alive this level: 1, peak no. threads: 1)
                              /       \
Level 1:                [T]               [T]                           (alive this level: 2, peak no. threads: 3)
                         / \             / \
Level 2:              [T]   [T]       [T]   [T]                         (alive this level: 4, peak no. threads: 7)
```

So the maximum peak no. of threads is `2^(cutoff+1) -1` ?

A full binary tree with depth C has (2^(C+1)-1) total nodes (recall: depth starts from 0). Here, every node except the root (thus minus 1) corresponds to a created thread