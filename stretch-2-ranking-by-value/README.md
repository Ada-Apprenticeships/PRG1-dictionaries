# Stretch 2: Ranking by value

File: `ranking.py`

Optional. Turning a dictionary of counts into a ranked report, which is what
almost every real dashboard is doing underneath.

## Predict

Three lines, then the ranked list. Be careful with the first two: they sort
different things.

## Run

Execute and compare.

## Investigate

- `sorted(page_counts)` and `sorted(page_counts.values())` return different
  things. What is each one being handed?
- `page_counts.items()` gives pairs. `key=lambda pair: pair[1]` picks the second
  item of each pair. Say in one sentence what the sort is therefore ordering by.
- Remove `reverse=True` and predict the output before running it.

## Modify

- Print only the top two pages.
- Rank by name rather than by count, without changing the `sorted` call's
  structure.
