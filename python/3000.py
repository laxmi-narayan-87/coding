from datetime import datetime, timedelta
from collections import defaultdict

def parse_log_entry(entry):
    """Parse a log entry into components."""
    parts = entry.split()
    timestamp = datetime.fromisoformat(parts[0].replace("Z", "+00:00"))
    username = parts[1]
    ip_address = parts[2]
    access_result = parts[3]
    return timestamp, username, ip_address, access_result

def process_logs(logs):
    user_failures = defaultdict(list)  # Stores timestamps of user failures
    ip_failures = defaultdict(list)    # Stores timestamps of IP failures
    user_suspensions = set()           # Stores suspended usernames
    ip_blacklists = {}                 # Stores blacklisted IPs with expiration
    violations = []                    # Stores the violations

    for log in logs:
        timestamp, username, ip_address, access_result = parse_log_entry(log)

        # Handle user suspensions
        if username in user_suspensions:
            violations.append(f"SUSPENSION_VIOLATION {timestamp.isoformat()}Z {username} {ip_address}")
            continue

        # Handle IP blacklists
        if ip_address in ip_blacklists and timestamp < ip_blacklists[ip_address]:
            violations.append(f"BLACKLIST_VIOLATION {timestamp.isoformat()}Z {username} {ip_address}")
            continue

        # Process login results
        if access_result == "FAILURE":
            # Update user failure history
            user_failures[username].append(timestamp)
            user_failures[username] = [t for t in user_failures[username] if timestamp - t <= timedelta(hours=24)]

            # Check for suspension
            if len(user_failures[username]) >= 10:
                user_suspensions.add(username)
                violations.append(f"SUSPENSION_VIOLATION {timestamp.isoformat()}Z {username} {ip_address}")
                continue

            # Check for lockout
            recent_failures = user_failures[username][-3:]
            if len(recent_failures) == 3 and (recent_failures[-1] - recent_failures[0]).total_seconds() <= 300:
                violations.append(f"LOCKOUT_VIOLATION {timestamp.isoformat()}Z {username} {ip_address}")
                continue

            # Update IP failure history
            ip_failures[ip_address].append(timestamp)
            ip_failures[ip_address] = [t for t in ip_failures[ip_address] if timestamp - t <= timedelta(minutes=20)]

            # Check for blacklist
            if len(ip_failures[ip_address]) >= 5:
                ip_blacklists[ip_address] = timestamp + timedelta(minutes=30)
                violations.append(f"BLACKLIST_VIOLATION {timestamp.isoformat()}Z {username} {ip_address}")

        elif access_result == "SUCCESS":
            # Reset user failure count on success
            if username in user_failures:
                user_failures[username] = []

    return violations

def main():
    # Input number of logs
    n = int(input())
    logs = [input().strip() for _ in range(n)]

    # Process and output the results
    violations = process_logs(logs)
    for violation in violations:
        print(violation)

if _name_ == "_main_":
    main()