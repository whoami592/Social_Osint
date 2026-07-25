# Social_Osint

<img width="1536" height="1024" alt="social osint" src="https://github.com/user-attachments/assets/5ed5e0f0-11a6-4d6d-8752-bd8d31e7041e" />

# 🔎 Social Media OSINT Tool

**Social Media OSINT Tool** is a Python-based Open Source Intelligence (OSINT) utility designed to help security researchers and students organize public social-media username investigations.

> **Coded by Mr Sabaz Ali Khan**

## ✨ Features

* 🔎 Generate public profile URL candidates from a username
* 🌐 Supports multiple platforms:

  * GitHub
  * Reddit
  * X
  * Instagram
  * TikTok
  * YouTube
* 🗄️ Store investigation results in a local SQLite database
* 📊 Display collected candidates in a GUI table
* 📄 Export results to CSV
* 📦 Export results to JSON
* 🖥️ Simple Python Tkinter GUI
* 🔄 Refresh saved investigation results

## 🛠️ Technology

* Python 3
* Tkinter
* SQLite3
* CSV
* JSON
* urllib

## 📂 Project Structure

```text
social-media-osint-tool/
│
├── main.py              # Main GUI application
├── database.py          # SQLite database operations
├── osint_search.py      # Public profile URL generation
├── report.py            # CSV/JSON report generation
├── README.md            # Project documentation
├── LICENSE              # License
└── banner.png           # GitHub project banner
```

## 🚀 Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Enter the project directory:

```bash
cd social-media-osint-tool
```

Run the application:

```bash
python main.py
```

## ▶️ How to Use

1. Start the application with `python main.py`.
2. Enter a **public username**.
3. Click **Generate Profiles**.
4. The tool generates candidate profile URLs for supported platforms.
5. Results are saved locally in the SQLite database.
6. Use **Export CSV** or **Export JSON** to create reports.
7. Use **Refresh** to reload saved results.

## 📊 Supported Platforms

| Platform  | Profile Pattern            |
| --------- | -------------------------- |
| GitHub    | `github.com/username`      |
| Reddit    | `reddit.com/user/username` |
| X         | `x.com/username`           |
| Instagram | `instagram.com/username`   |
| TikTok    | `tiktok.com/@username`     |
| YouTube   | `youtube.com/@username`    |

## 📄 Reports

The application can export investigation records into:

```text
osint_report.csv
osint_report.json
```

The database stores the username, platform, profile URL, notes and creation timestamp.

## 🔐 Ethical Use

This project is intended for:

* Cybersecurity education
* OSINT learning
* Authorized security research
* Public-information investigation
* Security laboratory/testing environments

**Important:** The generated URLs are profile candidates. A generated URL does not prove that the account exists or belongs to a particular person.

Do not use this tool for harassment, stalking, unauthorized surveillance, privacy violations, or other unlawful activity. Only investigate information you are legally permitted to access.

## 👨‍💻 Author

**Mr Sabaz Ali Khan**

Python & Cybersecurity Project

## ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐛 Report bugs
* 💡 Suggest improvements

## 🏷️ Topics

```text
python
osint
cybersecurity
social-media-osint
information-gathering
ethical-hacking
security-research
sqlite
tkinter
digital-investigation
```

---

**Social Media OSINT Tool — Coded by Mr Sabaz Ali Khan**



