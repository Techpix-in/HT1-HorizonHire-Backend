from pydantic import BaseModel, Field
from typing import List,Optional

class JobSearchModel(BaseModel):
    """Schema for job posting data"""
    # I have to include company name here, or company details..
    company_name : str = Field(description="name of the company",default=None)
    region: str = Field(description="Region or area where the job is located", default=None)
    role: str = Field(description="Specific role or function within the job category", default=None)
    job_title: str = Field(description="Title of the job position", default=None)
    experience: str = Field(description="Number of work experience required for the position", default=None)
    job_link: str = Field(description="Website link of the job posting", default=None)


class ExtractSchema(BaseModel):
    """Schema for job postings extraction"""
    job_postings: List[JobSearchModel] = Field(description="List of job postings")

class JobRequirements(BaseModel):
    """Schema extracted from the pdf"""
    job_title: str
    skills: List[str]
    experience: Optional[int] = 5
    location: Optional[str] = "Banglore"
    remote_only: Optional[bool] = False
