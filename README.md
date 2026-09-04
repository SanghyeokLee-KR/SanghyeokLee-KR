# Lee Sang Hyeok · 이상혁

Backend · Infra Developer

## About Me

열심히 하겠습니다.

contact  ·  [kljl6773@gmail.com](mailto:kljl6773@gmail.com)

## 주요 프로젝트

| 프로젝트                                                                                                | 설명                                                                                                | 결과                                                                   |
| :-------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------- |
| [sangkwon-platform-poly](https://github.com/sangkwon-poly/sangkwon-platform-poly)                   | 소상공인 상권분석 플랫폼. DB 설계, 상권분석 API, 관리자 백오피스와 배포를 담당했습니다.                                             | 커밋 206건, PR 154건, 테스트 75파일 335건, EC2 2대 + ALB 구성                     |
| [appintoss-meetup](https://github.com/Appintos-Harmony/appintoss-meetup)                            | 토스 미니앱 기반 합주 서비스. 백엔드 전체와 공유·커뮤니티 쪽 클라이언트를 맡았습니다.                                                 | 앱인토스 실제 출시, 커밋 240건, API 서버 450줄 중 378줄 작성                           |
| [SafetyNevi](https://github.com/SanghyeokLee-KR/SafetyNevi)                                         | 재난문자를 지도 위 위험구역으로 표시하고 대피 경로를 안내하는 서비스입니다. 졸업작품을 인계받은 뒤 혼자 유지보수와 개선을 이어갔습니다.                      | 인계 후 커밋 153건, 106일간 개발, 테스트 55건                                      |
| [keep-nginx-alive](https://github.com/SanghyeokLee-KR/keep-nginx-alive)                             | root 권한 공격자를 차단할 수 없는 CTF 환경에서 nginx를 최대한 오래 살려 두기 위해 만든 방어 스크립트와 운영 기록입니다.                       | 채점 다운 0회, bash 16개 914줄, systemd 유닛 12개, flock 기반 복구 직렬화             |
| [high-throughput-image-pipeline](https://github.com/SanghyeokLee-KR/high-throughput-image-pipeline) | t3.micro 한 대에서 asyncio와 Redis를 이용해 이미지 수집 파이프라인을 구성했습니다. 부하 테스트를 통해 병목이 메모리가 아니라 CPU라는 점을 확인했습니다. | 284 p/s, 평균 지연 85ms, CPU 100%, RAM 47%                               |
| [DeliveryPro](https://github.com/SanghyeokLee-KR/DeliveryPro)                                       | 주문, 매장, 라이더를 연결하는 배달 플랫폼입니다. 묶음배달 경로 탐색 로직도 구현했습니다.                                               | 다익스트라·Held-Karp 구현, 노드 525·간선 1,742, 테스트 41건, DB 설치 없이 실행 가능         |
| [ai-lunch-curator](https://github.com/SanghyeokLee-KR/ai-lunch-curator)                             | 식단 수집부터 AI 분석, Teams 발송, EC2 배포까지 자동화한 파이프라인입니다.                                                  | pytest 23건을 배포 전 게이트로 사용, Docker Compose · Nginx · GitHub Actions 구성 |

## 그 외 저장소

| 저장소                                                                                               | 내용                                                                                                |
| :------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------ |
| [polytalk](https://github.com/SanghyeokLee-KR/polytalk)                                           | 서버가 평문 메시지를 볼 수 없는 1:1 E2EE 소켓 채팅입니다. ECDH와 AES-GCM을 사용했고 테스트 14건을 작성했습니다.                        |
| [incident-response-cryptominer](https://github.com/SanghyeokLee-KR/incident-response-cryptominer) | 실제 GPU 크립토재킹 감염을 겪은 뒤 탐지, 제거, 검증 과정과 Sysmon 탐지 규칙을 정리했습니다.                                        |
| [kopo-ecommerce-evolution](https://github.com/SanghyeokLee-KR/kopo-ecommerce-evolution)           | 같은 쇼핑몰을 JSON, JDBC, Spring Boot 세 단계로 다시 만들면서 구조가 어떻게 달라지는지 정리한 프로젝트입니다.                          |
| [DevHub](https://github.com/SanghyeokLee-KR/DevHub)                                               | 코드와 UI를 공유하는 커뮤니티입니다. 기존 커스텀 세션 로그인은 유지하고, 브릿지 필터를 추가해 민감 경로 28개에 인가 처리를 적용했습니다. 테스트 17건을 작성했습니다. |
| [BookRidge](https://github.com/SanghyeokLee-KR/BookRidge)                                         | Java를 배우면서 처음 만든 콘솔 기반 도서 관리 프로그램입니다.                                                             |
| [linux-practice](https://github.com/SanghyeokLee-KR/linux-practice)                               | Linux 서버 구축과 운영을 연습하면서 남긴 기록입니다.                                                                  |

## 기술 스택

<b>프로젝트에서 배포·운영까지 사용한 기술</b>

<img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white" alt="Java" height="26" /><img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white" alt="Spring Boot" height="26" /><img src="https://img.shields.io/badge/Spring_Security-6DB33F?style=flat-square&logo=springsecurity&logoColor=white" alt="Spring Security" height="26" /><img src="https://img.shields.io/badge/JPA-59666C?style=flat-square&logo=hibernate&logoColor=white" alt="JPA" height="26" /><br /> <img src="https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=oracle&logoColor=white" alt="Oracle" height="26" /><img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" height="26" /><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" height="26" /><img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS" height="26" /><br /> <img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white" alt="Nginx" height="26" /><img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" height="26" /><img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" height="26" />

<b>사용 경험이 있는 기술</b>

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" height="26" /><img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" height="26" /><img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" height="26" /><img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white" alt="Apache Kafka" height="26" /><br /> <img src="https://img.shields.io/badge/Thymeleaf-005F0F?style=flat-square&logo=thymeleaf&logoColor=white" alt="Thymeleaf" height="26" /><img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible" height="26" /><img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" height="26" /><img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" height="26" />
