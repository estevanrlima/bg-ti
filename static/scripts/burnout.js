function validateForm() {
    var form = document.getElementById("burnoutForm");
    var inputs = form.getElementsByTagName("input");

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].type === "radio" && !inputs[i].checked) {
            alert("Por favor responda todas as perguntas");
            return false;
        } else if (inputs[i].value === "") {
            alert("Por favor responda todas as perguntas");
            return false;
        }
    }

    return true;
}