from flask import Blueprint

from ckan.plugins.toolkit import render
import ckan.lib.helpers as h


validate = Blueprint(u'validate', __name__)
cruza_info = Blueprint(u'cruza_info', __name__)


@validate.route(u'/validar')
def index():
    extra_vars = {
    }

    return render(u'validar.html', extra_vars)

@cruza_info.route(u'/cruza-tu-info')
def index():
    extra_vars = {
    }

    return render(u'cruza-tu-info.html', extra_vars)