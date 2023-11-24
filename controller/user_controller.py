from app import app
from model.user_model import user_model
from flask import request, send_file
from datetime import datetime

object = user_model() # call methods from the user_model class

@app.route("/user/getall")
def signup():
    return object.user_getall_model()

@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    return object.user_addone_model(request.form)

@app.route("/user/<uid>/upload/avatar", methods=['PUT'])
def user_upload_avatar_controller(uid):
    file = request.files['avatar']
    uniqueFileName = str(datetime.now().timestamp()).replace(".", "")
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit)-1]
    file.save(f"uploads/{uniqueFileName}.{ext}")
    filePath = f"uploads/{uniqueFileName}.{ext}"
    return object.user_upload_avatar_model(uid, filePath)

# fetching the uploaded file
@app.route("/uploads/<filename>")
def user_getavatart_controller(filename):
    return send_file(f"uploads/{filename}")