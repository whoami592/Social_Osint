import csv
import json
from database import get_results


def export_csv(filename="osint_report.csv"):
    results = get_results()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Username",
            "Platform",
            "Profile URL",
            "Notes",
            "Created At"
        ])

        writer.writerows(results)

    return filename


def export_json(filename="osint_report.json"):
    results = get_results()

    data = []

    for row in results:
        data.append({
            "id": row[0],
            "username": row[1],
            "platform": row[2],
            "profile_url": row[3],
            "notes": row[4],
            "created_at": row[5]
        })

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return filename