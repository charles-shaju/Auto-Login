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
    

def get_wifi_list():
    try:
        # Run the nmcli command
        result = subprocess.run(
            ["nmcli", "-t", "-f", "ACTIVE,SSID", "dev", "wifi"],
            capture_output=True,
            text=True
        )
        # If error occurs
        if result.stderr:
            print("Error:\n", result.stderr)
        lines = result.stdout.strip().split("\n")
        for line in lines:
            if line.startswith("yes:"):
                active_ssid = line.split(":", 1)[1]
                print("Active WiFi:", active_ssid)

    except Exception as e:
        print("Exception occurred:", e)

if __name__ == "__main__":
    if is_connected():
        pass
    else:
        get_wifi_list()
