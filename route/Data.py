from flask import Blueprint
from controller.Data import getScrappedData

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(getScrappedData)