<form action = {{actionType}} method=POST>
<input type=hidden name=id value={{stud.id}}>
Фамилия:<br><input type=text name=last_name value={{stud.last_name}}><br>
Имя:<br><input type=text name=first_name value={{stud.first_name}}><br>
Отчество:<br><input type=text name=middle_name value={{stud.middle_name}}><br>
Возраст:<br><input type=number name=age value={{stud.age}}><br>
Средний балл:<br><input type=text name=average_score value={{stud.average_score}}><br>
    {% if modelName == "MainStudent" %}
        Почта группы:<br><input type=text name=email value={{stud.email}}><br>
    {% endif %}
<br><input type=submit value="Ok">
    <input type="reset" value="Reset">
</form>