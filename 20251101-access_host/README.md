# ホストへのアクセス

## macOS

host.docker.internal でアクセスできる。
ただし、デフォルトネットワークルートではホストにアクセスできない。

確認したソフトウェア

- Docker Desktop for mac
- Colima(macOS)
- Podman(macOS)
- Finch(macOS)
- Rancher Desktop(macOS)

## Linux

host.docker.internal ではアクセスできない。
以下でデフォルトルートのIPアドレスを取得してアクセスできる。

```
export HOST_IP=$(ip route | awk '/default/ {print $3}')
```
