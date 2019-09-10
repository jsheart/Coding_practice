def task_scheduler(tasks, cooldown):
    if not tasks:
        return ''
    table = {}
    slot = 0
    result = ''
    for task in tasks:
        if task in table and slot < table[task]:
            for _ in range(table[task] - slot):
                result += '_'
            slot = table[task]
        result += str(task)
        table[task] = slot + cooldown + 1
        slot += 1
    return result

if __name__ == '__main__':
    tasks = [1, 2, 1, 1, 3, 4]
    cooldown = 2
    print(task_scheduler(tasks, cooldown))