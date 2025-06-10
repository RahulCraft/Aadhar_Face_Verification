import easyocr
import re

reader = easyocr.Reader(['en'])

def extract_dob_from_aadhaar(image_path):
    try:
        results = reader.readtext(image_path, detail=0)
        text = " ".join(results)

        if not any(keyword in text.lower() for keyword in ["aadhaar", "government of india"]):
            return None

        match = re.search(r'(\d{2}[/-]\d{2}[/-]\d{4})', text)
        if match:
            return match.group(1)
        return None
    except:
        return None