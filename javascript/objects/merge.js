const obj = {
	one: 1,
	two: "two"
};

const newobj = {...obj, ...{ three: 3, four: "four" }};

console.log(newobj);