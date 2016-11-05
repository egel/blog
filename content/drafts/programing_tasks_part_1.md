Title:		Solving programing tasks - part 1
Slug:			solving-programing-tasks-part-1
Date:			2016-10-08
Status:		Draft
Category: Diary
Tags:			javascript, algorithm
Authors:	Maciej Sypień

<div class="intro-article-image-sm" markdown="1">
  ![Linux logo]({filename}/images/linux_logo_pinguin.jpg)
</div>


# Task 1
Write method that calculate `n!`

```javascript
function factorial (num) {
  num = parseInt(num)
	if (num <= 0) return 'not valid'
  if (num <= 2) return num
  var result = 1;
  for (i=2; i<=num; i++) {
 		result *= i;
  }
	return result;
}
```


# Bubble sort method
-   input `[4, 2, 5, 1, 7]`
-   output `[1, 2, 4, 5, 7]`

```javascript
function bubble (arr) {
  if (Object.prototype.toString.call(arr) !== '[object Array]') return 'not valid'

  do {
  	n=0
    for (var i=0; i<=(arr.length-1); i++) {
      console.log('+')
 			if (arr[i] > arr[i+1]) {
    		var tmp = arr[i]
      	arr[i] = arr[i+1]
      	arr[i+1] = tmp
        n+=1
    	}
  	}
  } while (n>0)
	return arr;
}


console.log(bubble( [4, 2, 5, 1, 7]));
```

## fibonacci
```javascript
// fibonacci
function solution (numb) {
	numb = parseInt(numb)
  result = [0,1]
  len = numb - result.length // numb.lenght - 2 from result arr = final
  for (var i=1; i<=len; i++) {
    result[i+1] = result[i-1] + result[i]
  }
  return result.join(", ");
}

console.log(solution(90));
```

## Index exuilibrum of array
```javascript
// Codility Exuilibrum index
function solution (A, N) {
  // 0 <= P < N
  // N <= 100000
  // each element of A => −2,147,483,648 - 2,147,483,647
	var sumLeft = 0
  var sumRight = 0
  for (var i=0; i<N; i++) {
  	if (typeof A[i-1] !== 'undefined') sumLeft += A[i-1]
    sumRight=0
    for (var k=i+1; k<N; k++) {
    	sumRight += A[k]
    }
    if (sumLeft === sumRight) return i
  }
  return -1
}

//console.log(solution([-1, 3, -4, 5, 1, -6, 2, 1], 8)) // 1, 3, 7
console.log(solution([3,2,-5,1], 4)) // 3
```

## Merge 2 object into one

```javascript
function extend (dest, source) {
  for (var key in source) {
    if (source.hasOwnProperty(key)) dest[key] = source[key]
  }
  return dest
}
```


[github]: https://github.com

