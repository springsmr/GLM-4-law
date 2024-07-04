from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool

from services.sub_company_info_service import *


class CompanyNameInput(BaseModel):
    company_name: str = Field(description="公司名称")


class KeyValueInput(BaseModel):
    key: str = Field(description="键")
    value: str = Field(description="值")


parent_company_info_getter = StructuredTool.from_function(
    func=get_parent_company_info_service,
    name="parent_company_info_getter",
    args_schema=CompanyNameInput,
)

sub_company_name_getter = StructuredTool.from_function(
    func=get_sub_company_name_service,
    name="sub_company_name_getter",
    args_schema=CompanyNameInput,
)

sub_company_info_getter = StructuredTool.from_function(
    func=get_sub_company_info_service,
    name="sub_company_info_getter",
    args_schema=CompanyNameInput,
)

all_sub_company_counter = StructuredTool.from_function(
    func=count_sub_company_service,
    name="all_sub_company_counter",
    args_schema=CompanyNameInput,
)

company_name_retriever_by_super_info = StructuredTool.from_function(
    func=search_company_name_by_super_info_service,
    name="company_name_retriever_by_super_info",
    args_schema=KeyValueInput,
)

total_amount_invested_in_subsidiaries_getter = StructuredTool.from_function(
    func=query_total_amount_invested_in_subsidiaries,
    name="total_amount_invested_in_subsidiaries_getter",
    args_schema=CompanyNameInput,
)

sub_com_info_tools = [
    parent_company_info_getter,
    sub_company_name_getter,
    sub_company_info_getter,
    all_sub_company_counter,
    company_name_retriever_by_super_info,
    total_amount_invested_in_subsidiaries_getter
]
