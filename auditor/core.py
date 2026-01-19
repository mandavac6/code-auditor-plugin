import os
import subprocess
import logging
from openai import OpenAI

# Initialize Logging based on your observability experience [cite: 79, 155]
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class CodeAuditor:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.target_branch = os.getenv("GITHUB_BASE_REF", "main")

    def get_diff(self):
        """Extracts git diff for the PR branch[cite: 10]."""
        try:
            # Fetch base branch to ensure diff is available in CI [cite: 43]
            subprocess.run(["git", "fetch", "origin", self.target_branch], check=True)
            diff = subprocess.check_output(
                ["git", "diff", f"origin/{self.target_branch}...HEAD"], 
                text=True
            )
            return diff
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to fetch git diff: {e}")
            return None

    def analyze_code(self, diff):
        """Sends diff to GPT-4o for a Senior-level audit[cite: 35, 140]."""
        if not diff:
            return "No changes detected or error fetching diff."

        prompt = f"""
        Act as a Senior Python Security Engineer. Audit this code diff for:
        1. OWASP Top 10 vulnerabilities (Injection, Broken Access Control).
        2. Performance (Pandas vectorization, memory leaks)[cite: 81, 141].
        3. Scalability (AWS/Cloud-native best practices)[cite: 59, 101].
        
        Provide feedback in Markdown format with 'Severity: High/Med/Low'.
        
        DIFF:
        {diff}
        """

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": "You are a world-class code auditor."},
                          {"role": "user", "content": prompt}],
                temperature=0.2
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI API Error: {e}")
            return f"Audit failed due to API error: {e}"

if __name__ == "__main__":
    auditor = CodeAuditor()
    changes = auditor.get_diff()
    report = auditor.analyze_code(changes)
    
    # Save report for GitHub Action to consume [cite: 82]
    with open("ai_feedback.md", "w") as f:
        f.write("### 🤖 AI Code Audit Report\n\n")
        f.write(report)