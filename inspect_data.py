import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
        
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
        
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }

# Notice we changed the column name to area_km2 here!
result = inspect_column("mydata.csv", "area_km2")
print(result)