const fd = require("./fetchedData");

let test_arr = [
  {"age":38,"hobby":"computing","name":"Max"},
  {"age":63,"hobby":"movies","name":"Alex"},
  {"age":8,"hobby":"languages","name":"Sonya"},
  {"age":4,"hobby":"smartphones","name":"Sasha"}
]
let test_single_doc = {"age":4,"hobby":"smartphones","name":"Sasha"}

describe('fetching', () => {
  test('fetching array ', async() => {
    expect(await fd("http://127.0.0.1:4321/", []))
    .toEqual(test_arr)
  });
  test('fetching single_doc', async() => {
    expect(await fd("http://127.0.0.1:4321/doc"))
    .toEqual(test_single_doc)
  });
});
