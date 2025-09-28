DevContainer Featureのdocker-in-dockerを使ったコンテナがdocker-composeで起動したコンテナにアクセス可能かどうか。

まず、ローカルからアクセスできるか。

```
$ redis-cli -h redis info
```

アクセス可能。

次にコンテナ内からアクセスできるか。

```
$ docker run -it --rm debian

$ apt update && apt install -y redis-tools
$ redis-cli -h redis info
```

ダメだったが、コンテナ内はホスト名 redis を知らない。
それを教えてあげれば良い。

```
$ getent hosts redis
172.21.0.2    redis

$ docker run -it --rm --add-host redis:`getent hosts redis | awk '{print $1}'` debian

$ apt update && apt install -y redis-tools
$ redis-cli -h redis info
```

アクセス可能だった。

docker-in-dockerなのでホストに漏れたりしてなくて良い！