import html
import unicodedata

def sanitize_name(name):
    """Sanitize name input to handle special characters safely"""
    if not name:
        return "Guest"
    
    # Remove control characters
    name = ''.join(char for char in name if unicodedata.category(char)[0] != 'C')
    
    # Normalize unicode
    name = unicodedata.normalize('NFKD', name)
    
    # HTML escape for safety
    name = html.escape(name.strip())
    
    # Limit length
    if len(name) > 50:
        name = name[:50] + "..."
    
    return name or "Guest"