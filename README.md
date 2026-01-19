# 🤖 AI-Powered Code Auditor & Security Guard

An automated, end-to-end code review and security auditing system designed for modern CI/CD pipelines. This tool combines deterministic **Static Application Security Testing (SAST)** with probabilistic **Generative AI** to provide deep architectural and security insights for every Pull Request.

---

## 🏗️ System Architecture

The auditor operates as a multi-stage pipeline within a GitHub Actions environment:

1.  **Extraction Layer**: Utilizes Git subprocesses to isolate changed code blocks (`git diff`) between the feature branch and the base branch.
2.  **Deterministic Layer (SAST)**: Runs **Bandit** and **Pylint** to identify common security vulnerabilities (e.g., hardcoded secrets, SQL injection) and PEP8 compliance issues.
3.  **Intelligence Layer (LLM)**: Contextualizes the code changes and sends them to a fine-tuned **OpenAI GPT-4o** model to identify logic flaws, scalability bottlenecks, and cloud-native anti-patterns.
4.  **Reporting Layer**: Aggregates findings into a structured Markdown report and posts it as a developer-friendly comment directly on the Pull Request.



---

## 🛠️ Features

* **Automated PR Auditing**: Automatically triggers on `pull_request` events to ensure no code goes unreviewed.
* **Security-First Logic**: Specifically scans for vulnerabilities using **Bandit**, a tool designed for security-oriented static analysis.
* **Production-Ready Logging**: Implements structured logging for observability, mirroring patterns used in enterprise cloud-native monitoring.
* **Mock-Driven Testing**: Includes a full **pytest** suite with extensive mocking of the **OpenAI API** and **Git CLI** to ensure 100% test coverage without external dependencies.

---

## 🚀 Tech Stack

* **Language**: Python 3.12
* **AI Integration**: OpenAI SDK v1.0+
* **Static Analysis**: Bandit, Pylint
* **CI/CD**: GitHub Actions
* **Testing**: Pytest, Unittest.mock

---

## 🔧 Installation & Local Usage

### Prerequisites
* Python 3.12+
* An OpenAI API Key

### Setup
```bash
# Clone the repository
git clone [https://github.com/your-username/ai-code-auditor.git](https://github.com/your-username/ai-code-auditor.git)
cd ai-code-auditor

# Create a Virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run local audit (requires OPENAI_API_KEY env variable)
python auditor/core.py