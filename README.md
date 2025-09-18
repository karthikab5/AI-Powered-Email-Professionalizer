# AI-Powered-Email-Professionalizer

Transform any email into a **clear, polite, and professional business message** with the power of AI.  
This project uses **CrewAI agents** + **LangChain** inside a **Streamlit app** to polish communication for workplace and academic use.

---

##  Features

✅ Rewrite informal or rough emails into professional English  
✅ Expand abbreviations inline (e.g., ASAP → *as soon as possible*)  
✅ Correct grammar, spelling, and structure automatically  
✅ Ensure respectful, business-ready tone  
✅ Add greetings and closings if missing  
✅ Easy-to-use Streamlit web app interface  

---

##  Demo Preview  

<img width="1822" height="682" alt="image" src="https://github.com/user-attachments/assets/9701bc50-3f7f-4998-aa97-2519539a6950" />

<img width="1717" height="774" alt="image" src="https://github.com/user-attachments/assets/38271d6c-44fe-42de-994d-a00bf78095d6" />

 

### Example

**Raw Email**

hey can u send me that report asap, thx

**AI-Polished Email**

Subject: Request for Report

Dear [Recipient's Name],

I hope this message finds you well.

Could you please send me the report as soon as possible? Thank you very much for your assistance.

Best regards,
[Your Name]
[Your Position]
[Your Contact Information]


---

##  Project Structure

- **Python 3.11+**
- [Streamlit](https://streamlit.io/) → User Interface  
- [CrewAI](https://www.crewai.com/) → Multi-Agent Orchestration  
- [LangChain](https://www.langchain.com/) → LLM Integrations  
- [python-dotenv](https://pypi.org/project/python-dotenv/) → Secure API Key Management  

## How It Works

- This app uses a multi-agent AI workflow:

- Email Reader Agent → Understands the input email and extracts its context.

- Email Writer Agent → Rewrites the email into a polished, professional message with expanded abbreviations.

- Agents are orchestrated via CrewAI + LangChain, making the workflow modular, interpretable, and extensible.

##  Use Cases

- Students writing professional emails to professors or recruiters

- Employees sending client communication

- Managers preparing formal business requests

- Anyone who wants to upgrade casual writing into professional tone instantly

## Future Enhancements

- Add tone customization (formal, friendly, persuasive)

- Multi-language email rewriting

- Integration with Gmail/Outlook APIs

- Slack/Teams bot integration

  
