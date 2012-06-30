var i = 0;

function addQuestion() {
    var form = document.getElementById('survey_form');
    var new_text_area = document.createElement('input');
    new_text_area.setAttribute('type','textarea');
    new_text_area.setAttribute('rows', '4');
    new_text_area.setAttribute('cols', '20');
    new_text_area.setAttribute('id', 'area_' + i++);
    form.appendChild(new_text_area);
    form.appendChild(document.createElement('br'));
}