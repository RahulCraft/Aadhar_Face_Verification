🔍 Aadhaar Face Verification using Deep Learning & OCR:

This project implements an automated Aadhaar verification system using Deep Learning for face recognition and OCR (Optical Character Recognition) for Date of Birth (DOB) extraction from Aadhaar card images.
It is designed to verify the identity of users by matching their real-time selfie with the photograph on their Aadhaar card, and extracting the DOB for further authentication or validation steps.

🚀 Features:

✅ Upload Aadhaar card and a selfie to verify identity.
🔍 Extracts Date of Birth (DOB) from Aadhaar using OCR (Tesseract).
🤖 Matches the face on the Aadhaar with the selfie using DeepFace (VGG-Face / ArcFace).
⚠️ Handles low-quality documents and provides fallback messages.
📁 Accepts only Aadhaar card documents (auto-detection).
📦 REST API endpoint built using Django + DRF (Django REST Framework).
🧪 Fully testable via Postman or integrated frontend.
📊 JSON responses for seamless frontend or mobile app integration.


📂 Technologies Used:

Django 4+ – Backend Framework
Django REST Framework (DRF) – API Layer
MySQL – Database for storing verification logs
DeepFace – Face matching (Supports VGG-Face, ArcFace, Facenet, Dlib)
OpenCV – Image preprocessing
Tesseract OCR – Extracting DOB from Aadhaar
Render.com – Cloud Deployment


🔐 API Output:

{
  "verified": true,
  "message": "Face matched successfully",
  "dob": "12-08-1998"
}

⚙️ How It Works:

User uploads Aadhaar image and selfie via /verify-aadhaar/ API.
Aadhaar image is passed through OCR for DOB extraction.
Both images are preprocessed and passed to DeepFace for comparison.
If confidence threshold ≥ 0.5 (50%), verification is successful.
Response is returned in structured JSON format.
