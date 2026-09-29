# Activity 7: The analyser, broken

File: `broken_analyser.py`

The same analyser, with three faults introduced. Nothing crashes. Every figure
in the report looks like a figure a real report would produce.

This is the one to reach if you can. Finding a fault in output that looks
reasonable is the skill this whole module is built around.

## Predict

You already know what the correct report looks like from activity 5. Write it
out again from memory.

## Run

Execute it. Compare line by line against the correct version. Three things do
not match.

## Investigate

- The report claims four pages. Look at what it lists under "Requests per page".
  Those are not pages. Which single character in `count_by_page` is responsible?
- The busiest page is reported as the one with the fewest requests. Read
  `busiest_page` line by line and work out what it is actually doing on each
  pass of the loop. Something that should change never does.
- Every single request is reported as failed, including the ones that returned
  200. The comparison in `failed_requests` looks right. Print
  `line.split()[3]` on its own and look hard at what comes back.

## Fault log

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three, then check the report against activity 5's output. It should
match exactly.

> None of these three faults is a typo you would catch by looking. Each one
> needed you to know what the answer should have been before you started. That
> is why activity 5 came first, and it is why the assignment tasks keep asking
> you to predict before you run.
