def sum_of_intervals(intervals):
    if not intervals:
        return 0

    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged = []
    current_start, current_end = sorted_intervals[0]

    for start, end in sorted_intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    return sum(end - start for start, end in merged)
