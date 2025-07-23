file_name = input("Enter file ")
if file_name.endswith("gif"):
    print(f"image/gif")
elif file_name.endswith(".jpg"):
    print(f"image/jpg")
elif file_name.endswith(".jpeg"):
    print(f"image/{file_name}")
elif file_name.endswith(".png"):
    print(f"image/png")
elif file_name.endswith(".pdf"):
    print(f"image/pdf")
elif file_name.endswith(".txt"):
    print(f"image/txt")
elif file_name.endswith(".zip"):
    print("image/zip")
else:
    print("Application/octect-stream")

