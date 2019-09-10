from collections import defaultdict
def task_scheduler(tasks, cooldown):
    fr = defaultdict(int)
    for task in tasks:
        fr[task] += 1
    most_fr = max(fr.values())
    num_most_fr = 0
    for f in fr.values():
        if f == most_fr:
            num_most_fr += 1
    return max(len(tasks), (most_fr - 1) * (cooldown + 1) + num_most_fr)

if __name__ == '__main__':
    tasks = [1, 2, 1, 1, 2, 3, 4]
    cooldown = 2
    print(task_scheduler(tasks, cooldown))