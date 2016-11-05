Title:		Find a tricky bug
Slug:			find-a-tricky-bug
Date:			2016-10-09
Status:		Draft
Category: Diary
Tags:			javascript, algorithm
Authors:	Maciej Sypień
<!-- Summary: Sample summary -->

<div class="intro-article-image-sm" markdown="1">
  ![Linux logo]({filename}/images/linux_logo_pinguin.jpg)
</div>

Find the difference between those to code snippets and why one of them is wrong.

```javascript
// fibonacci
function solution (numb) {
	numb = parseInt(numb)
  result = [0,1]
  for (var i=1; i<=(numb - result.length); i++) {
  	console.log(i)
    result[i+1] = result[i-1] + result[i]
  }
  return result.join(", ");
}

console.log(solution(90));
```

```javascript
// fibonacci
function solution (numb) {
	numb = parseInt(numb)
  result = [0,1]
  len = numb - result.length // numb.lenght - 2 from result arr = final
  for (var i=1; i<=len; i++) {
  	console.log(i)
    result[i+1] = result[i-1] + result[i]
  }
  return result.join(", ");
}

console.log(solution(90));
```


[github]: https://github.com

