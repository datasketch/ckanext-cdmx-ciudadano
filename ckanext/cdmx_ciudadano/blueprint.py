from flask import Blueprint

from ckan.plugins.toolkit import render
import ckan.lib.helpers as h


validate = Blueprint(u'validate', __name__)


@validate.route(u'/validar')
def index():
    extra_vars = {
    }

    return render(u'validar.html', extra_vars)