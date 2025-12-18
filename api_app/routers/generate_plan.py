from fastapi import APIRouter, HTTPException ,Depends
from ..schemas.generate_plan_schema import generateRequest ,generateResponse



router = APIRouter()


@router.post('/generate-retention-plan')
async def generate_plan(request : generateRequest):

    

    return