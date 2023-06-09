function validateForm() {
  var emailInput = document.getElementById("exampleInputEmail1");
  var radioContainers = document.getElementsByClassName("radioContainer");

  if (emailInput.value === "") {
    alert("Por favor informe seu email.");
    return false;
  }

  for (var i = 0; i < radioContainers.length; i++) {
    var question = radioContainers[i].previousElementSibling.textContent.trim();
    var radioButtons = radioContainers[i].getElementsByClassName("form-check-input");
    var checkedCount = 0;

    for (var j = 0; j < radioButtons.length; j++) {
      if (radioButtons[j].checked) {
        checkedCount++;
        break; // Exit the loop if at least one radio button is checked
      }
    }

    if (checkedCount === 0) {
      alert("Por favor selecione uma opção para a pergunta: " + question);
      return false;
    }
  }

  return true;
}
