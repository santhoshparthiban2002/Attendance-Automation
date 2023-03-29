const currentYear = new Date().getFullYear();
const currentmonth = new Date().getMonth();
document.getElementById("year").innerHTML = currentYear;
document.getElementById("yoi").innerHTML = currentmonth;
var daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
document.getElementById("bigday").innerHTML = daysOfWeek[new Date().getDay()];
document.getElementById("bigno").innerHTML = new Date().getDate();
mons(currentmonth)
document.getElementById("next").addEventListener("click", nextValue);
document.getElementById("previous").addEventListener("click", previousValue);


function changebig(a) {
    for (var i = 1 ; i <= 42; i++) {
		document.getElementById("w"+String(i)).classList.remove("circle");
	}
    document.getElementById("bigno").innerHTML = a.innerHTML;
    const x = document.getElementById("year").innerHTML;
    const y = document.getElementById("yoi").innerHTML;
    var daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var date = new Date(parseInt(x), parseInt(y), parseInt(a.innerHTML));
    var dayOfWeek = daysOfWeek[date.getDay()];
    document.getElementById("bigday").innerHTML = dayOfWeek;
    console.log(a.id)
    document.getElementById(a.id).classList.add("circle");
}


function nextValue() {
    for (var i = 1 ; i <= 42; i++) {
		document.getElementById("w"+String(i)).classList.remove("circle");
	}
  const val1 = document.getElementById("year").innerHTML;
  document.getElementById("year").innerHTML = parseInt(val1) + 1;
  mons(currentmonth)
}

function previousValue() {
    for (var i = 1 ; i <= 42; i++) {
		document.getElementById("w"+String(i)).classList.remove("circle");
	}

  const val2 = document.getElementById("year").innerHTML;
  document.getElementById("year").innerHTML = parseInt(val2) - 1;
  
  mons(currentmonth)
}

function mons(a) {

    for (var i = 1 ; i <= 42; i++) {
		document.getElementById("w"+String(i)).innerHTML=""
        document.getElementById("w"+String(i)).classList.remove("circle");
	}
    const val1 = document.getElementById("year").innerHTML;
    document.getElementById("yoi").innerHTML = a
    var daysInMonth = new Date(parseInt(val1),parseInt(a)+ 1, 0).getDate();
    var firstDayOfMonth = new Date(parseInt(val1),parseInt(a), 1).getDay();
    for (var i = 0 ; i < firstDayOfMonth; i++) {
		document.getElementById("w"+String(i+1)).innerHTML=""
	}
    for (var i = 0 ; i < daysInMonth; i++) {
		document.getElementById("w"+String(firstDayOfMonth + i +1 )).innerHTML=i+1
	}

  }




  