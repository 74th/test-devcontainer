# mac上でdockerマウントでfioでパフォーマンスを測定する

## テスト内容

[test_fio.sh](./test_fio.sh)参照

- 10G、ブロックサイズ20Mのシーケンシャルリード
- 10G、ブロックサイズ20Mのシーケンシャルライト
- ブロックサイズ4Kの16スレッドランダムリード
- ブロックサイズ4Kの16スレッドランダムライト

## テスト対象

- dockerなしのmacOS
- Docker Desktopの標準（consistency=consistent）
- Docker Desktopのconsistency=delegatedオプション付き
- Docker Desktopのconsistency=cachedオプション付き
- Docker DesktopのSynclonized file shares
- Rancher Desktop
- Colima
- Podman
- Finch
- dockerなしのParallels DesktopのVM
- Parallels DesktopのVM上のDocker

## おおよその結果

Docker Desktopの標準と、
