"""
this script builds html files with either classic or testclassic templates
in share/jupyter/nbconvert/templates, but fails with
classic_clone in ./project_templatesls

"""
import nbformat
from traitlets.config import Config
from nbconvert import HTMLExporter
from jinja2 import FileSystemLoader

nbfile = "quiz_notebook.ipynb"
the_ipynb = nbformat.read(nbfile, as_version=4)

c = Config()
c.TemplateExporter.template_path = ['.', './project_templates']
c.TemplateExporter.template_data_paths = ['.', './project_templates']
c.Application.loglevel = 'DEBUG'
dl = FileSystemLoader('project_templates/')
for template in ['classic', 'testclassic', 'classic_clone']:
    c.HTMLExporter.template_name = template
    html_exporter = HTMLExporter(config=c, extra_loaders=[dl])
    (body, resources) = html_exporter.from_notebook_node(the_ipynb)
    with open(f"{template}.html", 'w') as outfile:
        outfile.write(body)
    print(f"\n{'*'*20}\n{template} succeeds\n{'*'*20}\n")
