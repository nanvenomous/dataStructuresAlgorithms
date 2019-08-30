function getTime() {
  let today = new Date(Date.now());
  // Future time for delayed responses
  let future = new Date(Date.now());
  future.setSeconds(future.getSeconds() + 12);
  return {
    utc: Date.UTC(
      today.getFullYear(),
      today.getMonth(),
      today.getDate(),
      today.getHours(),
      today.getMinutes(),
      today.getSeconds(),
      today.getMilliseconds(),
    ),
    today: today,
    future: future,
  };
}

console.log(getTime().today)
console.log(getTime().future)
