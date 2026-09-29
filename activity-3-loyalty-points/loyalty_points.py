"""
Loyalty Points

A coffee shop awards points on every purchase. This program takes a
day's purchases and works out where everybody stands at closing time.
"""

BRONZE_THRESHOLD = 100
SILVER_THRESHOLD = 200

points = {
    "alice": 120,
    "bob": 40,
    "siobhan": 195
}

purchases = [
    ("alice", 30),
    ("chen", 15),
    ("bob", 60),
    ("alice", 10),
    ("siobhan", 12)
]


def award_points(points, purchases):
    for name, amount in purchases:
        points[name] = points.get(name, 0) + amount


def tier(total):
    if total >= SILVER_THRESHOLD:
        return "Silver"
    elif total >= BRONZE_THRESHOLD:
        return "Bronze"
    else:
        return "Standard"


print(f"Customers at open: {len(points)}")

award_points(points, purchases)

print(f"Customers at close: {len(points)}")
print("End of day standings:")
for name, total in points.items():
    print(f"  {name}: {total} points, {tier(total)}")
