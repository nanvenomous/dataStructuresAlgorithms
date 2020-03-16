import {reference} from '../member_referencing';

const mock_object = {
	'one': 1,
	'two': {
		'a': {
			'i': 4,
			'ii': 7
		},
		'b': 3
	}
};


describe('reference', () => {
  test('should properly reference object', () => {
		expect(reference(mock_object, ['two', 'a', 'ii'])).toEqual(7);
  });
  test('should return null when member doesnt exist', () => {
		expect(reference(mock_object, ['two', 'z', 'ii'])).toBeNull();
  });
  test('should return null when object doesnt exist', () => {
		expect(reference(undefined, ['two', 'a', 'ii'])).toBeNull();
  });
});