def hanoi_solver(n):
    # Initialize rods: Rod 1 has disks [n, n-1, ..., 1], others are empty
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record_state():
        """Formats the current state of rods as a string."""
        return f"{rods[0]} {rods[1]} {rods[2]}"

    def move_disks(disks, source, target, auxiliary):
        if disks == 1:
            # Move the top disk
            rods[target].append(rods[source].pop())
            moves.append(record_state())
            return

        # Move n-1 disks to the auxiliary rod
        move_disks(disks - 1, source, auxiliary, target)
        
        # Move the nth disk to the target rod
        rods[target].append(rods[source].pop())
        moves.append(record_state())
        
        # Move the n-1 disks from auxiliary to target rod
        move_disks(disks - 1, auxiliary, target, source)

    # Add the starting arrangement
    moves.append(record_state())
    
    # Solve if there are disks
    if n > 0:
        move_disks(n, 0, 2, 1)
        
    return "\n".join(moves)

# Example usage:
# print(hanoi_solver(3))
