MAPS = {
    "default": {
        "start": "entrance",
        "goal": "vault",
        "rooms": {
            "entrance": {
                "name": "Bank Entrance",
                "description": "A grand marble entrance hall with a red carpet. Security cameras line the walls. Corridors lead east and north.",
                "exits": {"east": "office"},
                "doors": {
                    "north": {
                        "id": "vault_door",
                        "locked": True,
                        "key_id": "vault_key",
                        "leads_to": "vault"
                    }
                },
                "items": []
            },
            "office": {
                "name": "Bank Office",
                "description": "Rows of empty desks. Papers scattered everywhere. A vault key card sits on the managers desk.",
                "exits": {"west": "entrance", "south": "basement"},
                "doors": {},
                "items": [
                    {"name": "vault key card", "id": "vault_key"}
                ]
            },
            "basement": {
                "name": "Bank Basement",
                "description": "A dark damp basement. Filing cabinets line the walls. Smells of old money.",
                "exits": {"north": "office"},
                "doors": {},
                "items": []
            },
            "vault": {
                "name": "The Vault",
                "description": "Stacks of cash and gold bars everywhere. You have cracked the bank. Mission complete!",
                "exits": {},
                "doors": {},
                "items": []
            }
        }
    }
}