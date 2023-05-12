import mimetypes
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation
from flask import request

from ckanext.cdmx_ciudadano.lib import (
    date_formats,
    extract_from_key,
    get_format_color,
    get_popular_datasets,
    get_site_url,
    update_frequencies,
    chart_types,
    humanize_date,
    get_package_categories,
    humanize_filesize,
    dashboard_types,
    get_join_vars,
)


class CdmxCiudadanoPlugin(
    plugins.SingletonPlugin, toolkit.DefaultDatasetForm, DefaultTranslation
):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IMiddleware)
    # plugins.implements(plugins.IPackageController)

    # IMiddleware
    def make_middleware(self, app, config):
        @app.after_request
        def add_header(response):
            guessed_type, _ = mimetypes.guess_type(request.path)
            if guessed_type == "application/pdf":
                response.headers["Content-Type"] = "application/pdf"
            return response

        return app

    def make_error_log_middleware(self, app, config):
        return app

    # ITemplateHelpers

    def get_helpers(self):
        print(toolkit.current_user)
        print("*****")
        return {
            "date_formats": date_formats,
            "update_frequencies": update_frequencies,
            "chart_types": chart_types,
            "humanize_date": humanize_date,
            "get_package_categories": get_package_categories,
            "extract_from_key": extract_from_key,
            "get_popular_datasets": get_popular_datasets,
            "get_format_color": get_format_color,
            "get_site_url": get_site_url,
            "humanize_filesize": humanize_filesize,
            "dashboard_types": dashboard_types,
            "get_join_vars": get_join_vars,
        }

    # IConfigurable

    def configure(self, config):
        """Reference file"""
        # config['licenses_group_url'] = 'file://' + path.dirname(__file__) + '/public/licenses.json'
        """ Reference url """
        config[
            "licenses_group_url"
        ] = "https://raw.githubusercontent.com/datosabiertoscdmx/licencias-portal/main/licencias-portal-cdmx.json"
        config["ckan.locale_default"] = "es"

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_public_directory(config_, "public")
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_resource("assets", "cdmx_assets")

    # IDatasetForm

    def create_package_schema(self):
        schema = super(CdmxCiudadanoPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(CdmxCiudadanoPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(CdmxCiudadanoPlugin, self).show_package_schema()
        schema["tags"]["__extras"].append(toolkit.get_converter("free_tags_only"))
        schema["resources"].update(
            {
                "resource_filters": [toolkit.get_validator("ignore_missing")],
                "resource_subtitle": [toolkit.get_validator("ignore_missing")],
                "resource_default_var": [toolkit.get_validator("ignore_missing")],
                "resource_disaggregate": [toolkit.get_validator("ignore_missing")],
                "resource_viz": [toolkit.get_validator("ignore_missing")],
                "resource_priority_date": [toolkit.get_validator("ignore_missing")],
                "update_frequency": [toolkit.get_validator("ignore_missing")],
                "chart_type": [toolkit.get_validator("ignore_missing")],
                "date_format": [toolkit.get_validator("ignore_missing")],
                "dashboard": [toolkit.get_validator("ignore_missing")],
                "resource_tooltip": [toolkit.get_validator("ignore_missing")],
                "average_legend": [toolkit.get_validator("ignore_missing")],
                "meet_criteria": [toolkit.get_validator("ignore_missing")],
                "join_vars": [toolkit.get_validator("ignore_missing")],
            }
        )
        return schema

    def is_fallback(self):
        return True

    def package_types(self):
        return []

    def _modify_package_schema(self, schema):
        schema["resources"].update(
            {
                "resource_filters": [toolkit.get_validator("ignore_missing")],
                "resource_subtitle": [toolkit.get_validator("ignore_missing")],
                "resource_default_var": [toolkit.get_validator("ignore_missing")],
                "resource_disaggregate": [toolkit.get_validator("ignore_missing")],
                "resource_viz": [toolkit.get_validator("ignore_missing")],
                "resource_priority_date": [toolkit.get_validator("ignore_missing")],
                "update_frequency": [toolkit.get_validator("ignore_missing")],
                "chart_type": [toolkit.get_validator("ignore_missing")],
                "date_format": [toolkit.get_validator("ignore_missing")],
                "dashboard": [toolkit.get_validator("ignore_missing")],
                "resource_tooltip": [toolkit.get_validator("ignore_missing")],
                "average_legend": [toolkit.get_validator("ignore_missing")],
            }
        )
        return schema

    # IFacets

    def dataset_facets(self, facets_dict, package_type):
        facets_dict.pop("tags")
        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        facets_dict.pop("tags")
        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        facets_dict.pop("tags")
        return facets_dict

    # IPackageController

    # def after_dataset_create(self, context, pkg_dict):
    #     print(context)
    #     print("------")
    #     print(pkg_dict)
    #     print("*******")

    # def before_dataset_view(self, pkg_dict):
    #     return pkg_dict

    # def read(self, entity):
    #     pass

    # def create(self, entity) -> None:
    #     pass

    # def edit(self, entity) -> None:
    #     pass

    # def delete(self, entity) -> None:
    #     pass

    # def after_dataset_show(self, context, pkg_dict):
    #     pass

    # def before_dataset_search(self, search_params):
    #     return search_params

    # def after_dataset_search(self, search_results, search_params):
    #     return search_results

    # def before_dataset_index(self, pkg_dict):
    #     return pkg_dict