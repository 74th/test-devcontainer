DevContainer Featureのdocker-in-dockerを使うと、コンテナ内でdockerコマンドを実行できる。
macのDocker Desktopを使っている場合でも、ホストのDockerデーモンと切り離されているため、影響はない。

以下のコマンドで実行できた。

```
docker --rm -it -p 80:80 nginx
```

```
curl http://localhost
```