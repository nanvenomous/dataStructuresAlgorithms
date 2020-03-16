const redux = require('redux');

const reducer = (state = [], action) => {
	if (action.type === 'split_string') {
		return action.payload.split('');
	} else if (action.type === 'add_character') {
		return [ ...state, action.payload];
	}
	return state;
};

const store = redux.createStore(reducer);

console.log(store.getState());

const action = {
	type: 'split_string',
	payload: 'asdf',
};

store.dispatch(action);

console.log(store.getState());

const action2 = {
	type: 'add_character',
	payload: 'g',
};

store.dispatch(action2);
console.log(store.getState());
