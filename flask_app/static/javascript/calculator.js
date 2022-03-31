// -----COMMON CARDS-----

var common = document.querySelector("#common");

function setComQuantity(element) {
    common.innerText = element.value;
}

function calcCom(){
    var common = document.querySelector("#common");

    num2 = 0.025;
    document.getElementById("resultCom").innerHTML = (common.innerText * num2).toFixed(2)
}


// -----END COMMON-----

// -----RARE CARDS-----

var rare = document.querySelector("#rare");

function setRareQuantity(element) {
    rare.innerText = element.value;
}

function calcRare(){
    var rare = document.querySelector("#rare");

    num2 = 0.08;
    document.getElementById("resultRare").innerHTML = (rare.innerText * num2).toFixed(2)
}

// -----END RARE-----

// -----HOLO CARDS-----

var holo = document.querySelector("#holo");

function setHoloQuantity(element) {
    holo.innerText = element.value;
}

function calcHolo(){
    var holo = document.querySelector("#holo");

    num2 = 0.12;
    document.getElementById("resultHolo").innerHTML = (holo.innerText * num2).toFixed(2)
}

// -----END HOLO-----

// -----ENERGY CARDS-----

var energy = document.querySelector("#energy");

function setEnergyQuantity(element) {
    energy.innerText = element.value;
}

function calcEnergy(){
    var energy = document.querySelector("#energy");

    num2 = 0.01;
    document.getElementById("resultEnergy").innerHTML = (energy.innerText * num2).toFixed(2)
}

// -----END ENERGY-----

// -----GX CARDS-----

var gx = document.querySelector("#gx");

function setGxQuantity(element) {
    gx.innerText = element.value;
}

function calcGx(){
    var gx = document.querySelector("#gx");

    num2 = 1.75;
    document.getElementById("resultGx").innerHTML = (gx.innerText * num2).toFixed(2)
}

// -----END GX-----

// -----V CARDS-----

var v = document.querySelector("#v");

function setVQuantity(element) {
    v.innerText = element.value;
}

function calcV(){
    var v = document.querySelector("#v");

    num2 = 1.00;
    document.getElementById("resultV").innerHTML = (v.innerText * num2).toFixed(2)
}

// -----END V-----

// -----VMAX CARDS-----

var vmax = document.querySelector("#vmax");

function setVmaxQuantity(element) {
    vmax.innerText = element.value;
}

function calcVmax(){
    var vmax = document.querySelector("#vmax");

    num2 = 1.75;
    document.getElementById("resultVmax").innerHTML = (vmax.innerText * num2).toFixed(2)
}

// -----END VMAX-----

// -----FULL ART TRAINER CARDS-----

var trainer = document.querySelector("#trainer");

function setTrainerQuantity(element) {
    trainer.innerText = element.value;
}

function calcTrainer(){
    var trainer = document.querySelector("#trainer");

    num2 = 1.00;
    document.getElementById("resultTrainer").innerHTML = (trainer.innerText * num2).toFixed(2)
}

// -----END FULL ART TRAINER-----

// -----RAINBOW RARE CARDS-----

var rainbow = document.querySelector("#rainbow");

function setRainbowQuantity(element) {
    rainbow.innerText = element.value;
}

function calcRainbow(){
    var rainbow = document.querySelector("#rainbow");

    num2 = 2.50;
    document.getElementById("resultRainbow").innerHTML = (rainbow.innerText * num2).toFixed(2)
}

// -----END RAINBOW RARE-----

// -----GOLD RARE CARDS-----
var gold = document.querySelector("#gold");

function setGoldQuantity(element) {
    gold.innerText = element.value;
}

function calcGold(){
    var gold = document.querySelector("#gold");

    num2 = 1.50;
    document.getElementById("resultGold").innerHTML = (gold.innerText * num2).toFixed(2)
}

// -----END GOLD RARE-----

// -----GRAND TOTAL-----

function grandTotal(){
    var sum = 0
    var whatever = document.querySelectorAll(".bigTotal")

    whatever.forEach((element)=>{
        sum += parseFloat(element.innerText)
        console.log(element.innerText,sum)})
        document.getElementById("resultGrandTotal").innerHTML = (sum).toFixed(2)
}

function cardTotal(){
    var sum = 0
    var total = document.querySelectorAll(".cardTotal")

    total.forEach((element)=>{
        sum += parseInt(element.innerText)
        console.log(element.innerText,sum)})
        document.getElementById("cardTotal").innerHTML = sum + " card(s)"
}

function percentTotal(){
    var sum = 0
    var percent = document.querySelectorAll(".bigTotal")

    percent.forEach((element)=>{
        sum += parseFloat(element.innerText)
        console.log(element.innerText,sum)})
        document.getElementById("resultExtraTotal").innerHTML = (sum * 1.2).toFixed(2)
}

// -----COOKIE BOX-----
var cookieDiv = document.querySelector("#alertBox")

function removeCookie(){
    cookieDiv.remove();
}