"""
Optional stretch. Turning a dictionary of counts into a ranked report.
"""

page_counts = {"/home": 5, "/basket": 2, "/checkout": 3}

print(sorted(page_counts))
print(sorted(page_counts.values()))

ranked = sorted(page_counts.items(), key=lambda pair: pair[1], reverse=True)
print(ranked)

print("Pages by traffic:")
position = 1
for page, count in ranked:
    print(f"  {position}. {page} ({count})")
    position = position + 1
