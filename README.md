# Advanced Python Automation Framework 🚀

A professional-grade automation project demonstrating Full-Stack QA capabilities, including UI and API testing using **Playwright**, **Pytest**, and **GitHub Actions**.

---

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **UI Automation:** Playwright (Page Object Model)
* **API Testing:** Requests
* **Test Runner:** Pytest
* **Reporting:** Pytest-HTML with automatic failure screenshots
* **CI/CD:** GitHub Actions

---

## ✨ Key Features
* **Page Object Model (POM):** Clean separation between test logic and UI elements.
* **API Integration:** Backend verification for user and post management.
* **Data-Driven Testing:** Using `@pytest.mark.parametrize` for efficient test coverage.
* **CI/CD Pipeline:** Automated test execution on every push via GitHub Actions.
* **Advanced Reporting:** Detailed HTML reports with embedded screenshots upon test failure.

---

## 🚀 Getting Started: Setup & Execution

```bash
# 1. Clone the repo
git clone [https://github.com/DudiMonsonego/automation-portfolio.git](https://github.com/DudiMonsonego/automation-portfolio.git)
cd automation-portfolio

# 2. Install dependencies
pip install -r requirements.txt
playwright install

# 3. Execute tests and generate report
python -m pytest --html=reports/report.html --self-contained-html


הקובץ נראה מצוין ב-VS Code, אבל הבעיה היא שלפי ה-Screenshot האחרון שלך, חסר "תיחום" (Fencing). ב-Markdown, כדי שגיטהאב יציג קטעי קוד או מבנה תיקיות בתוך תיבה אפורה ויפה, צריך לעטוף אותם בסימנים מיוחדים.

הנה מה שחסר לך כדי שה-README יפסיק להיראות כמו "טקסט רגיל" ויהפוך למקצועי:

1. מה להוסיף (התיקון)
מתחת לכותרת ## 🚀 Getting Started, אתה צריך לעטוף את הפקודות ב-3 גרשיים הפוכים (backticks). אותו דבר לגבי מבנה התיקיות.

פשוט תעתיק את כל הטקסט הבא ותחליף את כל מה שיש לך ב-README.md:

Markdown
# Advanced Python Automation Framework 🚀

A professional-grade automation project demonstrating Full-Stack QA capabilities, including UI and API testing using **Playwright**, **Pytest**, and **GitHub Actions**.

---

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **UI Automation:** Playwright (Page Object Model)
* **API Testing:** Requests
* **Test Runner:** Pytest
* **Reporting:** Pytest-HTML with automatic failure screenshots
* **CI/CD:** GitHub Actions

---

## ✨ Key Features
* **Page Object Model (POM):** Clean separation between test logic and UI elements.
* **API Integration:** Backend verification for user and post management.
* **Data-Driven Testing:** Using `@pytest.mark.parametrize` for efficient test coverage.
* **CI/CD Pipeline:** Automated test execution on every push via GitHub Actions.
* **Advanced Reporting:** Detailed HTML reports with embedded screenshots upon test failure.

---

## 🚀 Getting Started: Setup & Execution

```bash
# 1. Clone the repo
git clone [https://github.com/DudiMonsonego/automation-portfolio.git](https://github.com/DudiMonsonego/automation-portfolio.git)
cd automation-portfolio

# 2. Install dependencies
pip install -r requirements.txt
playwright install

# 3. Execute tests and generate report
python -m pytest --html=reports/report.html --self-contained-html


📊 Project Structure & Files
 automation-portfolio/
├── .github/workflows/      # CI/CD pipeline configuration (GitHub Actions)
├── pages/                  # Page Object Model classes (UI Logic)
│   ├── login_page.py
│   └── inventory_page.py
├── tests/                  # Test suites
│   ├── test_ui.py          # UI tests with Playwright
│   └── test_api.py         # API tests with Requests
├── reports/                # Test reports and screenshots
├── conftest.py             # Global fixtures and hooks (Screenshots on failure)
├── pytest.ini              # Pytest configuration
└── requirements.txt        # Project dependencies