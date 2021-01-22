let xs = [-4,-5];

let prefixSum = xs.map((prev => curr => prev += curr)(0));
let sumRange = (i,j) => (i > 0) ? prefixSum[j] - prefixSum[i-1] : prefixSum[j];

console.log(sumRange(0,0))