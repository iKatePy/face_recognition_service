from sqlalchemy import Column, Integer, String  # Import necessary classes from SQLAlchemy
from .database import Base  # Import Base from database module

class ImageData(Base):
    """
    SQLAlchemy model to store image data and results.

    Attributes:
        id (int): Unique identifier for each record.
        filename (str): Name of the uploaded file.
        results (str): JSON string containing detection results.
    """
    
    __tablename__ = "images"  # Define table name in database
    
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    filename = Column(String)  # Column to store filename of uploaded image
    results = Column(String)  # Column to store results as JSON string
    
