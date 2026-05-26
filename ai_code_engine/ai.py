from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class AIEngine:

    @staticmethod
    def clean_code(code):

        if not code:
            return ""

        return (
            code
            .replace("```python", "")
            .replace("```", "")
            .strip()
        )

    @staticmethod
    def analyze(code):

        prompt = f"""
You are an elite Python optimizer.

STRICT RULES:
- Return ONLY raw JSON
- NEVER use markdown
- optimized_code MUST be optimized
- Replace manual summation loops with sum()
- Replace inefficient loops
- Keep same behavior/output

JSON FORMAT:
{{
    "fixed_code": "",
    "optimized_code": "",
    "issues": [],
    "suggestions": [],
    "severity": "LOW"
}}

CODE:
{code}
"""

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                temperature=0.0,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You ONLY return raw JSON."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            content = (
                response
                .choices[0]
                .message
                .content
                .strip()
            )

            print("\n====== RAW AI RESPONSE ======")
            print(content)
            print("=============================\n")

            content = (
                content
                .replace("```json", "")
                .replace("```python", "")
                .replace("```", "")
                .strip()
            )

            data = json.loads(content)

            optimized = AIEngine.clean_code(
                data.get("optimized_code", code)
            )

            fixed = AIEngine.clean_code(
                data.get("fixed_code", code)
            )

            return {
                "fixed_code": fixed,
                "optimized_code": optimized,
                "issues": data.get("issues", []),
                "suggestions": data.get("suggestions", []),
                "severity": data.get("severity", "LOW")
            }

        except Exception as e:

            print("AI ERROR:", e)

            return {
                "fixed_code": code,
                "optimized_code": code,
                "issues": [str(e)],
                "suggestions": [],
                "severity": "ERROR"
            }