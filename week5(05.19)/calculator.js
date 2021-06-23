function add(char) {
    const display = document.getElementById('display');
    display.value = display.value + char;
}

function calculate() {
    const display = document.getElementById('display');
    const result = eval(display.value);
    display.value = result;
}

function reset() {
    document.getElementById('display').value = "";
}
