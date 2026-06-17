import json
import os

log_file = "/home/olugbenga-mayowa/.gemini/antigravity/brain/fdb03f6d-6043-4d11-a7d1-2404688f44a1/.system_generated/logs/overview.txt"

with open(log_file, "r") as f:
    for line in f:
        try:
            data = json.loads(line)
        except:
            continue
        
        if "tool_calls" in data:
            for call in data["tool_calls"]:
                if call["name"] == "write_to_file":
                    args = call["args"]
                    target_raw = args.get("TargetFile", "")
                    if "premium-coffee-website" in target_raw:
                        try:
                            target = json.loads(target_raw)
                        except:
                            target = target_raw
                        target = target.strip('"')
                        
                        try:
                            content = json.loads(args["CodeContent"])
                        except:
                            content = args["CodeContent"]
                        
                        print(f"Restoring {target}")
                        os.makedirs(os.path.dirname(target), exist_ok=True)
                        with open(target, "w") as out:
                            out.write(content)

