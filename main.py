class Interval:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)


def finish_first(numJobs):
    interval_list = create_interval_list(numJobs)
    interval_list.sort(key=lambda x: x.end)

    num_intervals = 0
    end_time = 0
    for p in range(0, len(interval_list)):
        if int(interval_list[p].start) >= int(end_time):
            end_time = interval_list[p].end
            num_intervals += 1
    return num_intervals


def create_interval_list(numJobs):
    list = []
    for k in range(0, numJobs):
        new_interval_times = input().split(' ')
        new_interval = Interval(new_interval_times[0], new_interval_times[1])
        list.append(new_interval)
    return list


instances = int(input())
for i in range(0, instances):
    intervals = finish_first(int(input()))
    print(intervals)
