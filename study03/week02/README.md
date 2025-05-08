## 프로젝트 설정

### 1) 구성

.
├── .env.sample : 환경변수 설정 파일 sample
├── .gitignore : gitignore 파일
├── .python-version : python 버전 파일
├── 01_mcp_server_local.py : MCP 서버 stdio 모드 실행 파일
├── 02_mcp_server_remote.py : MCP 서버 sse 모드 실행 파일
├── 03_mcp_server_client.ipynb : MCP 서버 클라이언트 실행 파일
├── claude_desktop_config.json.sample : Claude Desktop 설정 파일 sample
├── main.py : 사용하지 않음
├── pyproject.toml : uv 설정 파일
├── README.md : 프로젝트 설명
└── uv.lock : uv 설정 파일

### 2) 라이브러리 동기화

```
uv sync
```

### 3) MCP 서버 (stdio) 설치 및 실행

#### 3-1) Development Mode로 실행하기 (MCP Inspector)

```
mcp dev 01_mcp_server_local.py
```

#### 3-2) Claude Desktop Integration

```
mcp install 01_mcp_server_local.py
```

- Claude Desktop 종료 후 재실행
- 검색 및 도구 메뉴에 새로운 도구가 추가되었는지 확인
- Claude Desktop 설정 파일 확인 (Claude Desktop -> 설정 -> 개발자)

#### 3-4) Claude Desktop에서 확인하기

```
오늘 서울 날씨를 알려줘
```

- Claude Desktop에서 검색 및 도구 메뉴에서 웹검색을 disable 하고 질의 수행

### 4) MCP 서버 (sse) 설치 및 실행

#### 4-1) MCP 서버 실행하기

```
uv run 02_mcp_server_remote.py
```

#### 4-2) Claude Desktop Integration

- Claude Desktop 설정 파일에 아래 정보 추가 (Claude Desktop -> 설정 -> 개발자)

```
"TimeService": {
      "command": "npx",
      "args": [
        "-y",
        "supergateway",
        "--sse",
        "http://localhost:8005/sse"
      ]
    }
```

- Claude Desktop 종료 후 재실행
- 검색 및 도구 메뉴에 새로운 도구가 추가되었는지 확인

#### 4-3) Claude Desktop에서 확인하기

```
현재 서울 시간을 알려줘
```

- Claude Desktop에서 검색 및 도구 메뉴에서 웹검색을 disable 하고 질의 수행
-

### 5) MCP 클라이언트 실행

```
03_mcp_server_client.ipynb 내 코드 실행
```
