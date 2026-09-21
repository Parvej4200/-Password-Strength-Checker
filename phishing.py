phishing_keywords = [
    "urgent",
    "verify",
    "password",
    "bank",
    "click here",
    "winner",
    "account suspended"
]

message = input("Enter email/message: ")

print("\nAnalysis Result:")
found = False

for keyword in phishing_keywords:
    if keyword.lower() in message.lower():
        print(f"Red Flag Found: {keyword}")
        found = True

if "http://" in message or "https://" in message:
    print("Red Flag Found: Suspicious Link")
    found = True

if found:
    print("\nWarning: This message may be a phishing attempt.")
else:
    print("\nNo obvious phishing indicators found.")