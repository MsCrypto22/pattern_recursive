# Test the function
#print(is_match("adceb", "*a*b"))  # Output: True  
def is_match(text, pattern):
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '?'}
    
    if pattern[0] == '*':
        return (is_match(text, pattern[1:]) or 
                bool(text) and is_match(text[1:], pattern))
    else:
        return first_match and is_match(text[1:], pattern[1:])
