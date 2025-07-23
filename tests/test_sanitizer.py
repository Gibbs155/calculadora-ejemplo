def test_special_characters():
    """Test handling of special characters"""
    test_cases = [
        ("José", "José"),
        ("<script>alert('xss')</script>", "&lt;script&gt;alert('xss')&lt;/script&gt;"),
        ("", "Guest"),
        (None, "Guest"),
        ("A" * 60, "A" * 50 + "...")
    ]
    
    for input_name, expected in test_cases:
        result = sanitize_name(input_name)
        assert result == expected, f"Failed for input: {input_name}"