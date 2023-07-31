from ninja import NinjaAPI
from book.api import router as book_router
from user.api import router as user_router


api = NinjaAPI()


api.add_router('bibliotech/', book_router)
api.add_router('bibliotech/', user_router)