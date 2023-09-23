def fcfs(at, bt):
    order = list(range(len(at)))  # Initialize order with process IDs
    wtd = {}
    tat = []
    wt = []
    d = {}
    for i in range(len(at)):
        d[at[i]] = bt[i]
    
    atsort = sorted(at)
    btsort = []
    for i in atsort:
        btsort.append(d[i])
    
    present = 0
    for i in range(len(atsort)):
        present = present + btsort[i]
        wtd[atsort[i]] = present - atsort[i] - btsort[i]
    
    for i in at:
        wt.append(wtd[i])
    for i in range(len(wt)):
        tat.append(wt[i] + bt[i])
    
    return wt, tat, order


def sjf(at, bt):
    order = []
    wt = [0] * len(at)
    tat = [0] * len(at)
    n = len(at)
    completed = [False] * n
    total_time = 0
    remaining_bt = bt.copy()

    while True:
        min_bt = float('inf')
        shortest = -1

        for i in range(n):
            if not completed[i] and at[i] <= total_time and remaining_bt[i] < min_bt:
                min_bt = remaining_bt[i]
                shortest = i

        if shortest == -1:
            break

        completed[shortest] = True
        total_time += bt[shortest]
        wt[shortest] = total_time - at[shortest] - bt[shortest]
        tat[shortest] = wt[shortest] + bt[shortest]
        order.append(shortest)

    return wt, tat, order

def ps(at, bt, priority):
    order = [] 
    n = len(at)
    wt = [0] * n
    tat = [0] * n
    processes = [(i, at[i], bt[i], priority[i]) for i in range(n)]
    processes.sort(key=lambda x: x[3])
    total_time = 0
    for i in range(n):
        process_id, arrival_time, burst_time, _ = processes[i]
        if arrival_time > total_time:
            total_time = arrival_time
        wt[process_id] = total_time - arrival_time
        total_time += burst_time
        tat[process_id] = wt[process_id] + burst_time
        order.append(process_id) 
    return wt, tat, order

def rr(at, bt, quantum):
    order = []
    n = len(at)
    wt = [0] * n
    tat = [0] * n
    remaining_bt = bt.copy()
    time = 0
    while any(remaining_bt):
        for i in range(n):
            if remaining_bt[i] > 0:
                if remaining_bt[i] <= quantum:
                    time += remaining_bt[i]
                    wt[i] = time - at[i] - bt[i]
                    remaining_bt[i] = 0
                else:
                    time += quantum
                    remaining_bt[i] -= quantum
                tat[i] = wt[i] + bt[i]
                order.append(i) 
    return wt, tat, order

def avgwt(wt):
    return sum(wt)/len(wt)

def avgtat(tat):
    return sum(tat)/len(tat)

at = [0,10,15,20]
bt = [30,20,40,15]
p = [3,5,2,4]

# fcfs
wt,tat,orderfcfs = fcfs(at,bt)
wtfcfs = avgwt(wt)
tatfcfs = avgtat(tat)

# sjf
wt,tat,ordersjf = sjf(at,bt)
wtsjf = avgwt(wt)
tatsjf = avgtat(tat)

# ps
wt,tat,orderps = ps(at,bt,p)
wtps = avgwt(wt)
tatps = avgtat(tat)

# rr
wt,tat,orderrr = rr(at,bt,4)
wtrr = avgwt(wt)
tatrr = avgtat(tat)

print([wtfcfs,wtsjf,wtps,wtrr])
print([tatfcfs,tatsjf,tatps,tatrr])

# for this question by looking at the average waiting time, we can tell that shortest job first 
# is the most efficient scheduling method to solve this problem, we can save the maximum number of lives using this.

print(ordersjf)
# the order of attending the patients is A,D,B,C