# Lee Sang Hyeok · 이상혁

Backend · Infra Developer

## About Me

> Java·Spring Boot로 백엔드를 만들고, Docker·AWS·Redis·Kafka로 배포와 운영까지 직접 합니다.<br />
> 동작하는 데모에서 멈추지 않고, 측정해서 병목을 찾고 운영 가능한 서비스로 다듬는 데 관심이 많습니다.

contact &nbsp;&middot;&nbsp; [kljl6773@gmail.com](mailto:kljl6773@gmail.com)

## 지금 만드는 것

고가용성 가상 암호화폐 거래소를 1년 주기로 만들고 있습니다. 매칭 엔진·원장·저널을 직접 구현하고, 장애 주입 실험으로 가용성을 실측하는 것이 목표입니다. 현재 카오스 실험 5종(노드 사망, 네트워크 분할, 프로세스 정지 등)이 라이브에서 통과한 상태입니다. 공개는 완성 후 예정입니다.

## 주요 프로젝트

| 프로젝트 | 무엇을 했나 | 확인 가능한 결과 |
| :-- | :-- | :-- |
| [sangkwon-platform-poly](https://github.com/sangkwon-poly/sangkwon-platform-poly) | 소상공인 상권분석 플랫폼. DB 설계·상권분석 API·관리자 백오피스·EC2 2대 ALB 배포 담당 | 커밋 206건, PR 154건, 테스트 75파일 335건, EC2 2대 + ALB 무중단 배포 |
| [appintoss-meetup](https://github.com/Appintos-Harmony/appintoss-meetup) | 토스 미니앱 합주 서비스. 백엔드 전량과 공유·커뮤니티 클라이언트 담당 | 앱인토스 실제 출시, 커밋 240건, 의존성 0인 API 서버 450줄 중 378줄 작성 |
| [SafetyNevi](https://github.com/SanghyeokLee-KR/SafetyNevi) | 재난문자를 지도 위 위험구역으로 바꾸고 대피 경로를 안내. 팀 졸업작품을 인계받아 단독으로 운영 수준까지 보강 | 인계 후 단독 커밋 153건, 106일 지속 개발, 테스트 55건 |
| [keep-nginx-alive](https://github.com/SanghyeokLee-KR/keep-nginx-alive) | root 공격자를 차단할 수 없는 CTF에서 nginx 가용성을 지킨 방어 기록 | 채점 다운 0회, bash 16개 914줄, systemd 유닛 12개, flock 기반 복구 직렬화 |
| [high-throughput-image-pipeline](https://github.com/SanghyeokLee-KR/high-throughput-image-pipeline) | t3.micro 한 대에서 asyncio·Redis로 이미지 수집. 병목이 CPU임을 실측으로 규명 | 284 p/s, 평균 지연 85ms, CPU 100%·RAM 47% 실측 비교 |
| [DeliveryPro](https://github.com/SanghyeokLee-KR/DeliveryPro) | 주문·매장·라이더를 잇는 배달 플랫폼. 묶음배달 경로 탐색을 라이브러리 없이 직접 구현 | 다익스트라·Held-Karp 직접 구현, 노드 525·간선 1,742, 테스트 41건, DB 설치 없이 한 줄 실행 |
| [ai-lunch-curator](https://github.com/SanghyeokLee-KR/ai-lunch-curator) | 식단 수집부터 AI 분석·Teams 발송·EC2 배포까지 잇는 자동화 파이프라인 | pytest 23건이 배포 선행 게이트, Docker Compose · Nginx · GitHub Actions |

## 그 외 저장소

| 저장소 | 내용 |
| :-- | :-- |
| [polytalk](https://github.com/SanghyeokLee-KR/polytalk) | 서버가 평문을 보지 않는 1:1 E2EE 소켓 채팅. ECDH 키 교환과 AES-GCM을 직접 조립, 테스트 14건 |
| [incident-response-cryptominer](https://github.com/SanghyeokLee-KR/incident-response-cryptominer) | 실제로 겪은 GPU 크립토재킹 감염을 탐지·제거·검증하고 Sysmon 탐지룰까지 정리한 기록 |
| [kopo-ecommerce-evolution](https://github.com/SanghyeokLee-KR/kopo-ecommerce-evolution) | 같은 쇼핑몰을 JSON, JDBC, Spring Boot 세 단계로 다시 설계한 기록 |
| [DevHub](https://github.com/SanghyeokLee-KR/DevHub) | 코드·UI 공유 커뮤니티. 커스텀 세션 로그인을 그대로 두고 브릿지 필터로 인가만 얹어 민감 경로 28개를 막았습니다. 테스트 17건 |
| [BookRidge](https://github.com/SanghyeokLee-KR/BookRidge) | Java를 배우고 처음 만든 콘솔 도서 관리 시스템 |
| [linux-practice](https://github.com/SanghyeokLee-KR/linux-practice) | Linux 서버 구축 실습 기록 |

## 기술 스택

<b>배포·운영까지 해본 것</b>

<img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white" alt="Java" height="26" /><img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white" alt="Spring Boot" height="26" /><img src="https://img.shields.io/badge/Spring_Security-6DB33F?style=flat-square&logo=springsecurity&logoColor=white" alt="Spring Security" height="26" /><img src="https://img.shields.io/badge/JPA-59666C?style=flat-square&logo=hibernate&logoColor=white" alt="JPA" height="26" /><br />
<img src="https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=oracle&logoColor=white" alt="Oracle" height="26" /><img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" height="26" /><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" height="26" /><img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS" height="26" /><br />
<img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white" alt="Nginx" height="26" /><img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" height="26" /><img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" height="26" />

<b>써본 것</b>

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" height="26" /><img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" height="26" /><img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" height="26" /><img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white" alt="Apache Kafka" height="26" /><br />
<img src="https://img.shields.io/badge/Thymeleaf-005F0F?style=flat-square&logo=thymeleaf&logoColor=white" alt="Thymeleaf" height="26" /><img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible" height="26" /><img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" height="26" /><img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" height="26" />
