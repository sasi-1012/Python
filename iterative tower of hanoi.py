def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move the disk 1 from {source} to {destination}")
        return
    
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move the disk {n} from {source} to {destination}")

    tower_of_hanoi(n-1, auxiliary, source, destination)

num_of_disks = int(input())
tower_of_hanoi(num_of_disks, 'pole 1', 'pole 2', 'pole 3')