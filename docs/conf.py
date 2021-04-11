# #!/usr/bin/env python
# #
# # codebots documentation build configuration file, created by
# # sphinx-quickstart on Fri Jun  9 13:47:02 2017.
# #
# # This file only contains a selection of the most common options. For a full
# # list see the documentation:
# # https://www.sphinx-doc.org/en/master/usage/configuration.html
# #
# # This file is execfile()d with the current directory set to its
# # containing dir.
# #
# # Note that not all possible configuration values are present in this
# # autogenerated file.
# #
# # All configuration values have a default; values that are commented out
# # serve to show the default.

# # If extensions (or modules to document with autodoc) are in another
# # directory, add these directories to sys.path here. If the directory is
# # relative to the documentation root, use os.path.abspath to make it
# # absolute, like shown here.
# #
# import os
# import sys
# import inspect
# import importlib
# from distutils.version import LooseVersion

# from sphinx.ext.napoleon.docstring import NumpyDocstring
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

# import codebots

# import sphinx_material
# from recommonmark.transform import AutoStructify

# FORCE_CLASSIC = os.environ.get("SPHINX_MATERIAL_FORCE_CLASSIC", False)
# FORCE_CLASSIC = FORCE_CLASSIC in ("1", "true")

# # -- Project information -----------------------------------------------------

# project = "CodeBots"
# copyright = "2021, Francesco Ranaudo"
# author = "Francesco Ranaudo"
# # The full version, including alpha/beta/rc tags
# release = "0.4.0"
# # release = LooseVersion(sphinx_material.__version__).vstring

# # -- General configuration ---------------------------------------------

# # If your documentation needs a minimal Sphinx version, state it here.
# #
# # needs_sphinx = "1.0"

# # Add any Sphinx extension module names here, as strings. They can be
# # extensions coming with Sphinx (named "sphinx.ext.*") or your custom ones.
# extensions = [
#     "sphinx.ext.autodoc",
#     "numpy"
#     "sphinx.ext.autosummary",
#     "sphinx_automodapi.automodapi",
#     "sphinx.ext.doctest",
#     "sphinx.ext.intersphinx",
#     "sphinx.ext.mathjax",
#     "sphinx.ext.napoleon",
#     "sphinx.ext.viewcode",
#     "sphinx.ext.githubpages",
#     "sphinx.ext.inheritance_diagram",
#     # "nbsphinx",
# ]

# # Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# # The suffix(es) of source filenames.
# # You can specify multiple suffix as a list of string:
# #
# # source_suffix = [".rst", ".md"]
# source_suffix = ".rst"

# # The master toctree document.
# master_doc = "index"

# # The version info for the project you"re documenting, acts as replacement
# # for |version| and |release|, also used in various other places throughout
# # the built documents.
# #
# # The short X.Y version.
# version = codebots.__version__
# # The full version, including alpha/beta/rc tags.
# release = codebots.__version__

# # The language for content autogenerated by Sphinx. Refer to documentation
# # for a list of supported languages.
# #
# # This is also used if you do content translation via gettext catalogs.
# # Usually you set "language" from the command line for these cases.
# language = None

# # List of patterns, relative to source directory, that match files and
# # directories to ignore when looking for source files.
# # This patterns also effect to html_static_path and html_extra_path
# exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# # The name of the Pygments (syntax highlighting) style to use.
# pygments_style = "sphinx"

# # If true, `todo` and `todoList` produce output, else they produce nothing.
# todo_include_todos = True

# # autodoc options
# autodoc_default_flags = [
#     "undoc-members",
#     # "show-inheritance",
# ]



# # napoleon options
# napoleon_google_docstring = False
# napoleon_numpy_docstring = True
# napoleon_include_init_with_doc = False
# napoleon_include_private_with_doc = True
# napoleon_include_special_with_doc = True
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = False
# napoleon_use_rtype = False


# # docstring sections

