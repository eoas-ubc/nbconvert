{%- extends 'null.tpl' -%}

{%- block header -%}
#!/usr/bin/env ipython
# coding: utf-8
{% endblock header %}

{% block in_prompt %}
{% if resources.global_content_filter.include_input_prompt -%}
    # In[{{ cell.execution_count if cell.execution_count else ' ' }}]:
{% endif %}
{% endblock in_prompt %}

{% block input %}
{{ cell.source | ipython2python }}
{% endblock input %}

{% block markdowncell scoped %}
{{ cell.source | comment_lines }}
{% endblock markdowncell %}
