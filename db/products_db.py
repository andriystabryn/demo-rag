"""
Mock product database for the shopping assistant
"""

PRODUCTS_DB = {
    "laptop": {
        "id": 1,
        "name": "Professional Laptop",
        "price": 1299.99,
        "currency": "USD",
        "in_stock": True,
        "quantity": 15,
        "description": "High-performance laptop with 16GB RAM, 512GB SSD, Intel i7 processor",
        "category": "Electronics",
        "specs": {
            "ram": "16GB",
            "storage": "512GB SSD",
            "processor": "Intel i7",
            "screen": "15.6 inch"
        }
    },
    "iphone_16_pro": {
        "id": 2,
        "name": "iPhone 16 Pro",
        "price": 999.99,
        "currency": "USD",
        "in_stock": True,
        "quantity": 42,
        "description": "Latest iPhone 16 Pro with 5G, 128GB storage, triple camera system",
        "category": "Electronics",
        "specs": {
            "storage": "128GB",
            "camera": "Triple 48MP",
            "battery": "4500mAh",
            "network": "5G"
        }
    },
    "headphones": {
        "id": 3,
        "name": "Wireless Headphones",
        "price": 249.99,
        "currency": "USD",
        "in_stock": False,
        "quantity": 0,
        "description": "Noise-cancelling wireless headphones with 30-hour battery life",
        "category": "Audio",
        "specs": {
            "battery_life": "30 hours",
            "noise_cancelling": True,
            "wireless": True,
            "bluetooth": "5.0"
        }
    },
    "iphone_15_pro": {
        "id": 4,
        "name": "iPhone 15 Pro",
        "price": 899.99,
        "currency": "USD",
        "in_stock": True,
        "quantity": 28,
        "description": "Latest iPhone 15 Pro with A17 Pro chip, titanium design, and advanced camera system",
        "category": "Smartphones",
        "specs": {
            "storage": "256GB",
            "chip": "A17 Pro",
            "camera": "48MP Main + 12MP Ultra Wide + 12MP Telephoto",
            "display": "6.1-inch Super Retina XDR",
            "material": "Titanium",
            "5g": True
        }
    },
    "iphone_15": {
        "id": 5,
        "name": "iPhone 15",
        "price": 799.99,
        "currency": "USD",
        "in_stock": True,
        "quantity": 45,
        "description": "iPhone 15 with Dynamic Island, 48MP camera, and all-day battery life",
        "category": "Smartphones",
        "specs": {
            "storage": "128GB",
            "chip": "A16 Bionic",
            "camera": "48MP Main + 12MP Ultra Wide",
            "display": "6.1-inch Super Retina XDR",
            "material": "Aluminum and glass",
            "5g": True
        }
    },
    "iphone_14": {
        "id": 6,
        "name": "iPhone 14",
        "price": 699.99,
        "currency": "USD",
        "in_stock": True,
        "quantity": 12,
        "description": "iPhone 14 with advanced dual-camera system and emergency SOS via satellite",
        "category": "Smartphones",
        "specs": {
            "storage": "128GB",
            "chip": "A15 Bionic",
            "camera": "12MP Main + 12MP Ultra Wide",
            "display": "6.1-inch Super Retina XDR",
            "material": "Aluminum and glass",
            "5g": True
        }
    }
}
