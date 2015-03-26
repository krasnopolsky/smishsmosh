//**************rand functions*************//

function bringToFront(x)  {
for(var i = 1; i <= cardCounter; i++)  {
	e = document.getElementById(i).style.zIndex = i;
	}
document.getElementById(x).style.zIndex = i++;
}

function randomHexColor() {
return '#'+Math.floor(Math.random()*16777215).toString(16);

}

function changeColor(x)  {
var p = document.getElementsByClassName("part");

for(var i = 0; i < p.length; i++)  {
	p[i].style.backgroundColor = x;
	}

}

function changeCSS(x)  {
var p = document.getElementsByClassName("part");

for(var i = 0; i < p.length; i++)  {
	p[i].style.border = x;
	}

}

function changeCSS2(x)  {
var p = document.getElementsByClassName("part");

for(var i = 0; i < p.length; i++)  {
	p[i].style.borderWidth = x;
	}

}

function changeCSS3(x)  {
var p = document.getElementsByClassName("divHolder");
var w = "8px";
for(var i = 0; i < p.length; i++)  {
	p[i].style.border = x;
	p[i].style.borderWidth = w;
	}

}

function changeCSS4(x)  {
var p = document.getElementsByClassName("part");
for(var i = 0; i < p.length; i++)  {
	p[i].style.border = x;
	p[i].style.padding = x;
	}

}


function changeTextColor(x)  {
var p = document.getElementsByClassName("part");
for(var i = 0; i < p.length; i++)  {
	p[i].style.color = x;
	}

}

function moveCards(x, y)  {
var p = document.getElementsByClassName("part");
if(x == "line")  {
alert(x);
for(var i = 0; i < p.length; i++)  {
	p[i].style.Top = "0px";
	$("#draggable").simulate("drag-n-drop", {dx: x, dy: y, interpolation: { stepWidth: 1, stepDelay: 1}});
	}
}
else  {

}

}

