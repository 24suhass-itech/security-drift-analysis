import json

with open("baseline_configs.json","r") as f:
    baseline=json.load(f)

parameter_mapping={

"cloudtrail_enabled":[
("NIST 800-53","AU-2","Audit Events"),
("ISO 27001","A.8.15","Logging"),
("CIS AWS","3.1","Enable CloudTrail")
],

"multi_region_trail":[
("NIST 800-53","AU-12","Audit Generation"),
("ISO 27001","A.8.15","Logging"),
("CIS AWS","3.2","Multi Region Logging")
],

"log_file_validation":[
("NIST 800-53","AU-9","Protection of Audit Information"),
("ISO 27001","A.8.15","Log Integrity"),
("CIS AWS","3.3","Log Validation")
],

"kms_encryption":[
("NIST 800-53","SC-13","Cryptographic Protection"),
("ISO 27001","A.8.24","Use of Cryptography"),
("CIS AWS","3.8","Encryption")
],

"public_access":[
("NIST 800-53","AC-3","Access Enforcement"),
("ISO 27001","A.5.15","Access Control"),
("CIS AWS","2.1","Restrict Public Access")
],

"bucket_encryption":[
("NIST 800-53","SC-28","Protection at Rest"),
("ISO 27001","A.8.24","Storage Encryption"),
("CIS AWS","2.3","Encrypt Storage")
],

"versioning":[
("NIST 800-53","CP-9","Information Backup"),
("ISO 27001","A.8.13","Backup"),
("CIS AWS","2.5","Enable Versioning")
],

"access_logging":[
("NIST 800-53","AU-12","Audit Generation"),
("ISO 27001","A.8.15","Logging"),
("CIS AWS","2.6","Access Logging")
],

"ebs_encryption":[
("NIST 800-53","SC-28","Protection at Rest"),
("ISO 27001","A.8.24","Disk Encryption"),
("CIS AWS","4.4","Encrypt EBS")
],

"instance_metadata_v2":[
("NIST 800-53","SI-7","Software Integrity"),
("ISO 27001","A.8.9","Configuration"),
("CIS AWS","4.2","Require IMDSv2")
],

"monitoring_enabled":[
("NIST 800-53","SI-4","System Monitoring"),
("ISO 27001","A.8.16","Monitoring"),
("CIS Azure","5.1","Enable Monitoring")
],

"diagnostic_logging":[
("NIST 800-53","AU-12","Audit Generation"),
("ISO 27001","A.8.15","Diagnostic Logs"),
("CIS Azure","5.2","Diagnostic Logging")
],

"metrics_collection":[
("NIST 800-53","SI-4","Monitoring"),
("ISO 27001","A.8.16","Metrics"),
("CIS Azure","5.3","Metrics Collection")
],

"retention_days":[
("NIST 800-53","AU-11","Retention"),
("ISO 27001","A.8.10","Retention"),
("CIS Azure","5.5","Retention Policy")
],

"port_443":[
("NIST 800-53","SC-7","Boundary Protection"),
("ISO 27001","A.8.20","Network Security"),
("CIS Network","1.2","Secure HTTPS")
],

"port_8080":[
("NIST 800-53","SC-7","Boundary Protection"),
("ISO 27001","A.8.20","Network Security"),
("CIS Network","1.3","Restrict Ports")
],

"firewall_logging":[
("NIST 800-53","AU-12","Firewall Logging"),
("ISO 27001","A.8.15","Logging"),
("CIS Network","2.1","Firewall Logs")
],

"ssh_access":[
("NIST 800-53","AC-17","Remote Access"),
("ISO 27001","A.5.15","Access Control"),
("CIS Network","2.2","Restrict SSH")
],

"threat_prevention":[
("NIST 800-53","SI-3","Malicious Code Protection"),
("ISO 27001","A.8.7","Threat Protection"),
("CIS Network","2.3","Threat Prevention")
],

"url_filtering":[
("NIST 800-53","SI-4","Monitoring"),
("ISO 27001","A.8.23","Web Filtering"),
("CIS Network","2.4","URL Filtering")
],

"logging_enabled":[
("NIST 800-53","AU-2","Logging"),
("ISO 27001","A.8.15","Logging"),
("CIS Windows","1.1","Enable Logs")
],

"bitlocker":[
("NIST 800-53","SC-28","Disk Encryption"),
("ISO 27001","A.8.24","BitLocker"),
("CIS Windows","1.2","Enable BitLocker")
],

"windows_firewall":[
("NIST 800-53","SC-7","Firewall"),
("ISO 27001","A.8.20","Firewall"),
("CIS Windows","1.3","Windows Firewall")
],

"defender_enabled":[
("NIST 800-53","SI-3","Endpoint Protection"),
("ISO 27001","A.8.7","Malware Protection"),
("CIS Windows","1.4","Microsoft Defender")
],

"auto_updates":[
("NIST 800-53","SI-2","Patch Management"),
("ISO 27001","A.8.8","Patch Management"),
("CIS Windows","1.5","Automatic Updates")
],

"auditd_enabled":[
("NIST 800-53","AU-2","Linux Audit"),
("ISO 27001","A.8.15","Audit Logs"),
("CIS Linux","1.1","Auditd")
],

"selinux":[
("NIST 800-53","AC-6","Least Privilege"),
("ISO 27001","A.8.9","Configuration"),
("CIS Linux","1.2","SELinux")
],

"ufw_firewall":[
("NIST 800-53","SC-7","Firewall"),
("ISO 27001","A.8.20","Firewall"),
("CIS Linux","1.3","UFW")
],

"mfa_enabled":[
("NIST 800-53","IA-2","MFA"),
("ISO 27001","A.5.17","Authentication"),
("CIS IAM","1.1","Require MFA")
],

"password_policy":[
("NIST 800-53","IA-5","Password Policy"),
("ISO 27001","A.5.17","Passwords"),
("CIS IAM","1.2","Strong Passwords")
],

"access_key_rotation":[
("NIST 800-53","IA-5","Credential Rotation"),
("ISO 27001","A.5.18","Credential Management"),
("CIS IAM","1.3","Rotate Keys")
],

"least_privilege":[
("NIST 800-53","AC-6","Least Privilege"),
("ISO 27001","A.5.15","Access Control"),
("CIS IAM","1.4","Least Privilege")
],

"conditional_access":[
("NIST 800-53","AC-3","Conditional Access"),
("ISO 27001","A.5.15","Access Control"),
("CIS IAM","1.5","Conditional Access")
],

"risk_policy":[
("NIST 800-53","RA-3","Risk Assessment"),
("ISO 27001","A.5.7","Risk Management"),
("CIS IAM","1.6","Risk Policies")
]

}

mapping=[]

seen=set()

for control in baseline:

    parameter=control["parameter"]

    if parameter in seen:
        continue

    seen.add(parameter)

    for framework,control_id,description in parameter_mapping[parameter]:

        mapping.append({

            "parameter":parameter,

            "framework":framework,

            "control":control_id,

            "description":description

        })

with open("compliance_mapping.json","w") as f:
    json.dump(mapping,f,indent=4)

print("Compliance mappings generated:",len(mapping))