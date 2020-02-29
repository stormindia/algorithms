enQueue(q,  x)
  1) Push x to stack1 (assuming size of stacks is unlimited).
Here time complexity will be O(1)

deQueue(q)
  1) If both stacks are empty then error.
  2) If stack2 is empty
       While stack1 is not empty, push everything from stack1 to stack2.
  3) Pop the element from stack2 and return it.
Here time complexity will be O(n)


push - 1 2 3 4 5
pop  -            1 2
push -                  3 4 5 6 7
pop -                               3

stack1     stack2       deQueue
5
4
3
2
1

            1
            2
            3
            4
            5

            3               1,2
            4
            5


enQueue  6,7

            3
7           4
6           5

                            3 (step 3 of deQueue)

7           4
6           5
