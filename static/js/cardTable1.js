/*Things to add
drawing a site card

add card to top 0 right 0 or anywhere really
add card management
	add card
	remove card
tally power when cards fill a box aka are present at a site

start of a game
	shuffle
	draw a hand
	place starting cards
	sites
	
	

*/

//**********card type Logic**************
function drawCard(d, x)  {
var div = d; //div to draw card onto
var cardId = x; //the card's DB id number

var cardTypeNum = Math.floor( Math.random() * 14 ) + 1;

var str = cardTypeNum.toString();

str = "15";

switch(str)  {

	case "1":
		drawSite(d, x);
		break;
	case "2":
		drawCreature(d, x);
		break;
	case "3":
		drawBasic(d, x);
		break;
	case "4":
		drawBasic(d, x);
		break;
	case "5":
		drawCard1(d, x);
		break;
	case "6":
		drawCard1(d, x);
		break;
	case "7":
		drawCard2(d, x);
		break;
	case "8":
		drawCard2(d, x);
		break;
	case "9":
		drawCard2(d, x);
		break;
	case "10":
		drawCard2(d, x);
		break;
	case "11":
		drawCard2(d, x);
		break;
	case "12":
		drawCard2(d, x);
		break;
	case "13":
		drawCard3(d, x);
		break;
	case "14":
		drawCard3(d, x);
		break;
	case "15":
		drawCard4(d, x);
		break;
	case "Location":
		drawSite(d, x);
		break;
	case "Creature":
		drawCreature(d, x);
		break;
	case "Admiral's Order":
		drawBasic(d, x);
		break;
	case "Objective":

		drawBasic(d, x);
		break;
	case "Epic Event":
		drawCard1(d, x);
		break;
	case "Jedi Test":
		drawCard1(d, x);
		break;
	case "Defensive Shield":
		drawCard2(d, x);
		break;
	case "Effect":
		drawCard2(d, x);
		break;
	case "Interrupt":
		drawCard2(d, x);
		break;
	case "Podracer":
		drawCard2(d, x);
		break;
	case "Weapon":
		drawCard2(d, x);
		break;
	case "Device":
		drawCard2(d, x);
		break;
	case "Starship":
		drawCard3(d, x);
		break;
	case "Vehicle":
		drawCard3(d, x);
		break;
	case "Character":
		drawCard4(d, x);
		break;
	default:
		alert("we lost");
}

}

//***********Drawing the card**************/

function drawBasic(d, x)  {
var div = document.getElementById(d);
//div.innerHTML = "drawBasic";
div.appendChild(drawTop(x));
div.appendChild(drawPic(x));
div.appendChild(drawText(x));


}

function drawSite(d, x)  {

var div = document.getElementById(d);
div.innerHTML = "drawSite --fuck you site!!";

}

function drawCreature(d, x)  {
var div = document.getElementById(d);
//div.innerHTML = "drawCreature "+x;
div.appendChild(drawTop(x));
div.appendChild(drawLore(x));
div.appendChild(drawPic(x));
div.appendChild(drawInfo(x));
div.appendChild(drawText(x));
}

function drawCard1(d, x)  {
var div = document.getElementById(d);
//div.innerHTML = "drawCard1 "+x;
div.appendChild(drawTop(x));
div.appendChild(drawPic(x));
div.appendChild(drawBar(x));
div.appendChild(drawText(x));
}

function drawCard2(d, x)  {
var div = document.getElementById(d);
//div.innerHTML = "drawCard "+x;
div.appendChild(drawTop(x));
div.appendChild(drawLore(x));
div.appendChild(drawPic(x));
div.appendChild(drawBar(x));
div.appendChild(drawText(x));
}

function drawCard3(d, x)  {
var div = document.getElementById(d);
//div.innerHTML = "drawCard "+x;
div.appendChild(drawTop(x));
div.appendChild(drawLore(x));
div.appendChild(drawPic(x));
div.appendChild(drawBar(x));
div.appendChild(drawInfo(x));
div.appendChild(drawText(x));
}

function drawCard4(d, x)  {
var div = document.getElementById(d);
//div.innerHTML = "drawCard "+x;
div.appendChild(drawTop(x));
div.appendChild(drawLore(x));
div.appendChild(drawPic(x));
div.appendChild(drawInfo(x));
div.appendChild(drawLeft(x));
div.appendChild(drawRight(x));
div.appendChild(drawText(x));


}

//*********Drawing of Card Parts***************//

function drawTop(x)  {
var cp1 = document.createElement("div");
cp1.setAttribute("class", "part");
cp1.style.height = "8%";
cp1.style.backgroundColor = randomHexColor();
cp1.innerHTML = "Card type || Card name || Destiny #";
return cp1;
}

function drawLore(x)  {
var cp1 = document.createElement("div");
cp1.setAttribute("class", "part");
cp1.style.height = "10%";
cp1.style.fontSize = "x-small";
cp1.style.backgroundColor = randomHexColor();
cp1.innerHTML = "drawLore || some shit about the card that only the super nerds read and care about. Look at this nerd reading the lore. Nerd.";
return cp1;
}

