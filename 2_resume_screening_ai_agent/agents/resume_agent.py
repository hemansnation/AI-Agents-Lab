from langchain.llms import HuggingFacePipeline
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from transformers import pipeline
from utils.pdf_utils import extract_text_from_pdf

class ResumeAgent:
    def __init__(self):
        hf_pipeline = pipeline("text-generation", model="distilgpt2", max_length=300)
        self.llm = HuggingFacePipeline(pipeline=hf_pipeline)

        self.memory = ConversationBufferMemory()
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt = PromptTemplate(
                input_variables = ['history', 'input'],
                template = "You are a resume screening assistant. Previous elavulation:\n{history}\nInput (resume and job: {input}\nAssessment:"
            )
        )

        # self.prompt = PromptTemplate(
        #     input_variables = ['resume', 'job_description'],
        #     template = "Evaluate the resume against the job description. Provide a brief assessment: \nResume: {resume}\nJob Description: {job_description}\nAssessment:",
        # )
        # self.chain = LLMChain(self.llm, self.prompt)

    def screen_resume(self, resume_text, job_description, is_pdf=False):
        if is_pdf:
            resume_text = extract_text_from_pdf(resume_text)
        else:
            resume_text = resume_text
        input_text = f"Resume: {resume_text}\nJob Description: {job_description}"
        # return self.chain.run(resume=resume_text, job_description=job_description)
        return self.conversation.predict(input=input_text)
    
if __name__ == "__main__":
    agent = ResumeAgent()
    resume_text = "software engineer with 5 years of experience in Python and Flask."
    job = "Looking for a Python Developer with 3+ years of experience."
    
    print("Text Result:", agent.screen_resume(resume_text, job))

    print("PDF Result:", agent.screen_resume("resume.pdf", job, is_pdf=True))
    
    # agent = ResumeAgent()
    # resume1 = "software engineer with 5 years of experience in Python and Flask."
    # job = "Python Developer with 3+ years of experience."
    # print("Results 1: ", agent.screen_resume(resume1, job))
    # resume2 = "junior developer with 1 year in Java"
    # print("Results 1: ", agent.screen_resume(resume2, job))