# autodoc_member_order = "alphabetical"
# autoclass_content = "class"
# autosummary_generate = True

# def parse_attributes_section(self, section):
#     return self._format_fields("Attributes", self._consume_fields())

# NumpyDocstring._parse_attributes_section = parse_attributes_section

# def patched_parse(self):
#     self._sections["attributes"] = self._parse_attributes_section
#     self._unpatched_parse()

# NumpyDocstring._unpatched_parse = NumpyDocstring._parse
# NumpyDocstring._parse = patched_parse

# # intersphinx options

# intersphinx_mapping = {
#     "python": ("https://docs.python.org/", None),
# }

# # linkcode

# def linkcode_resolve(domain, info):
#     if domain != 'py':
#         return None
#     if not info['module']:
#         return None
#     if not info['fullname']:
#         return None

#     package = info['module'].split('.')[0]
#     if not package.startswith('compas_fea'):
#         return None

#     module = importlib.import_module(info['module'])
#     parts = info['fullname'].split('.')

#     if len(parts) == 1:
#         obj = getattr(module, info['fullname'])
#         filename = inspect.getmodule(obj).__name__.replace('.', '/')
#         lineno = inspect.getsourcelines(obj)[1]
#     elif len(parts) == 2:
#         obj_name, attr_name = parts
#         obj = getattr(module, obj_name)
#         attr = getattr(obj, attr_name)
#         if inspect.isfunction(attr):
#             filename = inspect.getmodule(obj).__name__.replace('.', '/')
#             lineno = inspect.getsourcelines(attr)[1]
#         else:
#             return None
#     else:
#         return None

#     return f"https://github.com/compas-dev/compas_fea/blob/master/src/{filename}.py#L{lineno}"

# # extlinks

# extlinks = {}


# # -- Options for HTML output -------------------------------------------

# # The theme to use for HTML and HTML Help pages.  See the documentation for
# # a list of builtin themes.
# # Theme options are theme-specific and customize the look and feel of a
# # theme further.  For a list of options available for each theme, see the
# # documentation.
# #
# # Material theme options (see theme.conf for more information)
# html_theme = "sphinx_material"
# # html_theme_path = sphinx_compas_theme.get_html_theme_path()
# html_logo = "_static/images/icon.png"
# html_theme_options = {
#     "nav_title": "CodeBots",
#     "google_analytics_account": "G-1186S5WWWK",
#     "base_url": "https://github.com/franaudo/codebots",
#     "color_primary": "white",
#     "color_accent": "red",
#     "repo_url": "https://github.com/franaudo/codebots",
#     "repo_name": "codebots",
#     "repo_type": "github",
#     "globaltoc_depth": 1,
#     "globaltoc_collapse": False,
#     "globaltoc_includehidden": False,
#     # "html_minify": True,
#     # "css_minify": True,
# }
# html_last_updated_fmt = ""
# html_copy_source = False
# html_show_sourcelink = False
# html_add_permalinks = ""
# html_experimental_html5_writer = True
# html_compact_lists = True

# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# # # Additional
# # plot_html_show_source_link = False
# # plot_html_show_formats = False

# # -- Options for HTMLHelp output ---------------------------------------

# # Output file base name for HTML help builder.
# htmlhelp_basename = "botsdoc"


# # -- Options for LaTeX output ------------------------------------------

# latex_elements = {
#     # The paper size ("letterpaper" or "a4paper").
#     #
#     # "papersize": "letterpaper",

#     # The font size ("10pt", "11pt" or "12pt").
#     #
#     # "pointsize": "10pt",

#     # Additional stuff for the LaTeX preamble.
#     #
#     # "preamble": "",

#     # Latex figure (float) alignment
#     #
#     # "figure_align": "htbp",
# }

# # Grouping the document tree into LaTeX files. List of tuples
# # (source start file, target name, title, author, documentclass
# # [howto, manual, or own class]).
# latex_documents = [
#     (master_doc, "codebots.tex",
#      "codebots Documentation",
#      "Francesco Ranaudo", "manual"),
# ]


