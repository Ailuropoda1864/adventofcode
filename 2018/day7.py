day = 7

###############################
from read_input import *
import re

download_input_file(day)


class Step:
    offset = ord('A') - 61
    
    def __init__(self, uid):
        self.uid = uid
        self.seconds = ord(uid) - Step.offset
        self.prereq = set()
        self.downstream = set()

    def add_prereq(self, prereq):
        self.prereq.add(prereq)
        return self

    def add_downstream(self, downstream):
        self.downstream.add(downstream)
        return self

    def is_available(self, completed):
        # itself is not completed and all the prerequisites are completed
        return self.uid not in completed and self.prereq <= set(completed)


def parse_instructions(input_file):
    pattern = re.compile(r'Step (\w) must be finished before step (\w) can begin.')
    steps = {}
    with open(input_file) as f:
        for line in f:
            step1, step2 = pattern.match(line).groups()
            steps[step1] = steps.get(step1, Step(step1)).add_downstream(step2)
            steps[step2] = steps.get(step2, Step(step2)).add_prereq(step1)
    return steps


def update_available(steps, step, available, completed):
    for d in steps[step].downstream:
        if steps[d].is_available(completed):
            available.add(d)


# Part One
def complete_steps(steps):
    completed = ''
    available = set(k for k, v in steps.items() if len(v.prereq) == 0)

    num_steps = len(steps)
    while len(completed) < num_steps:
        step = min(available)
        completed += step
        available.remove(step)
        update_available(steps, step, available, completed)

    return completed


def part1(steps):
    return complete_steps(steps)


# Part Two
class Worker:
    def __init__(self):
        self.available_time = 0
        self.task = None

    def assign(self, step, current_time):
        self.task = step.uid
        self.available_time = current_time + step.seconds
        return self


def assign_work(available, workers, current_time):
    to_do = sorted(available)
    available_worker_ids = [id for id, worker in enumerate(workers)
                            if worker.available_time <= current_time]
    for step in to_do:
        id = available_worker_ids.pop(0)
        workers[id] = workers[id].assign(steps[step], current_time)
        available.remove(step)

        if not available_worker_ids:
            break


def parallelize(steps, n):
    workers = [Worker() for _ in range(n)]
    completed = ''
    available = set(k for k, v in steps.items() if len(v.prereq) == 0)

    current_time = 0
    num_steps = len(steps)
    while len(completed) < num_steps:
        assign_work(available, workers, current_time)

        task_completed = False
        # start the clock until the second one or more steps are completed
        while not task_completed:
            current_time += 1
            for id, worker in enumerate(workers):
                if worker.available_time == current_time:
                    task_completed = True
                    completed += worker.task
                    update_available(steps, worker.task, available, completed)

    return current_time


def part2(instr):
    return parallelize(instr, 5)


if __name__ == '__main__':
    steps = parse_instructions('input.txt')
    print(part1(steps))
    print(part2(steps))
