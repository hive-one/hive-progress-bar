import sys
import math
import threading
import time


def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()


class ProgressBar:
    num_blocks = 35
    block_size_pct = 100/num_blocks
    processed = 0
    current_blocks = -1
    lock = threading.Lock()
    mt = False
    start = None

    def __init__(self, label, total_items, mt=False):
        self.label = label
        self.total_items = total_items
        self.mt = mt
        self.finished = False

    def next(self):
        if self.mt:
            self.lock.acquire()

        if self.finished:
            return

        if not self.start:
            self.start = time.time()
            self.last_t = self.start

        self.processed += 1

        pct_progress = (self.processed/self.total_items) * 100
        num_blocks = self.num_blocks if self.processed == self.total_items else math.floor(
            (pct_progress) / self.block_size_pct)
        time_since_last_measurement = time.time() - self.last_t
        if num_blocks > self.current_blocks or time_since_last_measurement > 30:
            self.current_blocks = num_blocks
            restart_line()
            sys.stdout.write(self.label)
            sys.stdout.write(': [')
            [sys.stdout.write('#') for _ in range(num_blocks)]
            [sys.stdout.write(' ') for _ in range(
                self.num_blocks - num_blocks)]
            sys.stdout.write(']')
            sys.stdout.write(f' {self.get_eta_string()}')
            sys.stdout.write(' | ')
            sys.stdout.write(
                f'{self.processed} / {self.total_items} Processed')
            if self.num_blocks == num_blocks:
                sys.stdout.write('\n')
            sys.stdout.flush()
            self.last_t = time.time()

        if self.processed >= self.total_items:
            duration = time.time() - self.start
            self.finished = True
            sys.stdout.write(
                f'\nTime Taken: {seconds_to_time_string(duration)}\n')
            return

        if self.mt:
            self.lock.release()

    def get_eta_string(self):
        if self.processed == 1:
            return "Calculating ETA"
        now = time.time()
        elapsed_seconds = now - self.start
        time_per_item = elapsed_seconds / self.processed

        time_remaining = (
            self.total_items - self.processed) * time_per_item

        return f"{seconds_to_time_string(time_remaining)} remaining"


def seconds_to_time_string(seconds):
    hours = math.floor(seconds / 3600)

    total = seconds - hours*3600

    minutes = math.floor(total / 60)

    seconds = math.ceil(total - minutes * 60)

    return f"{hours:>3}h {minutes:>2}m {seconds:>2}s"
