Title:      Nginx configuration for AngularJS cloud project with Apiary
Date:       2016-04-13 12:44
Status:     published
Category:   Diary
Tags:       angularjs, nginx, apiary, frontend
Authors:    Maciej Sypień


<div class="intro-article-image-sm" markdown="1">
  ![Logo of Sublime Text 3]({filename}/images/nginx_logo.png)
</div>

Recently I have been working on some cloud project with my coworkers. We used
 [AngularJS][angularjs-webpage] as frontend framework and
[Apiary][apiary-webpage] as a backend bridge for RESTful API, while the real
backend was being built.

The main gole for proper nginx configuration was to serve `*.example.dev`
domains, but with some exceptions (restrictions) for subdomains:

*   `www` subdomain as a legacy restriction
*   `api` subdomain reserved for final REST API
*   `tests` this subdomain (for my purpose only) provides easy URL to code coverage with
    unit tests

> I use `dev` domain only for on my local machine only. Feel free to change it
> on whatever name you like.

While building frontend application I have made some basic nginx configuration
and it looks like this snippet presented at the bottom.

> It might be important for Readers. We have decided to split application for two separate projects, due to AngularJS have problems with support of multiple subdomains. Finally one of our application serve subdomains `<variable>.example.dev` and other serve bacis domain `example.dev`.

This configuration provides 5 servers:

*   First one is for frontend application, which may support organizations with
    some exceptions for `api`, `tests` and `www` (ex.: `companyname.example.dev`).
*   Second for legacy domain `www` redirect.
*   The third is for frontend aplication which may support only basic domain (ex.: `example.dev`).
*   Next one is for REST backend domain redirect provided by apiary.
*   The Last one provides easy access for auto generated code coverage for
    fronted app.

```nginx
server {
  listen 80;
  server_name ~^(?:(?!www)(?!api)(?!tests))(.*)\.example\.dev$;
  access_log /tmp/subdomains.example.dev.log;
  error_log  /tmp/subdomains.example.dev.error.log;

  client_max_body_size 100M;

  location / {
    add_header 'Access-Control-Allow-Origin' '*';
    root '/ABSOLUTE_PATH_TO_WORKING_DIR/example-subdomain-frontend/build';
    try_files $uri $uri/ /index.html =404;
  }
}

server {
  listen 80;
  server_name www.example.dev;
  return 301 $scheme://exampe.dev$request_uri;
}

server {
  listen 80;
  server_name example.dev;
  access_log /tmp/example.dev.log;
  error_log  /tmp/example.dev.error.log;

  client_max_body_size 100M;

  location / {
    add_header 'Access-Control-Allow-Origin' '*';
    root '/ABSOLUTE_PATH_TO_WORKING_DIR/example-domain-frontend/build';
    try_files $uri $uri/ /index.html =404;
  }
}

server {
  listen 80;
  server_name api.example.dev;

  access_log /tmp/api.example.dev.log;
  error_log  /tmp/api.example.dev.error.log;

  location / {
    add_header 'Access-Control-Allow-Credentials' 'true';
    add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, OPTIONS';
    add_header 'Access-Control-Allow-Headers' 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type';

    proxy_pass http://private-ABCDE-example.apiary-mock.com;
  }
}


server {
  listen 80;
  server_name tests.example.dev;

  client_max_body_size 100M;

  root "/ABSOLUTE_PATH_TO_WORKING_DIR/example-subdomain-frontend/tests/test-coverage/PhantomJS 2.1.1 (Mac OS X 0.0.0)";
}
```

[angularjs-webpage]: https://angularjs.org/
[apiary-webpage]: https://apiary.io/
