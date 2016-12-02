Title:		Angular 2 observables
Slug:			angular-2-observables
Date:			2016-12-01
Status:		Draft
Category: Diary
Tags:			angular2, typescript
Authors:	Maciej Sypień
<!-- Summary: Sample summary -->

<div class="intro-article-image-sm" markdown="1">
  ![Linux logo]({filename}/images/linux_logo_pinguin.jpg)
</div>

observables can be stopped during the request. In compare to promises cannot do this.
```typescript
import {Observable} from "rxjs/Observable"
import "rxjs/Rx"

let stream = new Observable(observer => {
  let timeout = setTimeout(() => {
    observer.next('observable timeout')
  }

  return () => {
    clearTimeout(timeout);
  }
}

stream.subscribe(value => console.log(value))
```


Async operation over the time. Promises cannot do this.
It can be Array object changed over the time.

```typescript
import {Observable} from "rxjs/Observable"
import "rxjs/Rx"

let stream = new Observable(observer => {
  let count = 0;
  let timeout = setimeout(() => {
    observer.next('observable timeout')
  }

  return () => {
    cleartimeout(timeout);
  }
}

stream.subscribe(value => console.log(value))
```

Operators:
-   filter


[github]: https://github.com

