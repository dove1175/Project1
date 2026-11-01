# Project1

AWS 인프라를 직접 구축하며 네트워크, 서버, 보안 설정을 실습하고
아키텍처 의사결정과 트러블슈팅 과정을 기록하는 프로젝트입니다.

## Goal

- AWS EC2 기반 서버 구축
- Security Group을 통한 접근 제어
- Nginx 웹 서버 구성
- CloudWatch 기본 모니터링
- 아키텍처 설계 및 개선 과정 기록

## Environment

- AWS Region: ap-northeast-2 (Seoul)
- VPC: Default VPC
- EC2 Instance Name: project1

## Implementation

현재까지 다음 구성을 완료했습니다.

- Default VPC 사용
- Public Subnet에 EC2 `project1` 배포
- Security Group 구성
  - SSH 22: 제한된 소스만 허용
  - HTTP 80: 웹 접속 허용
- Amazon Linux 2023 사용
- Nginx 설치 및 실행
- EC2 Public IP를 통한 웹 페이지 접속 확인

현재 구성:

```text
Internet
   ↓
Security Group
   ↓
EC2 project1
   ↓
Nginx :80
   ↓
Gunicorn :8000
   ↓
Flask Application
```

- Nginx가 외부 HTTP 요청을 수신
- Gunicorn은 `127.0.0.1:8000`에서 내부적으로 실행
- Flask가 실제 애플리케이션 요청을 처리
- Gunicorn은 systemd 서비스로 등록하여 EC2 재부팅 후 자동 실행
- Gunicorn 프로세스 종료 시 `Restart=always` 설정으로 자동 복구
- `curl`을 이용해 Gunicorn 직접 요청과 Nginx Reverse Proxy 요청을 각각 확인

## Monitoring

EC2에서 기본 제공되는 CloudWatch Metrics를 이용해 인스턴스 상태와 기본 트래픽을 확인했습니다.

- CPUUtilization
- NetworkIn
- NetworkOut
- StatusCheckFailed

![CloudWatch Basic Metrics](docs/screenshots/cloudwatch-basic-metrics.png)

현재 프로젝트 규모에서는 별도의 모니터링 스택을 추가하지 않고 CloudWatch 기본 지표로 상태를 확인하도록 구성했습니다.
