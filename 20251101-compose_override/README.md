Docker Composeにある、自動で compose.override.yml を読み込む機能は DevContainer ではサポートされない。
明示的に、devcontainer.json の dockerComposeFile に両方のComposeファイルを指定する必要がある。
