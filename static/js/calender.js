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
  if(a.innerText != ""){
    document.getElementById("bigno").innerHTML = a.innerHTML;
    const x = document.getElementById("year").innerHTML;
    const y = document.getElementById("yoi").innerHTML;
    var daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var date = new Date(parseInt(x), parseInt(y), parseInt(a.innerHTML));
    var dayOfWeek = daysOfWeek[date.getDay()];
    document.getElementById("bigday").innerHTML = dayOfWeek;
    const calender_box = document.getElementById("calender_box");
    calender_box.classList.remove("bg-success","bg-primary","bg-warning","bg-danger","text-light");
    if (a.classList.contains("bg-success")) {
      calender_box.classList.add("bg-success","text-light");
      document.getElementById("status").innerText = "Present";
      
    }
    else if (a.classList.contains("bg-danger")) {
      calender_box.classList.add("bg-danger","text-light");
      document.getElementById("status").innerText = "Absent";
    }
    else if (a.classList.contains("bg-warning")) {
      calender_box.classList.add("bg-warning","text-light");
      document.getElementById("status").innerText = "Late";
    }
    else if (a.classList.contains("bg-primary")) {
      calender_box.classList.add("bg-primary","text-light");
      document.getElementById("status").innerText = "Holiday";
    }

    console.log(a.id)
   
    document.getElementById(a.id).classList.add("circle");
}
}
console.log(myData1);
console.log(myData2);
console.log(myData3);



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
  removehighlight()
  month_highlight(a);

    for (var i = 1 ; i <= 42; i++) {
		document.getElementById("w"+String(i)).innerHTML=""
        document.getElementById("w"+String(i)).classList.remove("circle");
	}
    const val1 = document.getElementById("year").innerHTML;
    document.getElementById("yoi").innerHTML = a
    var daysInMonth = new Date(parseInt(val1),parseInt(a)+ 1, 0).getDate();
    var firstDayOfMonth = new Date(parseInt(val1),parseInt(a), 1).getDay();
    for (var i = 0 ; i < firstDayOfMonth; i++) {
		document.getElementById("w"+String(i+1)).innerHTML="";
	}
    for (var i = 0 ; i < daysInMonth; i++) {
		let days_ot = document.getElementById("w"+String(firstDayOfMonth + i +1 ));
    days_ot.innerHTML=i+1;
    

	}
 


  for (var i = 1 ; i <= 42; i++) {

  let days_ot = document.getElementById("w"+String(i));
  let cut_date = String(days_ot.innerText)+"-"+""+String(parseInt(a)+ 1)+"-"+String(val1);
  const [day, month, year] = cut_date.split('-');
  const formattedDay = day.padStart(2, '0');
  const formattedMonth = month.padStart(2, '0');
  let join_date =  `${formattedDay}-${formattedMonth}-${year}`;
  let is_present,status = attendance(join_date);
  let is_holiday = holidays(join_date);
  if(is_present,status){
    days_ot.classList.add("text-light");
    if(status === 1){
      days_ot.classList.add("bg-success"); 
    }
    else if(status === 2){
      days_ot.classList.add("bg-warning"); 
    }
    else if(status === 3){
      days_ot.classList.add("bg-danger"); 
    }
  }

  if(is_holiday){
    days_ot.classList.add("bg-primary"); 
    days_ot.classList.add("text-light");
  }


  }





  }


function attendance(highlight) {
  for (let i = 0; i < myData1.length; i++) {
    const obj = myData1[i];

    if (obj.date === highlight) {
      console.log(obj.date );
      if(obj.status === "PRESENT"){
        return true,1
      }
      else if(obj.status === "LATE"){
        return true,2
      }
      else if(obj.status === "ABSENT"){
        return true,3
      }
     
    }
  }
}

function holidays(highlight) {
  for (let i = 0; i < myData2.length; i++) {
    const obj = myData2[i];

    if (obj.date === highlight) {
      console.log(obj.date );
      return true; // terminate function execution if match is found
    }
  }
}


function month_highlight(highlight) {
  for (let i = 0; i < 12; i++) {
    let hmonth = document.getElementById("m"+String(parseInt(i)+ 1));
    hmonth.classList.remove("hmonth"); 
    hmonth.classList.remove("text-light"); 
    hmonth.classList.remove("rounded-pill"); 
    hmonth.classList.remove("p-1"); 
   
  }
  let hmonth = document.getElementById("m"+String(parseInt(highlight)+ 1));
  hmonth.classList.add("hmonth"); 
  hmonth.classList.add("text-light"); 
  hmonth.classList.add("rounded-pill")
  hmonth.classList.add("p-1")
}


function removehighlight(){
  for (var i = 1 ; i <= 42; i++) {
    let days_ot = document.getElementById("w"+String(i));
    days_ot.classList.remove("bg-danger"); 
    days_ot.classList.remove("text-light");
    days_ot.classList.remove("bg-success");
    days_ot.classList.remove("bg-warning");
    days_ot.classList.remove("bg-primary");
  }
}