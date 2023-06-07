function validateForm() {
    var form = document.getElementById("hadForm");
    var questionGroups = form.getElementsByClassName("question-group");
  
    for (var i = 0; i < questionGroups.length; i++) {
      var radios = questionGroups[i].getElementsByTagName("input");
      var checkedCount = 0;
  
      for (var j = 0; j < radios.length; j++) {
        if (radios[j].type === "radio" && radios[j].checked) {
          checkedCount++;
        }
      }
  
      if (checkedCount === 0) {
        alert("Por favor, responda todas as perguntas");
        return false;
      }
    }
  
    return true;
  }