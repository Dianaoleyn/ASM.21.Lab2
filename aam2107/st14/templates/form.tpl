{% extends "base.tpl" %}

{% block content %}

    {% if modelName == "MainStudent" %}
        <p>Форма ввода информации о старосте</p>
    {% else %}
        <p>Форма ввода информации о студенте</p>
    {% endif %}

    {% if stud.id == 0 %}
        {% with actionType = '/add' %}
            {% include "subform.tpl" %}
        {% endwith%}
    {% else %}
        {% with actionType = '/update' %}
            {% include "subform.tpl" %}
        {% endwith %}
    {% endif %}

{% endblock %}


