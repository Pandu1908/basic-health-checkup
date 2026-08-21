print("🩺 BASIC HEALTH CHECKUP")

temperature = float(input("Enter temperature: "))
heart_rate = int(input("Enter heart rate: "))

if temperature > 38:
    print("⚠️ High temperature detected.")
else:
    print("✅ Temperature is normal.")

if heart_rate < 60 or heart_rate > 100:
    print("⚠️ Heart rate is outside the typical resting range.")
else:
    print("✅ Heart rate is within the typical resting range.")
