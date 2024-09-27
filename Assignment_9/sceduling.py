class Process:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def fcfs(processes):
    time = 0
    completion_times = []
    waiting_times = []
    turnaround_times = []
    
    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time
        time += process.burst_time
        process.completion_time = time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        
        completion_times.append(process.completion_time)
        waiting_times.append(process.waiting_time)
        turnaround_times.append(process.turnaround_time)
    
    return completion_times, waiting_times, turnaround_times

def sjf(processes):
    time = 0
    completed = 0
    completion_times = []
    waiting_times = []
    turnaround_times = []

    while completed < len(processes):
        available_processes = [p for p in processes if p.arrival_time <= time and p.remaining_time > 0]
        if available_processes:
            current_process = min(available_processes, key=lambda p: p.remaining_time)
            time += current_process.remaining_time
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed += 1
            
            completion_times.append(current_process.completion_time)
            waiting_times.append(current_process.waiting_time)
            turnaround_times.append(current_process.turnaround_time)
        else:
            time += 1

    return completion_times, waiting_times, turnaround_times

def priority_scheduling(processes):
    time = 0
    completed = 0
    completion_times = []
    waiting_times = []
    turnaround_times = []

    while completed < len(processes):
        available_processes = [p for p in processes if p.arrival_time <= time and p.remaining_time > 0]
        if available_processes:
            current_process = min(available_processes, key=lambda p: (p.priority, p.arrival_time))
            time += current_process.remaining_time
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed += 1
            
            completion_times.append(current_process.completion_time)
            waiting_times.append(current_process.waiting_time)
            turnaround_times.append(current_process.turnaround_time)
        else:
            time += 1

    return completion_times, waiting_times, turnaround_times

def round_robin(processes, time_quantum):
    time = 0
    queue = processes[:]
    completion_times = []
    waiting_times = []
    turnaround_times = []

    while queue:
        process = queue.pop(0)
        if process.remaining_time > 0:
            if process.remaining_time > time_quantum:
                time += time_quantum
                process.remaining_time -= time_quantum
                queue.append(process) 
            else:
                time += process.remaining_time
                process.completion_time = time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                completion_times.append(process.completion_time)
                waiting_times.append(process.waiting_time)
                turnaround_times.append(process.turnaround_time)
                process.remaining_time = 0

    return completion_times, waiting_times, turnaround_times

processes_data = [
    ("P1", 0, 24, 3),
    ("P2", 4, 3, 1),
    ("P3", 5, 3, 4),
    ("P4", 6, 12, 2)
]
# processes_data = [
#     ("P1", 0, 24, 3),
#     ("P2", 4, 3, 1),
#     ("P3", 5, 3, 4),
#     ("P4", 6, 12, 2)
# ]

processes = [Process(*data) for data in processes_data]

fcfs_results = fcfs(processes)
print("FCFS:")
print(f"  Completion Times: {fcfs_results[0]}")
print(f"  Waiting Times: {fcfs_results[1]}")
print(f"  Turnaround Times: {fcfs_results[2]}")
fcfs_throughput = len(processes) / fcfs_results[0][-1]
print(f"  Throughput: {fcfs_throughput:.2f}")

# Reset process data
processes = [Process(*data) for data in processes_data]
sjf_results = sjf(processes)
print("\nSJF:")
print(f"  Completion Times: {sjf_results[0]}")
print(f"  Waiting Times: {sjf_results[1]}")
print(f"  Turnaround Times: {sjf_results[2]}")
sjf_throughput = len(processes) / sjf_results[0][-1]
print(f"  Throughput: {sjf_throughput:.2f}")

# Reset process data
processes = [Process(*data) for data in processes_data]
priority_results = priority_scheduling(processes)
print("\nPriority Scheduling:")
print(f"  Completion Times: {priority_results[0]}")
print(f"  Waiting Times: {priority_results[1]}")
print(f"  Turnaround Times: {priority_results[2]}")
priority_throughput = len(processes) / priority_results[0][-1]
print(f"  Throughput: {priority_throughput:.2f}")

# Reset process data
processes = [Process(*data) for data in processes_data]
round_robin_results = round_robin(processes, time_quantum=4)
print("\nRound Robin:")
print(f"  Completion Times: {round_robin_results[0]}")
print(f"  Waiting Times: {round_robin_results[1]}")
print(f"  Turnaround Times: {round_robin_results[2]}")
round_robin_throughput = len(processes) / round_robin_results[0][-1]
print(f"  Throughput: {round_robin_throughput:.2f}")

throughputs = {
    "FCFS": fcfs_throughput,
    "SJF": sjf_throughput,
    "Priority": priority_throughput,
    "Round Robin": round_robin_throughput,
}

