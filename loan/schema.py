from ninja import ModelSchema
from .models import Loan


class LoanSchema(ModelSchema):
    class Config:
        model = Loan
        model_fields = '__all__'