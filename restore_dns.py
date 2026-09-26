#!/usr/bin/env python3
"""
CSAFETYSEE - Restore DNS
Restores network adapters to automatic (DHCP) DNS settings.
"""

import subprocess
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def restore_dns():
    print("[*] Restoring DNS settings to automatic (DHCP)...")

    cmd = (
        "Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | "
        "ForEach-Object { Set-DnsClientServerAddress -InterfaceIndex $_.InterfaceIndex "
        "-ResetServerAddresses -ErrorAction SilentlyContinue }"
    )

    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", cmd],
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0:
            print("[+] DNS settings restored to automatic.")
            print("[i] You may want to run 'ipconfig /flushdns' and restart your browser.")
        else:
            print("[-] Failed to restore DNS.")
            print(result.stderr or result.stdout)
    except Exception as e:
        print(f"[-] Error: {e}")


def main():
    if not is_admin():
        print("[-] Administrator privileges required.")
        print("[*] Requesting elevation...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{__file__}"', None, 1
        )
        sys.exit(0)
    else:
        restore_dns()
        print("\nPress Enter to exit...")
        input()


if __name__ == "__main__":
    main()
