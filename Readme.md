# 🕵️ CASCADE Internal Breach — CTF Machine

## 📌 Description

A realistic web exploitation lab simulating a full attack chain from reconnaissance to root access.

Designed in HTB/VulnHub style for hands-on practice.

---

## 🎯 Objective

Compromise the system and capture all flags.

---

## 🚀 Setup

```bash
git clone <CASCADE-INTERNAL-BREACH-CTF>
cd ctf-machine
docker-compose up --build -d
```

Access:

```
http://localhost:8080
```

---

## 🧩 Difficulty

Easy → Medium

---

## 🔗 Attack Path Overview

1. JS Enumeration
2. IDOR Exploitation
3. Internal API Discovery
4. Remote Code Execution
5. Reverse Shell
6. Privilege Escalation

---

## 🏁 Flags

* FLAG{entry_point_compromised}
* FLAG{devs_are_lazy}
* FLAG{user_shell_obtained}
* FLAG{root_dominion}

---

## 🐇 Rabbit Holes

* `/admin` endpoint (misleading credentials)

---

## 🛠 Technologies

* Flask (Python)
* Docker
* Linux Privilege Escalation

---

## 👤 Author

Parvathy P Joshy
Cybersecurity Enthusiast | Offensive Security

---

## ⚠️ Disclaimer

This project is created for educational purposes only.

