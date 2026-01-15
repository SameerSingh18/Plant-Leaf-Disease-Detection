"""
Base64 Image Test for Leaf Disease Detection
===========================================
"""

from dotenv import load_dotenv
load_dotenv()   # 🔥 VERY IMPORTANT

import json
import sys
import os
import base64
from pathlib import Path

# Add Leaf Disease folder to path
LEAF_DIR = Path(__file__).parent / "Leaf Disease"
sys.path.insert(0, str(LEAF_DIR))

try:
    from main import LeafDiseaseDetector
except ImportError as e:
    raise ImportError(f"Could not import LeafDiseaseDetector: {str(e)}")


def test_with_base64_data(base64_image_string: str):
    try:
        detector = LeafDiseaseDetector()
        return detector.analyze_leaf_image_base64(base64_image_string)
    except Exception as e:
        return {"error": str(e)}


def convert_image_to_base64_and_test(image_bytes: bytes):
    try:
        if not image_bytes:
            return {"error": "No image bytes provided"}

        base64_string = base64.b64encode(image_bytes).decode("utf-8")
        return test_with_base64_data(base64_string)

    except Exception as e:
        return {"error": str(e)}

