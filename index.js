// Lambda function trigger
const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://dafbprumukerwlot2pqi3jg7o40orqxd.lambda-url.us-west-1.on.aws/");
    let data = await response.json();
    counter.innerHTML = ` Views: ${data};`
}
updateCounter();