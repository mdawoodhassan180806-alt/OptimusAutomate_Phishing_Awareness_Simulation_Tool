# 🛡️ Phishing Awareness Simulation Tool

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Purpose](https://img.shields.io/badge/Purpose-Educational-success.svg)

> **An educational desktop application that helps users recognize phishing attacks through simulated emails, URL analysis, interactive quizzes, and performance tracking. This project is designed strictly for cybersecurity awareness and training.**

---

# 📑 Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [System Architecture](#system-architecture)
- [Application Workflow](#application-workflow)
- [Installation Guide](#installation-guide)
- [How to Run](#how-to-run)
- [Application Modules](#application-modules)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Ethical Considerations](#ethical-considerations)
- [License](#license)

---

# 📖 Project Overview

Phishing is one of the most common cyberattacks used to steal usernames, passwords, financial information, and other sensitive data. Attackers often impersonate trusted organizations and use social engineering techniques to trick users into revealing confidential information.

The **Phishing Awareness Simulation Tool** is an educational desktop application developed using **Python** and **Tkinter**. It provides realistic but completely safe phishing email simulations, analyzes suspicious URLs, and tests users through an interactive quiz.

The application is designed to improve cybersecurity awareness among students, employees, and anyone interested in learning how to recognize phishing attacks.

> **This application is strictly educational. It does not send emails, collect credentials, or perform any real phishing activity.**

---

# ❗ Problem Statement

Many users are unable to distinguish between legitimate emails and phishing attempts. Cybercriminals exploit this lack of awareness through:

- Fake login pages
- Urgent security alerts
- Password reset scams
- Lottery and prize scams
- Fake banking notifications
- Social engineering attacks

Organizations require a safe and interactive training tool to educate users on identifying these threats without exposing them to actual attacks.

---

# 🎯 Objectives

The objectives of this project are:

- Educate users about phishing attacks.
- Demonstrate common phishing techniques.
- Explain phishing indicators and warning signs.
- Improve cybersecurity awareness.
- Assess user knowledge using an interactive quiz.
- Track learning progress and quiz performance.
- Provide a safe environment for cybersecurity training.

---

# ✨ Features

## 📧 Educational Phishing Examples

- Displays realistic phishing emails.
- Highlights suspicious content.
- Explains phishing indicators.
- Calculates a phishing risk score.

---

## 🎲 Random Phishing Email Generator

Generates random educational phishing email examples using different:

- Sender names
- Subjects
- Messages
- Suspicious URLs

Each generated email is safe and intended for awareness training only.

---

## 🌐 URL Analyzer

The URL Analyzer helps users identify suspicious URLs by checking for:

- `@` symbol usage
- Suspicious hyphens
- "login" keywords
- "verify" keywords
- "secure" keywords

Example:

```
https://secure-login-bank.verify-account.com
```

Output:

```
Contains login keyword
Contains verify keyword
Uses secure keyword
Contains suspicious hyphens
```

---

## 📝 Interactive Quiz

The application includes a phishing awareness quiz.

Features:

- Multiple educational questions
- Immediate feedback
- Detailed explanations
- Progress tracking
- Final score calculation

---

## 📊 Statistics Dashboard

Tracks:

- Correct answers
- Incorrect answers
- Overall accuracy
- Quiz performance

---

## 💾 CSV Report Export

Quiz results are automatically saved into:

```
quiz_results.csv
```

Example:

```
2026-06-27 10:15:33,5,5
2026-06-27 10:20:51,4,5
```

---

## 🌙 Dark Theme GUI

The application includes a modern dark-themed interface for improved readability.

---

# 💻 Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python 3.x |
| GUI Framework | Tkinter |
| Data Storage | CSV |
| Date Handling | datetime |
| Randomization | random |

---

# 📂 Project Structure

```
Phishing-Awareness-Simulation-Tool/
│
├── phishing_awareness_tool.py
├── README.md
├── LICENSE
├── requirements.txt
└── quiz_results.csv (generated automatically)
```

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
        Tkinter Graphical Interface
                  │
                  ▼
        -------------------------
        | Application Logic      |
        -------------------------
        | Examples Module        |
        | Random Generator       |
        | URL Analyzer           |
        | Quiz Engine            |
        | Statistics Module      |
        | CSV Export Module      |
        -------------------------
                  │
                  ▼
            CSV File Storage
```

---

# 🔄 Application Workflow

```
Start Application
        │
        ▼
Open GUI
        │
        ▼
────────────────────────────
│ View Phishing Examples    │
────────────────────────────
        │
        ▼
Generate Random Emails
        │
        ▼
Analyze Suspicious URLs
        │
        ▼
Take Awareness Quiz
        │
        ▼
View Statistics
        │
        ▼
Export Results
        │
        ▼
Exit
```

---

# ⚙️ Installation Guide

## Step 1

Install Python 3.x

Download from:

https://www.python.org

Verify installation:

```bash
python --version
```

---

## Step 2

Clone the repository

```bash
git clone https://github.com/yourusername/Phishing-Awareness-Simulation-Tool.git
```

---

## Step 3

Navigate into the project

```bash
cd Phishing-Awareness-Simulation-Tool
```

---

## Step 4

Run the application

Windows

```bash
python phishing_awareness_tool.py
```

Linux/macOS

```bash
python3 phishing_awareness_tool.py
```

---

# 🚀 How to Use

### Examples Tab

- Read simulated phishing emails.
- Learn phishing warning signs.
- Review phishing risk scores.

---

### Generator Tab

Generate random phishing email examples.

---

### URL Analyzer

Enter any URL.

Example:

```
https://secure-login-bank.verify-account.com
```

View detected phishing indicators.

---

### Quiz Tab

Take the phishing awareness quiz.

Receive:

- Instant feedback
- Educational explanations
- Final score

---

### Statistics Tab

View:

- Correct answers
- Incorrect answers
- Accuracy percentage

---

# 🧩 Application Modules

## 1. Examples Module

Displays realistic phishing emails with explanations and phishing indicators.

---

## 2. Random Generator Module

Creates random phishing scenarios for training purposes.

---

## 3. URL Analyzer Module

Detects suspicious characteristics commonly used in phishing URLs.

---

## 4. Quiz Module

Tests user knowledge using educational phishing questions.

---

## 5. Statistics Module

Calculates:

- Accuracy
- Correct answers
- Incorrect answers

---

## 6. CSV Export Module

Automatically saves quiz results for future review.

---

# 📸 Screenshots

Add screenshots here after running the application.

Example:

```
screenshots/

home.png

examples.png

generator.png

url_analyzer.png

quiz.png

statistics.png
```

Example markdown:

```markdown
## Home Screen

![Home](screenshots/home.png)

## Quiz

![Quiz](screenshots/quiz.png)
```

---

# 📚 Learning Outcomes

After using this application, users should be able to:

- Identify phishing emails.
- Recognize suspicious URLs.
- Detect urgency-based attacks.
- Understand impersonation techniques.
- Identify credential theft attempts.
- Recognize common social engineering tactics.
- Improve overall cybersecurity awareness.

---

# 🔮 Future Enhancements

Possible future improvements include:

- PDF report generation
- Difficulty levels
- User accounts
- Leaderboard
- Email header analysis
- Domain reputation lookup
- WHOIS information lookup
- Machine learning phishing detection
- Multi-language support
- Cloud database integration

---

# 🔒 Ethical Considerations

This project is designed **strictly for educational purposes**.

The application:

- ✅ Simulates phishing emails safely
- ✅ Teaches phishing awareness
- ✅ Improves cybersecurity knowledge

The application **does NOT**:

- Send emails
- Collect passwords
- Clone websites
- Capture credentials
- Host phishing pages
- Perform phishing attacks
- Access personal information
- Conduct offensive cybersecurity activities

All phishing examples are simulated and intended solely for awareness training.

---

# 🤝 Contributing

Contributions are welcome.

You can contribute by:

- Improving the GUI
- Adding more phishing scenarios
- Enhancing the quiz
- Improving documentation
- Reporting bugs
- Suggesting new educational features

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this project for educational and non-commercial purposes.

---

# 👨‍💻 Author

**Project:** Phishing Awareness Simulation Tool

**Purpose:** Cybersecurity Awareness & Education

**Language:** Python

**GUI:** Tkinter

**Project Type:** Educational Desktop Application

---

# ⭐ Acknowledgements

This project was created to promote cybersecurity awareness and help users recognize phishing attempts in a safe and controlled environment.

If you found this project helpful, consider giving it a ⭐ on GitHub!# OptimusAutomate_Phishing_Awareness_Simulation_Tool
