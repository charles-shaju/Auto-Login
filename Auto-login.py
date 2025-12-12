import subprocess

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
    get_wifi_list()
