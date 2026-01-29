correct_password = "admin123"
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("✅ Login successful")
        break
    else:
        attempts += 1
        print("❌ Wrong password")
if attempts == max_attempts:
    print("⚠️ ALERT: Too many failed login attempts")