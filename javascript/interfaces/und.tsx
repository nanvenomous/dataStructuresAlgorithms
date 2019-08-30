
interface LabelledValue {
	label: string;
}

// automatically checks the sape of LabelledObj against the definition ^ of LabelledValue
function printLabel(labelledObj: LabelledValue) {
	console.log(labelledObj.label);
}

let myObj = {size: 10, label: "Size 10 Object"};
printLabel(myObj);