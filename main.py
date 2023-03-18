import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    for i in range(m):
        time = data[i]
        f_time, thread_idx = heapq.heappop(threads)
        s_time = max(f_time, output[-1][1] if output else 0)
        f_time = s_time + time
        output.append((thread_idx, s_time))
        heapq.heappush(threads, (f_time, thread_idx))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread_idx, start_time in result:
        print(thread_idx, start_time)


if __name__ == "__main__":
    main()

