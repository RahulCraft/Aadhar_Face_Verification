from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VerificationRequest
from .serializers import VerificationRequestSerializer
from .utils.ocr import extract_dob_from_aadhaar
from .utils.face_match import compare_faces

class VerifyAadhaarView(APIView):
    def post(self, request):
        aadhaar = request.FILES.get('aadhaar_image')
        selfie = request.FILES.get('selfie_image')

        if not aadhaar or not selfie:
            return Response({"error": "Both Aadhaar and Selfie are required."}, status=400)

        instance = VerificationRequest.objects.create(aadhaar_image=aadhaar, selfie_image=selfie)

        aadhaar_path = instance.aadhaar_image.path
        selfie_path = instance.selfie_image.path

        dob = extract_dob_from_aadhaar(aadhaar_path)

        # Check if Aadhaar keywords present in OCR
        if dob is None:
            instance.delete()
            return Response({"verified": False, "message": "Upload only Aadhaar image. Try again."}, status=400)

        matched = compare_faces(aadhaar_path, selfie_path)

        instance.dob_extracted = dob or ""
        instance.face_match = matched
        instance.save()

        if not matched:
            return Response({"verified": False, "message": "Face does not match with Aadhaar photo."})

        return Response({"verified": True, "dob": dob, "message": "Face matched and DOB extracted."})