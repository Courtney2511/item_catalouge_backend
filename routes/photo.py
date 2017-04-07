from flask import Blueprint, request, jsonify
from database_models import Photo
from database import db_session

photo_api = Blueprint('photo_api', __name__)


# PHOTO BY ID ENDPOINT
@photo_api.route('/photos/<int:photo_id>', methods=['GET'])
def get_photo(photo_id):
    photo = Photo.query.get(photo_id)
    return jsonify(photo=photo.serialize)


@photo_api.route('/photos/<int:photo_id>', methods=['PUT'])
def edit_photo(photo_id):
    photo = Photo.query.get(photo_id)
    data = request.get_json()
    photo.description = data['description']
    photo.picture = data['picture']
    photo.category_id = data['category_id']
    db_session.add(photo)
    db_session.commit()
    return jsonify(photo=photo.serialize), 200


@photo_api.route('/photos/<int:photo_id>', methods=['DELETE'])
def delete_photo(photo_id):
    photo = Photo.query.get(photo_id)
    if photo is None:
        return jsonify(Message="Not Found"), 404
    db_session.delete(photo)
    db_session.commit()
    return jsonify(success=True)