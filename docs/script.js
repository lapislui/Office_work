    // alert("Welcome to sigzen");
document.writeln("okayari");
document.writeln("hi")
console.log("webpage log");
var x=5
if (x==5) {
    console.log("output is true");
}

function example() {
    if (true) {
        let bv = "keval";
        console.log(bv);
    }

}
example();

let fn = "keval";
let ln = 'patel';
let num1 =100;
let num2 = 96.5;
let true_bool = true;
let false_bool = false;

document.writeln(typeof(num1)," = ",num1);
document.writeln("<br>\n true bool"," = ",true_bool);
document.writeln("<br>false bool"," = ",typeof(false_bool));

let a=0
while (a<10) {
    document.writeln("<br>",a);
    a++;
}
// let x = 10<20;
// document.write("<br>",x);

if (a<6) {
    document.writeln("<br> a is less than 6 = ",a);
} else {
    document.writeln("<br> a is greater than 6 = ",a);
}

switch (a) {
    case 10:
        document.writeln('<br> this is switch case ');
        break;

    default:
        break;
}

function name(firstname,lastname) {
    document.writeln('<br> name is'+firstname+lastname);
}
name(" keval ","patel");

function display(result){
    document.writeln('<br>',result);
}
function add(n1,n2,cb){
    let sum = n1 + n2;
    cb(sum)
}

add(10,20,display);

//annonymous function
let sum = function (n1,n2) {
    return n1+n2;
}

document.writeln('<br>',sum(10,20));

(
    function () {
        document.writeln('<br> wolcome to sigzem');
    }
)();

// setTimeout(function () {
//     document.writeln('<br> this is timeout func');
// },2000);

const name1={
    firstname:"keval",
    lastname:"patel",
    age:20,
    skills:{
        "software development":"python",
        "framework":"frappe",
        "database":"mysql",
        "operating system":"windows,linux",
        "android dev":"java"
    }
}

document.writeln('<br> ',name1);
document.writeln('<br> ',name1.firstname);
document.writeln('<br> ',name1["lastname"]);

name1.firstname="techguru"

delete name1.age;

document.writeln('<br> ',name1);
document.writeln('<br> ',name1.firstname);
document.writeln('<br> ',name1["lastname"]);
document.writeln('<br> ',name1.skills["operating system"]);
document.writeln('<br>');
for(let porp in name1){
    document.writeln((name1[porp]));

}

const name1 = new Object();
name1.firstname = "keval";
name1.lastname = "patel";
name1.age = 20;

document.writeln('<br>',name1);

//js object method

const name1 = {
    firstname: "keval",
    lastname: "patel",
    greet: function greet(){
        document.writeln('<br>hello world');
    }
}
name1.greet();
