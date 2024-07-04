from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool

from services.company_register_service import *


class CompanyNameInput(BaseModel):
    company_name: str = Field(description="公司名称")


class IndustryNameInput(BaseModel):
    industry_name: str = Field(description="行业名称")


class RegistrationNumberInput(BaseModel):
    registration_number: str = Field(description="注册号")


class KeyValueInput(BaseModel):
    key: str = Field(description="键")
    value: str = Field(description="值")


company_register_getter = StructuredTool.from_function(
    func=get_company_register_service,
    name="company_register_getter",
    args_schema=CompanyNameInput,
)

company_name_retriever_by_register_number = StructuredTool.from_function(
    func=search_company_name_by_registration_number_service,
    name="company_name_retriever_by_register_number",
    args_schema=RegistrationNumberInput,
)

company_name_retriever_by_register = StructuredTool.from_function(
    func=search_company_name_by_register_service,
    name="company_name_retriever_by_register",
    args_schema=KeyValueInput,
)

cnr_retriever_by_industry = StructuredTool.from_function(
    func=search_cnr_by_industry_service,
    name="cnr_retriever_by_industry",
    args_schema=IndustryNameInput,
)

com_register_tools = [
    company_register_getter,
    company_name_retriever_by_register_number,
    company_name_retriever_by_register,
    cnr_retriever_by_industry,
]
