# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "MC-Wiki"
copyright = "2026, MongooseChat team"
author = "MongooseChat team"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design", "sphinxext.opengraph", "sphinx_copybutton"]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = f"{project} V{release}"
html_show_sourcelink = False
html_static_path = ["_static"]

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "dark-gray",
            "color-sidebar-brand-text": "hotpink",
    },
    "dark_css_variables": {
            "color-brand-primary": "gray",
            "color-sidebar-brand-text": "pink",
        },
}

ogp_site_url = "https://mongoosechat.github.io/MC-wiki/"
