import os
import subprocess

# Cek apakah file ada
if os.path.exists("app.py"):
    subprocess.run(["streamlit", "run", "app.py"])
else:
    print("File app.py tidak ditemukan!")
    print(f"Direktori saat ini: {os.getcwd()}")

    # Tampilkan file .py yang ada
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]
    if py_files:
        print("File .py yang tersedia:", py_files)