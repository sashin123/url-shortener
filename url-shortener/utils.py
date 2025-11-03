"""
URL Shortener - Utility Functions
Helper functions for URL generation and validation
"""

import hashlib
import string
from urllib.parse import urlparse


def generate_short_code(url, length=7):
    """
    Generate a short code from a URL using hash
    
    Args:
        url: The URL to generate code for
        length: Length of the short code
    
    Returns:
        A short code string

    How it works:

    1. Creates an MD5 hash of the URL (converts URL to a unique number)

    2. Converts that number to base62 using base62_encode()

    3. Takes first 7 characters as the short code
    """
    # Create MD5 hash of the URL
    hash_object = hashlib.md5(url.encode())
    hash_hex = hash_object.hexdigest()
    
    # Convert hex to base62
    hash_int = int(hash_hex, 16)
    short_code = base62_encode(hash_int)[:length]
    
    return short_code


def base62_encode(num):
    """
    Convert a number to base62 string
    Uses: 0-9, a-z, A-Z (62 characters total)
    
    Args:
        num: Integer to encode
    
    Returns:
        Base62 encoded string

    How it works:
    1. Takes a number

    2. Divides it by 62 repeatedly

    3. Converts each remainder to a base62 character

    4. Reverses the result
    """
    alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase
    if num == 0:
        return alphabet[0]
    
    arr = []
    while num:
        num, rem = divmod(num, 62)
        arr.append(alphabet[rem])
    
    return ''.join(reversed(arr))


def is_valid_url(url):
    """
    Validate if a string is a valid URL
    
    Args:
        url: String to validate
    
    Returns:
        True if valid, False otherwise
    """
    try:
        result = urlparse(url)
        # Must have scheme (http/https) and netloc (domain)
        return all([result.scheme, result.netloc])
    except:
        return False


"""
How do these functions work together?
When you submit a URL to shorten:

1. is_valid_url() checks if it's legitimate

2. generate_short_code() creates the short code

3. The short code is saved with the original URL in the database

4. User gets back the short URL

"""