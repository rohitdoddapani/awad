function appendChar(char) {
    document.getElementById('result').value += char;
  }
  
  function deleteChar() {
    var result = document.getElementById('result').value;
    document.getElementById('result').value = result.slice(0, -1);
  }
  
  function clearResult() {
    document.getElementById('result').value = '';
  }
  
  function calculate() {
    var flag = localStorage.getItem("power_flag");
    console.log(flag);
    var result = document.getElementById('result').value;
    var output;
    if(flag){
      const values = result.split("^");
      var output = Math.pow(values[0], values[1]);
    }else{
      try {
        output = eval(result);
      } catch (error) {
        output = 'Error';
      }
    }

    document.getElementById('result').value = output;
    localStorage.removeItem("power_flag")
  }

  function calculateSquareRoot() {
    var result = document.getElementById('result').value;
    var output = Math.sqrt(result);
    document.getElementById('result').value = output;
  }
  
  function calculateSin() {
    var result = document.getElementById('result').value;
    var output = Math.sin(result);
    document.getElementById('result').value = output;
  }

  function calculateCos() {
    var result = document.getElementById('result').value;
    var output = Math.cos(result);
    document.getElementById('result').value = output;
  }
  
  function calculateTan() {
    var result = document.getElementById('result').value;
    var output = Math.tan(result);
    document.getElementById('result').value = output;
  }
  
  function calculatePower() {
    var result = document.getElementById('result').value;
    // var result = document.getElementById('result') = result+'^';
    // var power = prompt('Enter the power:');
    // var output = Math.pow(result, power);
    document.getElementById('result').value = result+'^';
    localStorage.setItem("power_flag", 1);
  }
  