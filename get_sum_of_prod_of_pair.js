function getSum(vector, result = 0) {
    if (vector.length == 1) {
      return result;
    }

    let sumPair = 0;

    for (let i = 1; i < vector.length; ++i) {
      sumPair = vector[0] * vector[i];
      
      result += sumPair
    }

    vector.shift();
    return getSum(vector, result);
  }

console.log("Sum: " + getSum([1, 2, 3]));
