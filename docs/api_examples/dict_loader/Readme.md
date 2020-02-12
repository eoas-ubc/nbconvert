# need to document correct syntax for template_paths

To run:

```
python make_html.py
```

output:

```
% python make_html.py 

********************
classic succeeds
********************


********************
testclassic succeeds
********************

Traceback (most recent call last):
  File "make_html.py", line 24, in <module>
    (body, resources) = html_exporter.from_notebook_node(the_ipynb)
  File "/Users/phil/repos/nbconvert/nbconvert/exporters/html.py", line 103, in from_notebook_node
    self.register_filter('highlight_code', highlight_code)
  File "/Users/phil/repos/nbconvert/nbconvert/exporters/templateexporter.py", line 418, in register_filter
    return self._register_filter(self.environment, name, jinja_filter)
  File "/Users/phil/repos/nbconvert/nbconvert/exporters/templateexporter.py", line 154, in environment
    self._environment_cached = self._create_environment()
  File "/Users/phil/repos/nbconvert/nbconvert/exporters/templateexporter.py", line 436, in _create_environment
    paths = self.get_template_paths()
  File "/Users/phil/repos/nbconvert/nbconvert/exporters/templateexporter.py", line 465, in get_template_paths
    template_names = self.get_template_names()
  File "/Users/phil/repos/nbconvert/nbconvert/exporters/templateexporter.py", line 512, in get_template_names
    raise ValueError('No template sub-directory with name %r found in the following paths:\n\t%s' % (template_name, paths))
ValueError: No template sub-directory with name 'classic_clone' found in the following paths:
	/Users/phil/repos/nbconvert/share/jupyter
	/Users/phil/Library/Jupyter
	/Users/phil/a50037/envs/e213/share/jupyter
	/usr/local/share/jupyter
	/usr/share/jupyter
~/repos/nbconvert/docs/api_examples/template_path_issue e213 [master] phil@rail
```
