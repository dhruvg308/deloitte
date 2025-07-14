def iso_to_millis(iso_str: str) -> int:
    # IMPLEMENT: convert 2025-07-14T12:00:00Z → 1720958400000
    ...

def unify_record(record: dict) -> dict:
    # IMPLEMENT: take one record from either data-1 or data-2
    # and return it in the data-result format
    ...

from datetime import datetime, timezone

def iso_to_millis(iso_str: str) -> int:
    # Parse ISO string to aware datetime
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    # Unix epoch milliseconds
    return int(dt.timestamp() * 1000)

def unify_record(record: dict) -> dict:
    out = {}
    # Copy shared fields
    out["deviceId"] = record["deviceId"]
    out["sensor"]   = record["sensor"]
    # Time handling
    if isinstance(record["timestamp"], str):           # ISO 8601
        out["timestamp"] = iso_to_millis(record["timestamp"])
    else:                                              # already ms
        out["timestamp"] = record["timestamp"]
    # Readings stay unchanged
    out["value"] = record["value"]
    return out

