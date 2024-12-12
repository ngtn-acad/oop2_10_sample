from models import Food
from peewee import fn

def most_eaten_ranking():
    eaten_ranking = (
        Food
        .select(Food.food, Food.restaurant, fn.COUNT(Food.id).alias("total"))
        .group_by(Food.food,Food.restaurant)
        .order_by(fn.COUNT(Food.food).desc())
        .limit(5)
    )

    result =[]
    for food in eaten_ranking:
        result.append(
            {
                "food" : food.food,
                "restaurant" : food.restaurant.name,
                "eaten_num" : food.total,
            }
        )

    return result