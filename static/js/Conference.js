document.getElementById("Workshop").addEventListener('change', enableGroup);
document.getElementById("H").addEventListener('click', changeTitle2);
const button = document.getElementById("submit");
button.addEventListener("click", mustselect);
document.getElementById("nominees").addEventListener("click", nominees);
document.getElementById("A1").addEventListener("click", votecount);
document.getElementById("A2").addEventListener("click", votecount1);
document.getElementById("A3").addEventListener("click", votecount2);


function register() {
    if (document.getElementById("idnum").value.length==0){
        document.cookie = "123456" + "=" +  document.getElementById("fname").value + ","+ document.getElementById("lname").value
            + ","+ document.getElementById("address1").value +","+ document.getElementById("city").value +","+ document.getElementById("state").value
            +","+ document.getElementById("zipcode").value +","+ document.getElementById("tel").value +","+ document.getElementById("email").value;

    }
    else{
        document.cookie = document.getElementById("idnum").value + "=" +  document.getElementById("fname").value + ","+ document.getElementById("lname").value
            + ","+ document.getElementById("address1").value +","+ document.getElementById("city").value +","+ document.getElementById("state").value
            +","+ document.getElementById("zipcode").value +","+ document.getElementById("tel").value +","+ document.getElementById("email").value;
    }

}

function populate(){
let cookieFields = document.cookie.split(',');
if (document.getElementById("idnum").value=='123456')
{

    for (let i=0; i<cookieFields.length;i++)
    {
        let fname = cookieFields[0].split('=');
        document.getElementById("fname").value=fname[1];
        document.getElementById("lname").value=cookieFields[1];
        document.getElementById("address1").value=cookieFields[2];
        document.getElementById("city").value=cookieFields[3];
        document.getElementById("state").value=cookieFields[4];
        document.getElementById("zipcode").value=cookieFields[5];
        document.getElementById("tel").value=cookieFields[6];
        document.getElementById("email").value=cookieFields[7];


    }
}
else
{
    //alert("welcome to the club!");
}

}


function enableGroup() {

    if (document.getElementById("B").checked) {
        alert("If you select B, you cannot select workshops in session 2.");
        document.getElementById("D").disabled = true;
        document.getElementById("E").disabled = true;
        document.getElementById("F").disabled = true;
        if (document.getElementById("D").checked || document.getElementById("E").checked |
            document.getElementById("F").checked) {
            alert("Removing your selection for session 2 as you've selected B")
            document.getElementById("D").checked = false;
            document.getElementById("E").checked = false;
            document.getElementById("F").checked = false;
        }
        if (document.getElementById("H").checked) {
            document.getElementById("H").checked = false;
        }
    } else if (!(document.getElementById("B").checked)) {
        document.getElementById("D").disabled = false;
        document.getElementById("E").disabled = false;
        document.getElementById("F").disabled = false;
    }


    if (document.getElementById("F").checked) {
        alert("if you select F, you must also take H. and cannot select" +
            "G or I");
        document.getElementById("G").disabled = true;
        document.getElementById("I").disabled = true;
        document.getElementById("H").checked = true;
    }

    if (!(document.getElementById("F").checked)) {
        document.getElementById("G").disabled = false;
        document.getElementById("I").disabled = false;
        document.getElementById("H").checked = false;
    }
}

function changeTitle2() {
    if (!(document.getElementById("F").checked)) {
        alert("You cannot take H unless you signed up for F");
    }
}


if (document.getElementById("B").checked) {
    if (document.getElementById("D").checked) {
        window.print();
    } else if (document.getElementById("E").checked) {
        window.print();
    } else if (document.getElementById("F").checked) {
        window.print();
    }

    function mustselect() {
        if (document.getElementById("B").checked) {
            if (document.getElementById("D").checked || document.getElementById("E").checked |
                document.getElementById("F").checked) {
                window.open(href = "popup.html", 'width=500,height=200,centered=true');
            }
            if (document.getElementById("H").checked) {

                window.open(href = "popup.html", 'width=500,height=200,centered=true');
            }

        }
    }
    document.getElementById("result").innerHTML = localStorage.getItem("votes");
    document.getElementById("result1").innerHTML = localStorage.getItem("votes1");
    document.getElementById("result2").innerHTML = localStorage.getItem("votes2");

    function nominees() {
        const ele = document.getElementsByName('mostcreative');
        for (let i = 0; i < ele.length; i++) {

            if (ele[i].checked) {
                alert("Thank you for voting for:" + ele[i].value);
                break;
            }

        }
    }

    function votecount() {

        let numOfVotes;
        if (isNaN(parseInt(localStorage.getItem("votes")))) {
            numOfVotes = 0;
        } else {
            numOfVotes = parseInt(localStorage.getItem("votes"));
        }
        numOfVotes = numOfVotes + 1;
        localStorage.setItem("votes", numOfVotes.toString());
        document.getElementById("result").innerHTML = localStorage.getItem("votes");

    }

    function votecount1() {

        let numOfVotes1;
        if (isNaN(parseInt(localStorage.getItem("votes1")))) {
            numOfVotes1 = 0;
        } else {
            numOfVotes1 = parseInt(localStorage.getItem("votes1"));
        }
        numOfVotes1 = numOfVotes1 + 1;
        localStorage.setItem("votes1", numOfVotes1.toString());
        document.getElementById("result1").innerHTML = localStorage.getItem("votes1");

    }

    function votecount2() {
        let numOfVotes2;
        if (isNaN(parseInt(localStorage.getItem("votes2")))) {
            numOfVotes2 = 0;
        } else {
            numOfVotes2 = parseInt(localStorage.getItem("votes2"));
        }
        numOfVotes2 = numOfVotes2 + 1;
        localStorage.setItem("votes2", numOfVotes2.toString());
        document.getElementById("result2").innerHTML = localStorage.getItem("votes2");

    }
}