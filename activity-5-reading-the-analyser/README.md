# Activity 5: Reading the analyser

File: `log_analyser.py`

A real program. It takes a morning of web server log lines and reports what
happened: traffic per page, the busiest page, and everything that failed.

You are not changing anything yet. You are working out how it does what it does.

## Predict

- How many pages appear in the report?
- Which page is busiest, and with how many requests?
- How many requests failed?

Write the whole report out if you can. Then run it.

## Run

Execute and compare.

## Investigate

- `line.split()` turns one line into a list. Print it for a single line and look
  at it. Why is the page at position 2 and not position 1?
- `count_by_page` starts with an empty dictionary and ends with one entry per
  page. Trace the first four lines of the log by hand, writing the dictionary
  out after each one. You will see the pattern by the third.
- `counts.get(page, 0) + 1` is the whole of the counting. Explain what the `0`
  is for. What would happen without it?
- `busiest_page` takes the dictionary that `count_by_page` produced, not the log
  itself. Why is that a better design than passing it the log again?
- `failed_requests` compares against `"200"` in quotes rather than `200`. Try it
  without the quotes and see what the program reports. Do not fix it, just look.

## Modify

- Report the number of distinct users as well as the number of pages.
- Report the quietest page as well as the busiest.
- Add a log line of your own and predict every figure that changes before you
  run it.
