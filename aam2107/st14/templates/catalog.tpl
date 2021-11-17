{% extends "base.tpl" %}

{% block content %}

    {% for stud in mainStudents %}
        {% include "mainstudent.tpl" ignore missing %}
    {% endfor %}

    {% for stud in students %}
        {% include "student.tpl" ignore missing %}
    {% endfor %}

    {% include "add.tpl" ignore missing %}
{% endblock %}