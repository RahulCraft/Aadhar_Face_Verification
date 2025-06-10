import face_recognition


def compare_faces(aadhaar_img_path, selfie_img_path, tolerance=0.6):
    try:
        doc_img = face_recognition.load_image_file(aadhaar_img_path)
        doc_face_enc = face_recognition.face_encodings(doc_img)

        selfie_img = face_recognition.load_image_file(selfie_img_path)
        selfie_face_enc = face_recognition.face_encodings(selfie_img)

        if not doc_face_enc or not selfie_face_enc:
            return False

        match = face_recognition.compare_faces([doc_face_enc[0]], selfie_face_enc[0], tolerance=tolerance)
        return match[0]
    except:
        return False