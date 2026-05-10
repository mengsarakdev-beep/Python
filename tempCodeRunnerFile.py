class CustomError(Exception): 
    """A custom exception class.""" 
    pass
try: 
    raise CustomError("An error occurred.") 
except CustomError as e: 
    print(f"Caught an exception: {e}")
    