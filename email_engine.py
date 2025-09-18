# and the crewai and langchain libraries are installed.
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = LLM(
    model="gpt-4o-mini",
    temperature=0.3,
    api_key=OPENAI_API_KEY,
)



# ---------------------------
# Agents
# ---------------------------
reader = Agent(
    role="Email Reader",
    goal="Crefully go through the key points of the email and identify the context",
    backstory="You quickly understand emails and highlight what matters.",
    llm=llm
)

writer = Agent(
    role="Email Writer",
    goal=("Rewrite emails to be clear, polite, and highly professional. "
          "Preserve original intent, correct grammar and tone, and expand "
          "all abbreviations and slang into formal, standard English."),
    backstory="You are an expert in business communication and etiquette.",
    llm=llm
)

# ---------------------------
# Functions for Streamlit app
# ---------------------------

def summarize_email(email_text: str) -> str:
    """
    Rewrites the provided email into a formal, polite version and expands abbreviations.
    """
    task = Task(
        description=(
            "Rewrite the email below into a clear, polite, and highly professional message. "
            "Keep the original meaning, but fix grammar, spelling, and structure. "
            "Remove slang. Expand ALL abbreviations and acronyms in-line the first time "
            "they appear (e.g., 'ASAP' -> 'as soon as possible'). "
            "Use concise, respectful language. "
            "If the original lacks a greeting or closing, add appropriate ones. "
            "Avoid adding facts that aren't present.\n\n"
            f"--- ORIGINAL EMAIL ---\n{email_text}\n"
            "----------------------\n"
            "Output only the final polished email (no explanations)."
        ),
        agent=writer,
        expected_output="A single polished, professional email with expanded abbreviations."
    )
    crew = Crew(agents=[reader], tasks=[task], verbose=False)
    
    result = crew.kickoff()
    return str(result)

