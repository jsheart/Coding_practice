from collections import defaultdict
import heapq
def task_scheduler(tasks, cooldown):
    if not tasks:
        return ''
    result = []
    fr = defaultdict(int)
    for task in tasks:
        fr[task] += 1
    heap = [[-f, str(task)] for task, f in fr.items()]
    heapq.heapify(heap)
    cycle = cooldown + 1
    while heap:
        idle = 0
        temp = []
        for _ in range(cycle):
            if heap:
                temp.append(heapq.heappop(heap))
            else:
                idle += 1
        for task in temp:
            task[0] += 1
            result.append(task[1])
            if task[0] < 0:
                heapq.heappush(heap, task)
        if heap:
            for _ in range(idle):
                result.append('_')
    return ''.join(result)

if __name__ == '__main__':
    tasks = [1, 2, 1, 1, 2, 3, 4, 1, 2, 3]
    cooldown = 3
    print(task_scheduler(tasks, cooldown))