"""
Script to populate the database with sample products.
Run with: python manage.py shell < populate_db.py
"""

from shop.models import Product

products = [
    {
        "name": "Wireless Headphones",
        "description": "Premium noise-cancelling wireless headphones with 30-hour battery life.",
        "price": 199.99,
        "image_url": "https://via.placeholder.com/300?text=Headphones",
    },
    {
        "name": "USB-C Cable",
        "description": "Durable 6ft USB-C charging and data cable. Works with all USB-C devices.",
        "price": 12.99,
        "image_url": "https://via.placeholder.com/300?text=USB-C+Cable",
    },
    {
        "name": "Portable Charger",
        "description": "20000mAh portable power bank with fast charging support.",
        "price": 34.99,
        "image_url": "https://via.placeholder.com/300?text=Charger",
    },
    {
        "name": "Mechanical Keyboard",
        "description": "RGB mechanical keyboard with custom switches and programmable keys.",
        "price": 129.99,
        "image_url": "https://via.placeholder.com/300?text=Keyboard",
    },
    {
        "name": "4K Webcam",
        "description": "Ultra HD 4K webcam with auto-focus and built-in microphone.",
        "price": 89.99,
        "image_url": "https://via.placeholder.com/300?text=Webcam",
    },
    {
        "name": "Laptop Stand",
        "description": "Adjustable aluminum laptop stand for better ergonomics.",
        "price": 39.99,
        "image_url": "https://via.placeholder.com/300?text=Laptop+Stand",
    },
]

for p in products:
    Product.objects.get_or_create(
        name=p["name"],
        defaults={
            "description": p["description"],
            "price": p["price"],
            "image_url": p["image_url"],
        }
    )

print(f"✓ Created {len(products)} sample products!")
