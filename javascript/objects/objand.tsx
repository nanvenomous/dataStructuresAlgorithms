interface oneObj {
	fir: true;
	sec: false;
	thir: true;
}

interface twoObj {
	first: true;
	second: true;
	third: true;
}

type combination = oneObj & twoObj;


console.log(combination);