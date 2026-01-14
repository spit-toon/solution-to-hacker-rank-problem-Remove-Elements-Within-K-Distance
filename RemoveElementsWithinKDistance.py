def debounceTimestamps(timestamps, K):
    if not timestamps:
        return 0

    # Index of last kept timestamp
    write = 0

    for read in range(1, len(timestamps)):
        if timestamps[read] - timestamps[write] >= K:
            write += 1
            timestamps[write] = timestamps[read]

    # New length is write index + 1
    return write + 1



