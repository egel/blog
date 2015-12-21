Title:      Discover the docker containers
Date:       2015-08-05 09:31
Status:     Published
Category:   Discovery
Tags:       linux, docker
Authors:    Maciej Sypień
Summary:    <div class="intro-article-image-sm" markdown="1">![Docker logo]({filename}/images/docker_large_logo_transparent.png)</div> We will invetigate docker containers.


<div class="intro-article-image-sm" markdown="1">
  ![Docker logo]({filename}/images/docker_large_logo_transparent.png)
</div>

## how to start?
install it from site


### List docker images

    docker images

### Run image in teminal and interactive

    docker run -it 

### Save container into images

You do this by `commit` I mean 

    docker commit <container-ID> <yourname>/<morespec>:1.0


### Use Dockerfile

    vim Dockerfile

then

    
