total_seconds = int(input("Enter total seconds: "))

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"Time: {minutes}:{seconds:02d}")