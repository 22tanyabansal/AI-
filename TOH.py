def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

if __name__ == "__main__":
    N = int(input("Enter the number of disks: "))
    from_rod = input("Enter the name of the source rod: ")
    to_rod = input("Enter the name of the destination rod: ")
    aux_rod = input("Enter the name of the auxiliary rod: ")

    TowerOfHanoi(N, from_rod, to_rod, aux_rod)








# Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. 
# Initially, all the disks are stacked in decreasing value of diameter i.e., 
# the smallest disk is placed on the top and they are on rod A. 
# The objective of the puzzle is to move the entire stack to another rod (here considered C), 
# obeying the following simple rules: 

# Only one disk can be moved at a time.
# Each move consists of taking the upper disk from one of the stacks and 
# placing it on top of another stack i.e. a disk can only be moved if it is 
# the uppermost disk on a stack.
# No disk may be placed on top of a smaller disk.

# Follow the steps below to solve the problem:
# Create a function towerOfHanoi where pass the N (current number of disk), from_rod, to_rod, aux_rod.
# Make a function call for N – 1 th disk.
# Then print the current the disk along with from_rod and to_rod
# Again make a function call for N – 1 th disk.