import time


def ft_tqdm(range):
    total = len(range)
    start_time = time.time()

    for i, item in enumerate(range):
        elapsed_time = time.time() - start_time
        progress = int((i + 1) / total * 100)
        progress_str = str(progress).rjust(3)

        if i > 0:
            speed = i / elapsed_time
            remaining_time = (total - i) / speed
        else:
            speed = 0
            remaining_time = 0

        print(
            f"{progress_str}%|{'=' * int(progress)}\
{' ' * (100 - (int(progress)))}| {i + 1}/{total} "
            f"[{elapsed_time:.1f}:{remaining_time:.1f}\
<{int(remaining_time + elapsed_time)}, {speed:.2f}it/s]",
            end="\r" if i + 1 < total else "\n",
        )
        yield item
