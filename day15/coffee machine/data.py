CURRENCY = { # In $
    "quater": 0.25,
    "dime":  0.10,
    "pennie": 0.01,
    "nickle": 0.05
}
resources_available = {
    "water": 1000, # In ml
    "milk": 1000, # In ml
    "coffee": 100, # In g
    "money": 0 # In $
}
RESOURCES_REQUIRED = [
    {
        "name":'espresso',
        "water": 50,
        "coffee": 18,
        "money": 1.50,
        "milk": 0
    },
    {
        "name": 'latte',
        "water": 200,
        "coffee": 24,
        "money": 2.50,
        "milk": 100
    },
    {
        "name":'cappuchino',
        "water": 250,
        "coffee": 24,
        "money": 3.00,
        "milk": 150
    }
]
COST = {
    "espresso":1.50,
    "latte": 2.50,
    "cappuchino": 3.00
}