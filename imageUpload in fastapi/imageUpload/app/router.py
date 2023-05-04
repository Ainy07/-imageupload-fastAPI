from fastapi import APIRouter, Depends, UploadFile, File, status, HTTPException
from .models import *
from slugify import slugify
from datetime import datetime, timedelta
import os
from .pydantic_models import *


router = APIRouter()


@router.post("/category/")
async def create_category(data: categoryitem = Depends(),
                          category_image: UploadFile = File(...)):
    if await Category.exists(name=data.name):
        return {'status': False, 'message': 'category already exists'}
    else:
        slag = slugify(data.name)

        FILEPATH = 'static/images/category'

        if not os.path.isdir(FILEPATH):
            os.mkdir(FILEPATH)

        filename = category_image.filename
        extension = filename.split(".")[1]
        imagename = filename.split(".")[0]

        if extension not in ['png', 'jpg', 'jpeg']:
            return {'status': 'error', 'detail': 'File extension not allowed'}

        dt = datetime.datetime.now()
        dt_timestamp = round(datetime.datetime.timestamp(dt))

        modified_image_name = imagename+"_"+str(dt_timestamp)+"."+extension
        genrated_name = FILEPATH + modified_image_name
        file_content = await category_image.read()

        with open(genrated_name, 'wb') as file:
            file.write(file_content)

            file.close()

        category_obj = await Category.create(
            category_image=genrated_name,
            discription=data.description,
            name=data.name,
            slag=slag
        )
        return category_obj