function drawPic(x)  {
var cp1 = document.createElement("div");
cp1.setAttribute("class", "part");
cp1.style.height = "45%";
cp1.style.backgroundImage = "url('/img/cardpic.jpg')";
cp1.style.backgroundSize = "250px 100%";
cp1.style.backgroundColor = randomHexColor();
cp1.innerHTML = "drawPic ||  "+x;
return cp1;
}

function drawBar(x)  {
var cp1 = document.createElement("div");
cp1.setAttribute("class", "part");
cp1.style.height = "5%";
cp1.style.textAlign = "center";
cp1.style.backgroundColor = randomHexColor();
cp1.innerHTML = "drawBar ||  "+x;
return cp1;
}

function drawInfo(x)  {
var cp1 = document.createElement("div");
cp1.setAttribute("class", "part");
cp1.style.height = "8%";
cp1.style.textAlign = "center";
cp1.style.backgroundColor = randomHexColor();
cp1.innerHTML = "Power || Defense || Movement";
return cp1;
}

function drawText(x)  {
var cp1 = document.createElement("div");
cp1.setAttribute("class", "part");
cp1.style.height = "29%";
cp1.style.paddingLeft = "8%";
cp1.style.paddingRight = "8%";
cp1.style.backgroundColor = randomHexColor();
cp1.innerHTML = "drawText ||  The read meat of the game. This is what puts the 'c' in swccg. This shit right here is where it is at. Read this shit to win.";
return cp1;
}

function drawLeft(x)  {
var cp1 = document.createElement("div");
cp1.setAttribute("class", "part");
cp1.style.height = "10%";
cp1.style.backgroundColor = randomHexColor();
cp1.style.width = "5%";
cp1.innerHTML = "L";
cp1.style.cssFloat="left";
return cp1;
}

function drawRight(x)  {
var cp1 = document.createElement("div");
cp1.setAttribute("class", "part");
cp1.style.height = "10%";
cp1.style.width = "5%";
cp1.style.backgroundColor = randomHexColor();
cp1.innerHTML = "R";
cp1.style.cssFloat="right";
return cp1;
}

//************adding cards to table****************//
var cardCounter = 0;

function addRandomCard() {

var randCard = Math.floor( Math.random() * 3442 ) + 1;

cardCounter++;

var c = document.getElementByTagName("body");

var cardH = 343;
var cardW = 250; 

	var imgDiv = document.createElement("div");
	imgDiv.setAttribute("id", cardCounter);
	imgDiv.setAttribute("cid", randCard);
	imgDiv.setAttribute("class", "divHolder");
	imgDiv.style.height = cardH+"px";
	imgDiv.style.width = cardW+"px";
	imgDiv.style.top = "0px";
	imgDiv.style.left = "0px";
	imgDiv.style.backgroundColor = randomHexColor();
//	imgDiv.style.backgroundImage = "url('img/'+i+'.JPG')";
	imgDiv.style.zIndex = cardCounter;
	imgDiv.setAttribute("onclick", "bringToFront("+cardCounter+")");
	c.appendChild(imgDiv);

	drawCard(cardCounter, randCard);

	makeDraggable(cardCounter);
	
	

}

function makeDraggable(x) {
$( "#"+x ).draggable();
}

function addThisCard()  {
var cId = document.getElementById("cardId").value;

cardCounter++;

var c = document.getElementById("cardTable");

var cardH = 343;
var cardW = 250; 

	var imgDiv = document.createElement("div");
	imgDiv.setAttribute("id", cardCounter);
	imgDiv.setAttribute("cid", cId);
	imgDiv.setAttribute("class", "divHolder");
	imgDiv.style.height = cardH+"px";
	imgDiv.style.width = cardW+"px";
	imgDiv.style.top = "0px";
	imgDiv.style.left = "0px";
	imgDiv.style.backgroundColor = randomHexColor();
//	imgDiv.style.backgroundImage = "url('img/'+i+'.JPG')";
	imgDiv.style.zIndex = cardCounter;
	imgDiv.setAttribute("onclick", "bringToFront("+cardCounter+")");
	c.appendChild(imgDiv);

	drawCard(cardCounter, cId);

	makeDraggable(cardCounter);


}

function bringToFront(x)  {
for(var i = 1; i <= cardCounter; i++)  {
	e = document.getElementById(i).style.zIndex = i;
	}
document.getElementById(x).style.zIndex = i++;
}


function randomHexColor() {
return '#'+Math.floor(Math.random()*16777215).toString(16);

}

//**************rand functions*************//


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
alert(x, y);
for(var i = 0; i < p.length; i++)  {
	p[i].style.Top = "0px";
	//$("#draggable").simulate("drag-n-drop", {dx: x, dy: y, interpolation: { stepWidth: 1, stepDelay: 1}});
	}
}
else  {

}

}
