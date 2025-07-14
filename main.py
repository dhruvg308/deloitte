import json
from datetime import datetime

# Helper function to convert ISO 8601 timestamp to epoch milliseconds
def iso_to_epoch_ms(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)

# IMPLEMENT: normalize_data1
def normalize_data1(data1):
    return [
        {
            "timestamp": iso_to_epoch_ms(entry["timestamp"]),
            "value": entry["value"]
        }
        for entry in data1.get("telemetry", [])
    ]

# IMPLEMENT: normalize_data2
def normalize_data2(data2):
    return [
        {
            "timestamp": entry["timestamp"],
            "value": entry["value"]
        }
        for entry in data2.get("telemetry", [])
    ]

# Main execution block (for local testing/output)
if __name__ == "__main__":
    # Load both JSON files
    with open("data-1.json", "r") as f:
        data1 = json.load(f)

    with open("data-2.json", "r") as f:
        data2 = json.load(f)

    # Normalize both datasets
    normalized_1 = normalize_data1(data1)
    normalized_2 = normalize_data2(data2)

    # Combine and optionally sort by timestamp
    final_output = sorted(normalized_1 + normalized_2, key=lambda x: x["timestamp"])

    # Save result to file
    with open("output.json", "w") as f:
        json.dump(final_output, f, indent=2)

    print("✅ Output saved to output.json")
