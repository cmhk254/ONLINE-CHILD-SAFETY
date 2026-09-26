# CSAFETYSEE – Child Safety Network Shield

**Danger detection & content filtering software for child protection**

A lightweight, open-source Windows tool that activates a system-wide network shield to block malware, adult content, and explicit websites. It routes all internet traffic through Cloudflare’s Family DNS (1.1.1.3), which automatically:

- Blocks known malicious and adult domains
- Enforces SafeSearch on Google, Bing, YouTube, and other major search engines
- Provides free, privacy-respecting family-friendly filtering

Ideal for parents, educators, and anyone who wants a simple, effective way to protect devices used by children.

---

## Features

- One-click activation of Cloudflare Family DNS
- Automatic administrator privilege elevation
- Works on Wi-Fi and Ethernet interfaces
- Clean restore option (returns DNS to automatic/DHCP)
- Zero external dependencies (pure Python + Windows PowerShell)
- Open source and free

---

## Requirements

- Windows 10 or Windows 11
- Python 3.6+ (usually pre-installed or available from python.org)
- Administrator privileges (the script requests them automatically)

---

## Quick Start

### 1. Activate Protection
```bash
python child_guard.py
```
or simply double-click `child_guard.py` (it will request admin rights).

### 2. Restore Original DNS Settings
```bash
python restore_dns.py
```

---

## How It Works

The tool changes the DNS servers of your active network adapters to:

- Primary: `1.1.1.3` (Cloudflare Family – blocks malware + adult content)
- Secondary: `1.0.0.3`

Cloudflare’s Family DNS is maintained by Cloudflare and is free for personal use. No account or software installation is required beyond this script.

---

## Safety Notes

- This is a **DNS-level** filter. It is effective against most websites but is not a full parental-control suite (it does not monitor apps, block specific keywords in real time, or provide time limits).
- For stronger protection, combine it with Windows Family Safety / Microsoft Family features or a dedicated parental-control app.
- Always keep Windows and browsers updated.

---

## Project Structure

```
CSAFETYSEE/
├── child_guard.py      # Main activation script
├── restore_dns.py      # Restores DNS to automatic settings
├── README.md           # This file
└── LICENSE             # MIT License
```

---

## Future Improvements (Roadmap)

- [ ] Simple system-tray GUI
- [ ] Logging of blocked domains
- [ ] Support for Linux and macOS
- [ ] Optional hosts-file based extra blocking list
- [ ] One-click installer (.exe)

---

## License

MIT License – free to use, modify, and distribute.

---

## Author

**Cosmas Mutembei Henery Kauma**  
GitHub: [github.com/cmhk254](https://github.com/cmhk254)  
LinkedIn: [linkedin.com/in/mutembei-h-k-cosmas-b93453123](https://www.linkedin.com/in/mutembei-h-k-cosmas-b93453123/)

Built with a focus on practical child protection and online safety.