# # -- Options for manual page output ------------------------------------

# # One entry per manual page. List of tuples
# # (source start file, name, description, authors, manual section).
# man_pages = [
#     (master_doc, "codebots",
#      "codebots Documentation",
#      [author], 1)
# ]


# # -- Options for Texinfo output ----------------------------------------

# # Grouping the document tree into Texinfo files. List of tuples
# # (source start file, target name, title, author,
# #  dir menu entry, description, category)
# texinfo_documents = [
#     (master_doc, "codebots",
#      "codebots Documentation",
#      author,
#      "codebots",
#      "One line description of project.",
#      "Miscellaneous"),
# ]

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from distutils.version import LooseVersion
import os

import sphinx_material
from recommonmark.transform import AutoStructify

FORCE_CLASSIC = os.environ.get("SPHINX_MATERIAL_FORCE_CLASSIC", False)
FORCE_CLASSIC = FORCE_CLASSIC in ("1", "true")

# -- Project information -----------------------------------------------------

project = "codebots"
html_title = "codebots"

copyright = "2021, Francesco Ranaudo"
author = "Francesco Ranaudo"

# The full version, including alpha/beta/rc tags
release = LooseVersion(sphinx_material.__version__).vstring

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "recommonmark",
    "sphinx_markdown_tables",
    "sphinx_copybutton",
]

autosummary_generate = True
autoclass_content = "class"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["_static"]

# -- HTML theme settings ------------------------------------------------

html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"

# material theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "http://franaudo.github.io/codebots/",
    "repo_url": "https://github.com/franaudo/codebots",
    "repo_name": "codebots",
    "google_analytics_account": "G-1186S5WWWK",
    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    "logo_icon": "&#xe869",
    "repo_type": "github",
    "globaltoc_depth": 2,
    "color_primary": "blue",
    "color_accent": "cyan",
    "touch_icon": "images/apple-icon-152x152.png",
    "theme_color": "#2196f3",
    "master_doc": False,
    "nav_links": [
        {"href": "index", "internal": True, "title": "codebots"},
        {
            "href": "https://github.com/franaudo",
            "internal": False,
            "title": "About me",
        },
    ],
    "heroes": {
        "index": "Collection of bots for tasks automation in your code.",
        "customization": "????",
    },
    "version_dropdown": True,
    "version_json": "_static/versions.json",
    "version_info": {
        "Release": "https://franaudo.github.io/codebots/",
        "Development": "https://franaudo.github.io/codebots/development/",
        "Release (rel)": "/codebots/",
        "Development (rel)": "/codebots/development/",
    },
    "table_classes": ["plain"],
}

if FORCE_CLASSIC:
    print("!!!!!!!!! Forcing classic !!!!!!!!!!!")
    html_theme = "classic"
    html_theme_options = {}
    html_sidebars = {"**": ["globaltoc.html", "localtoc.html", "searchbox.html"]}

language = "en"
html_last_updated_fmt = ""

todo_include_todos = True
html_favicon = "images/favicon.ico"

html_use_index = True
html_domain_indices = True

nbsphinx_execute = "always"
nbsphinx_kernel_name = "python3"

extlinks = {
    "duref": (
        "http://docutils.sourceforge.net/docs/ref/rst/" "restructuredtext.html#%s",
        "",
    ),
    "durole": ("http://docutils.sourceforge.net/docs/ref/rst/" "roles.html#%s", ""),
    "dudir": ("http://docutils.sourceforge.net/docs/ref/rst/" "directives.html#%s", ""),
}

# Enable eval_rst in markdown
def setup(app):
    app.add_config_value(
        "recommonmark_config",
        {"enable_math": True, "enable_inline_math": True, "enable_eval_rst": True},
        True,
    )
    app.add_transform(AutoStructify)
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )


