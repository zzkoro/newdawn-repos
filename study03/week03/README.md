## 프로젝트 설정

### 1) 구성

.
├── .env.sample : 환경변수 설정 파일 sample
├── .gitignore : gitignore 파일
├── .python-version : python 버전 파일
├── 01_rag_with_lcel.ipynb : LCEL을 사용한 RAG 실행 파일
├── 02_rag_with_langgraph.ipynb : LangGraph를 사용한 RAG 실행 파일
├── data : 데이터 폴더
├── pyproject.toml : uv 설정 파일
├── README.md : 프로젝트 설명
└── uv.lock : uv 설정 파일

### 2) 라이브러리 동기화

```
uv sync
```
