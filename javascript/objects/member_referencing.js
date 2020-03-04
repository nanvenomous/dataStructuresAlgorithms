export const reference = (object, member_array) =>
  member_array.reduce((xs, x) =>
    (xs && xs[x]) ? xs[x] : null, object)