if (!localStorage.getItem("counter")) {
    // jika tidak tersedia "counter" pada localStorate maka declare "counter"
    localStorage.setItem("counter", 0)
}

function count() {
    let counter = localStorage.getItem("counter");
    counter++;
    document.getElementById('count_text').innerHTML = counter;

    localStorage.setItem("counter", counter);
    
    /*
    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`);
    };
    */
};

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector("#count_text").innerHTML = localStorage.getItem("counter");
    // bind button
    document.getElementById("count_button").onclick = count;
    
    //setInterval(count, 1000);
})