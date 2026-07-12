import json

def run():

    with open("drift_report.json","r") as f:
        drift_report = json.load(f)

    with open("system_dependencies.json","r") as f:
        dependencies = json.load(f)

    dependency_map = {
        item["system"]: item["depends_on"]
        for item in dependencies
    }

    def find_dependencies(system, visited):

        if system in visited:
            return

        visited.add(system)

        for dep in dependency_map.get(system, []):
            find_dependencies(dep, visited)

    blast_report = []

    for event in drift_report:

        if not event["drift_detected"]:
            continue

        affected = set()

        find_dependencies(
            event["system"],
            affected
        )

        affected.add(event["system"])

        blast_report.append({

            "event_id": event["event_id"],

            "control_id": event["control_id"],

            "system": event["system"],

            "severity": event["severity"],

            "affected_systems": sorted(list(affected)),

            "blast_radius": len(affected)

        })

    with open("blast_radius_report.json","w") as f:
        json.dump(blast_report,f,indent=4)

    print("\nBlast Radius Analysis Completed")
    print("Total Records :",len(blast_report))

    return "blast_radius_report.json"

if __name__=="__main__":
    output=run()
    print(f"\nGenerated: {output}")