## 프로젝트 설정

### 1) 구성

.
├── .env.sample : 환경변수 설정 파일 sample
├── .gitignore : gitignore 파일
├── .python-version : python 버전 파일
├── 01_langchain_model.ipynb : langchain을 이용한 LLM 모델 연동
├── 02_langchain_tools.ipynb : langchain을 이용한 Function Call 연동
├── main.py : 사용하지 않음
├── pyproject.toml : uv 설정 파일
├── README.md : 프로젝트 설명
└── uv.lock : uv 설정 파일

### 2) 라이브러리 동기화

```
uv sync
```

### 3) 환경변수 설정

- .env.sample 파일을 참고하여 .env 파일 생성
- OPENAI_API_KEY, ANTHROPIC_API_KEY 설정
  ❗`.env 파일은 github에 올라가지 않도록 주의해 주세요.`

### 4) chatapi_sample.ipynb 파일

- OpenAI 모델 연결하기
- Anthropic 모델 연결하기
- Ollama 모델 연결하기
