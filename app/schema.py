import strawberry
from typing import List, Optional
from app.models import ShoppingCart, SessionLocal


@strawberry.type
class ShoppingCartType:
    id: int
    name: str
    price: float
    quantity: int
    creation_date: str
    last_update: str


@strawberry.type
class Query:
    @strawberry.field
    def shoppicarts(self) -> List[ShoppingCartType]:
        db = SessionLocal()
        items = db.query(ShoppingCart).all()
        return items


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_cart(self, name: str, price: float, quantity: int) -> ShoppingCartType:
        db = SessionLocal()
        shopping_cart = ShoppingCart(name=name, price=price, quantity=quantity)
        db.add(shopping_cart)
        db.commit()
        db.refresh(shopping_cart)
        return shopping_cart

    @strawberry.mutation
    def update_cart(self, cart_id: int, name: Optional[str] = None, price: Optional[float] = None,
                    quantity: Optional[int] = None) -> ShoppingCartType:
        db = SessionLocal()
        shopping_cart = db.query(ShoppingCart).filter(ShoppingCart.id == cart_id).first()
        if not shopping_cart:
            raise Exception("Shopping cart not found")
        if name:
            shopping_cart.name = name
        if price:
            shopping_cart.price = price
        if quantity:
            shopping_cart.quantity = quantity
        db.commit()
        db.refresh(shopping_cart)
        db.close()
        return shopping_cart

    @strawberry.mutation
    def delete_cart(self, cart_id: int) -> bool:
        db = SessionLocal()
        shopping_cart = db.query(ShoppingCart).filter(ShoppingCart.id == cart_id).first()
        if not shopping_cart:
            raise Exception("Shopping cart not found")
        db.delete(shopping_cart)
        db.commit()
        db.close()
        return True


schema = strawberry.Schema(query=Query, mutation=Mutation)
