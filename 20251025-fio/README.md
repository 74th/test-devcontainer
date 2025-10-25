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

### 4k 16スレッド ランダムリード(IOPS)

- `56k`: macOS
- `36k`: Parallels Desktop VM
- `33k`: Docker on Parallels Desktop VM
- `9.9k`: Rancher Desktop
- `9.3k`: Docker Desktop (consistency=delegated)
- `9.0k`: Finch
- `8.9k`: Docker Desktop (consistency=cached)
- `8.9k`: Docker Desktop (consistency=consistent)
- `8.8k`: Colima
- `7.6k`: Docker Desktop (Synclonized file shares)

Docker Desktop (Synclonized file shares)が性能でないのが納得感がない。
ファイル数が多い場合に効果があるという感じなのかもしれない。
