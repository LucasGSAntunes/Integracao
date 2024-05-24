from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.domain.use_cases.lead_use_case import LeadUseCase
from src.app.fastapi_api.docs.LeadModel import LeadModel

lead_router = APIRouter(prefix="/lead", tags=["Lead"])

@lead_router.post("", response_model=LeadModel)
def create_lead(lead_data: LeadModel):
    response = LeadUseCase().create_lead(
        lead_data.name,
        lead_data.phone,
        lead_data.area,
        lead_data.id,
        lead_data.pergunta
    )
    
    status_code_by_response = {
        "success": status.HTTP_201_CREATED,
        "error": status.HTTP_400_BAD_REQUEST,
    }

    status_code = status_code_by_response.get(response.get("message"), status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content=response, status_code=status_code)

    