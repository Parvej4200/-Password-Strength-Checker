audit = {
    "Strong Password": "Yes",
    "MFA Enabled": "No",
    "OS Updated": "Yes",
    "Antivirus Updated": "Yes",
    "Guest Account Disabled": "No",
    "Firewall Enabled": "Yes",
    "Disk Encryption Enabled": "No"
}

print("=== Security Audit Report ===\n")

for item, status in audit.items():
    print(f"{item}: {status}")

print("\n=== Risks Found ===")

for item, status in audit.items():
    if status == "No":
        print(f"- {item} needs attention")