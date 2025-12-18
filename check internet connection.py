import subprocess
import platform

def is_connected():
    # Use different ping parameter for Windows / Linux / macOS
    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        subprocess.check_output(
            ["ping", param, "1", "8.8.8.8"],
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    if is_connected():
        print("✅ Internet is connected")
    else:
        print("❌ No internet connection")
