import heapq

def parallel_processing(n, m, data):
    output = []
    pavedieni = [(0, i) for i in range(n)]
    heapq.heapify(pavedieni)
    for i in range(m):
        time = data[i]
        f_time, pavediens = heapq.heappop(pavedieni)
        if output:
            s_time = max(f_time, output[-1][1])
        else:
            s_time = f_time
        f_time = s_time + time
        output.append((pavediens, s_time))
        heapq.heappush(pavedieni, (f_time, pavediens))
    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for pavediens, start_time in result:
        print(pavediens, start_time)


if __name__ == "__main__":
    main()

