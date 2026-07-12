import json

def run():

    with open("drift_report.json","r") as f:
        drift_report=json.load(f)

    with open("compliance_mapping.json","r") as f:
        mappings=json.load(f)

    compliance_lookup={}

    for item in mappings:

        parameter=item["parameter"]

        if parameter not in compliance_lookup:
            compliance_lookup[parameter]=[]

        compliance_lookup[parameter].append(item)

    compliance_report=[]

    for event in drift_report:

        if not event["drift_detected"]:
            continue

        parameter=event["parameter"]

        violations=compliance_lookup.get(parameter,[])

        compliance_report.append({

            "event_id":event["event_id"],

            "control_id":event["control_id"],

            "system":event["system"],

            "parameter":parameter,

            "severity":event["severity"],

            "violations":violations,

            "total_violations":len(violations)

        })

    with open("compliance_report.json","w") as f:
        json.dump(compliance_report,f,indent=4)

    print("\nCompliance Mapping Completed")
    print("Total Records :",len(compliance_report))

    return "compliance_report.json"

if __name__=="__main__":
    output=run()
    print(f"\nGenerated: {output}")