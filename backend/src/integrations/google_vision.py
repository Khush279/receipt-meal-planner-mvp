from google.cloud import vision
import google.generativeai as genai
from typing import List, Dict, Any
import os
from PIL import Image
import io

# Google Vision API client
vision_client = vision.ImageAnnotatorClient()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel('gemini-pro')

class GoogleVisionService:
    """
    Service for Google Cloud Vision API integration
    Handles receipt OCR and text extraction
    """
    
    @staticmethod
    async def extract_text_from_receipt(image_bytes: bytes) -> Dict[str, Any]:
        """
        Extract text from receipt image using Google Vision OCR
        """
        try:
            # Create Vision API image object
            image = vision.Image(content=image_bytes)
            
            # Detect text in the image
            response = vision_client.text_detection(image=image)
            texts = response.text_annotations
            
            if response.error.message:
                raise Exception(f"Vision API error: {response.error.message}")
                
            # Extract full text
            full_text = texts[0].description if texts else ""
            
            # Extract individual text annotations
            text_annotations = []
            for text in texts[1:]:  # Skip the first one (full text)
                text_annotations.append({
                    "text": text.description,
                    "confidence": text.confidence if hasattr(text, 'confidence') else 0.0,
                    "bounding_box": {
                        "vertices": [(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices]
                    }
                })
            
            return {
                "full_text": full_text,
                "text_annotations": text_annotations,
                "status": "success"
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "status": "error"
            }

class GeminiService:
    """
    Service for Google Gemini AI integration
    Handles intelligent text processing and meal planning
    """
    
    @staticmethod
    async def parse_receipt_data(raw_text: str) -> Dict[str, Any]:
        """
        Parse receipt text using Gemini to extract structured data
        """
        try:
            prompt = f"""
            Parse this receipt text and extract the following information in JSON format:
            - store_name
            - date (YYYY-MM-DD format)
            - total_amount (numeric)
            - items (array with name, quantity, unit_price, total_price)
            
            Receipt text:
            {raw_text}
            
            Return only valid JSON, no additional text.
            """
            
            response = gemini_model.generate_content(prompt)
            
            # TODO: Parse and validate JSON response
            # This is a placeholder for the structured parsing
            return {
                "parsed_data": response.text,
                "status": "success"
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "status": "error"
            }
    
    @staticmethod
    async def generate_meal_suggestions(inventory_items: List[str]) -> Dict[str, Any]:
        """
        Generate meal suggestions based on available inventory
        """
        try:
            items_text = ", ".join(inventory_items)
            
            prompt = f"""
            Based on these available ingredients: {items_text}
            
            Generate 3 meal suggestions with:
            - Recipe name
            - Ingredients needed (mark which are available)
            - Preparation time
            - Difficulty level
            - Brief instructions
            
            Return as JSON format.
            """
            
            response = gemini_model.generate_content(prompt)
            
            return {
                "meal_suggestions": response.text,
                "status": "success"
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "status": "error"
            }

# Helper functions
async def process_receipt_with_ai(image_bytes: bytes) -> Dict[str, Any]:
    """
    Full pipeline: OCR + AI parsing for receipt processing
    """
    # Step 1: Extract text with Vision API
    vision_result = await GoogleVisionService.extract_text_from_receipt(image_bytes)
    
    if vision_result["status"] == "error":
        return vision_result
    
    # Step 2: Parse with Gemini
    gemini_result = await GeminiService.parse_receipt_data(vision_result["full_text"])
    
    return {
        "ocr_result": vision_result,
        "parsed_result": gemini_result,
        "status": "success"
    }
