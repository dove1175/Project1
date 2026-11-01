# Troubleshooting

## 01. EC2 SSH 접속 방식 확인

EC2 Instance Connect를 사용할 때는 AWS의 EC2 Instance Connect 서비스에서 SSH 요청이 들어오기 때문에, Security Group에 서울 리전 EC2 Instance Connect Prefix List를 허용해야 했습니다.

이후 로컬 Windows PowerShell에서 키 페어를 이용한 직접 SSH 접속도 확인했습니다.

### 배운 점

- EC2 Instance Connect와 로컬 SSH는 모두 SSH(22)를 사용하지만 접속 출발지가 다릅니다.
- 로컬 SSH는 키 페어와 `ec2-user` 계정을 사용합니다.
- Private Key 파일 권한이 너무 넓으면 SSH 클라이언트가 키 사용을 거부할 수 있습니다.

---

## 02. Nginx 요청 로그 확인

브라우저에서 웹 페이지를 새로고침한 뒤 다음 명령어를 사용해 요청이 실제로 Nginx까지 전달되는 것을 확인했습니다.

```bash
sudo tail -f /var/log/nginx/access.log
```

정상 요청에서는 HTTP 상태 코드 `200`이 기록되었습니다.

---

## 03. Nginx 404 오류 로그 확인

존재하지 않는 경로를 요청해 의도적으로 404 오류를 발생시켰습니다.

```text
/notfound.html
```

다음 명령어로 오류 로그를 실시간 확인했습니다.

```bash
sudo tail -f /var/log/nginx/error.log
```

Nginx가 요청받은 파일을 찾을 수 없어 `404 Not Found`를 반환하는 과정을 로그를 통해 확인했습니다.

### 배운 점

- `access.log`는 어떤 요청이 들어왔고 어떤 HTTP 상태 코드로 응답했는지 확인할 수 있습니다.
- `error.log`는 요청 처리 중 발생한 문제의 원인을 확인할 때 사용합니다.
- 웹 서버 장애 발생 시 브라우저 화면만 보는 것이 아니라 서버 로그를 먼저 확인하는 것이 중요합니다.
