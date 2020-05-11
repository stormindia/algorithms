#Shortest path properties

1. A shortest path tree (SPT) solution exists always.

2. For a source vertex S, we can represent SPT with two vertex-indexed arrays

#EDGE RELAXATION -> e = v -> w
3. distTo[v] is length of shortest *known* path from S to v

4. distTo[w] is length of shortest *known* path from S to w

5. edgeTo[v] is last edge on the shortest *known* path from S to v

6. If an e = v -> w gives shorter path to w through v
    update both distTo[w] and edgeTo[w]


#PROGRAMMING ASSIGNMENT -> seam carving
https://coursera.cs.princeton.edu/algs4/assignments/seam/specification.php
