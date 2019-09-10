def task_scheduler(tasks, cooldown):
    if not tasks:
        return 0
    slot = 0
    table = {}
    for task in tasks:
        if task in table and table[task] > slot:
            slot = table[task]
        table[task] = slot + cooldown + 1
        slot += 1
    return slot

if __name__ == '__main__':
    tasks = [1, 2, 1, 1, 3, 4]
    cooldown = 2
    print(task_scheduler(tasks, cooldown))