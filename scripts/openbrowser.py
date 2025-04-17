import webbrowser
import validators
from urllib.parse import urlparse

def open_browser_with_url(url):
    """
    Opens the default web browser with the specified URL.
    
    This function validates the provided URL for correctness and attempts
    to open the default web browser with the given URL. If the URL is not
    valid or if there's an error in opening the browser, appropriate
    exceptions are raised.
    
    Args:
        url (str): The URL to open in the web browser. Must be a valid URL
                   including the protocol (e.g., 'https://example.com').
    
    Returns:
        bool: True if the browser was successfully opened, False otherwise.
    
    Raises:
        ValueError: If the URL is empty or not a string.
        ValueError: If the URL is not valid (missing protocol or improper format).
        Exception: If there's an error opening the browser.
    
    Examples:
        >>> open_browser_with_url('https://www.python.org')
        True
        >>> open_browser_with_url('invalid-url')
        ValueError: Invalid URL format. URL must include protocol (e.g., 'https://example.com')
    """
    # Check if URL is provided and is a string
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")
    
    # Check if URL has a protocol (http, https, etc.)
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        raise ValueError("Invalid URL format. URL must include protocol (e.g., 'https://example.com')")
    
    # Additional validation using validators library (if available)
    try:
        if not validators.url(url):
            raise ValueError(f"Invalid URL: {url}")
    except NameError:
        # validators library not installed, use basic validation
        if not (parsed_url.scheme and parsed_url.netloc):
            raise ValueError(f"Invalid URL: {url}")
    
    # Attempt to open the URL in the default browser
    try:
        webbrowser.open(url)
        return True
    except Exception as e:
        raise Exception(f"Error opening browser: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        # Replace with your URL
        success = open_browser_with_url("https://www.python.org")
        if success:
            print("Browser opened successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")