# hive-progress-bar

This is a simple package to show progress when doing some computations on a collection. It shows the number of items iterated and a time estimate for the remaining items.

It over-writes the same line that progress bar is on as the iteration continues.

## Installation

`pip install hive-progress-bar`

## Usage

```
import time
from hive_progress_bar import ProgressBar

items = range(100)

pb = ProgressBar("Doing stuff on collection", len(items))

for _ in items:
    time.sleep(1)
    pb.next()
```

Example Output During Processing
```
Doing stuff on collection: [####                               ]   0h  1m 21s remaining | 12 / 100 Processed
```

After Finishing
```
Doing stuff on collection: [###################################]   0h  0m  0s remaining | 100 / 100 Processed

Time Taken:   0h  1m 40s
```