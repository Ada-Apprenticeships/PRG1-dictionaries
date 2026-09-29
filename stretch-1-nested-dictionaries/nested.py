"""
Optional stretch. A first look at a dictionary whose values are
themselves dictionaries, which is how most real configuration and
API data is shaped.
"""

site_traffic = {
    "/home": {"200": 5, "404": 0, "500": 0},
    "/basket": {"200": 1, "404": 1, "500": 0},
    "/checkout": {"200": 1, "404": 0, "500": 2}
}

print(site_traffic["/checkout"])
print(site_traffic["/checkout"]["500"])
print(len(site_traffic))
print(len(site_traffic["/checkout"]))

for page, statuses in site_traffic.items():
    total = 0
    for status, count in statuses.items():
        total = total + count
    print(f"{page}: {total} requests, {statuses['500']} server errors")
