import face_recognition

my_picture = face_recognition.load_image_file("me.jpg")
my_face_encoding = face_recognition.face_encodings(my_picture)[0]

unknown_picture = face_recognition.load_image_file("mept2.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

results = face_recognition.compare_faces([my_face_encoding],unknown_face_encoding )

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")

