import json
import sys
# Safety check
if len(sys.argv) < 2:
    print("Usage: python monitor.py all/running/costly [output_file]")
    exit()
mode = sys.argv[1].strip().lower()
output_file = None
if len(sys.argv) > 2:
    output_file = sys.argv[2]
with open("ec2_real.json") as file:
    data = json.load(file)
for reservation in data.get("Reservations", []):
    for instance in reservation.get("Instances", []):

        instance_id = instance.get("InstanceId") or "Unknown ID"
        state = instance.get("State") or "unknown"
        instance_type = instance.get("Type") or "unknown"

        if mode == "all":
            line = f"{instance_id} | {state} | {instance_type}"
        elif mode == "running" and state == "running":
            line = f"{instance_id} | {state}"
        elif mode == "stopped" and state == "stopped":
            line = f"{instance_id} | {state}"
        elif mode == "costly" and instance_type in ["t2.large", "t2.medium"]:
            line = f"{instance_id} | {instance_type}"
        else:
            continue

        if output_file:
            with open(output_file, "a") as f:
                f.write(line + "\n")
        else:
            print(line)



