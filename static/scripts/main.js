function validateForm() {
    var form = document.getElementById("hadForm");
    var inputs = form.getElementsByTagName("input");

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value === "") {
        alert("Por favor preencha todos os campos.");
        return false;
        }
    }

    return true;
}
