import re

def validate_name(name):
    """Validate name parameter"""
    if not name or len(name.strip()) == 0:
        return False, "Name cannot be empty"
    
    if len(name) > 50:
        return False, "Name too long (max 50 characters)"
    
    # Allow letters, numbers, spaces, hyphens, underscores
    if not re.match(r'^[a-zA-Z0-9\s\-_]+$', name):
        return False, "Name contains invalid characters"
    
    return True, None