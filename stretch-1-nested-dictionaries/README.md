# Stretch 1: Dictionaries inside dictionaries

File: `nested.py`

Optional. Only once you have finished the core activities for the session.

A first look at something covered properly later in the module. Each value in
`site_traffic` is itself a dictionary.

## Predict

Four lines, then three more from the loop. Write them all down.

## Run

Execute and compare.

## Investigate

- `site_traffic["/checkout"]` gives a whole dictionary. `site_traffic["/checkout"]["500"]` gives one number. Read the second one out loud in words,
  left to right.
- `len(site_traffic)` and `len(site_traffic["/checkout"])` both give 3, for
  completely different reasons. What is each one counting?
- The status codes are strings here, in quotes. What would go wrong if some were
  strings and some were numbers?

## Modify

- Report the total number of requests across the whole site.
- Report only the pages that had at least one server error.
