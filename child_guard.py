#!/usr/bin/env python3
"""
CSAFETYSEE - Child Guard
Activates Cloudflare Family DNS (1.1.1.3) to block malware and adult content.
Requires administrator privileges on Windows.
"""

import subprocess
import sys
import ctypes
import time

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def activate_family_filter():
    """Set DNS servers to Cloudflare Family DNS on Wi-Fi and Ethernet adapters."""
    primary_dns = "1.1.1.3"
    secondary_dns = "1.0.0.3"

    print("[*] Activating system-wide child safety filter...")
    print(f"[*] Setting DNS to Cloudflare Family: {primary_dns} / {secondary_dns}")

    # PowerShell command to set DNS on common interface names
    # Covers Wi-Fi, Ethernet, and some common variations
    cmd = (
        f"Get-NetAdapter | Where-Object {{$_.Status -eq 'Up'}} | "
        f"ForEach-Object {{ Set-DnsClientServerAddress -InterfaceIndex $_.InterfaceIndex "
        f"-ServerAddresses ('{primary_dns}','{secondary_dns}') -ErrorAction SilentlyContinue }}"
    )

    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", cmd],
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0:
            print("[+] Success! Dangerous and explicit content is now filtered on this device.")
            print("[i] Note: Restart your browser (or flush DNS with 'ipconfig /flushdns') for changes to take full effect.")
            print("[i] To restore original settings later, run: python restore_dns.py")
        else:
            print("[-] Partial or failed update. Error output:")
            print(result.stderr or result.stdout)
            print("[!] Try running the script again as Administrator.")
    except Exception as e:
        print(f"[-] Unexpected error: {e}")


def main():
    if not is_admin():
        print("[-] This script requires Administrator privileges.")
        print("[*] Requesting elevation...")
        # Re-launch with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{__file__}"', None, 1
        )
        sys.exit(0)
    else:
        activate_family_filter()
        print("\nPress Enter to exit...")
        input()


if __name__ == "__main__":
    main()
