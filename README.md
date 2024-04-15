<div align="center">
<h1>😉CBOM</h1>
  
![대시보드1](https://github.com/Dxhyeon/cbom-project/assets/118159407/803a765e-ea6e-4f66-94cb-f4f89b3826eb)
SBOM을 이용한 취약점 식별 자동화 시스템 <br> Automation System for Vulnerability Identification Using SBOM
</div>
<br>

## 프로젝트 소개

 - CBOM은 SBOM을 이용하여 소프트웨어의 취약점을 식별하고 투명성을 검증할 수 있는 솔루션입니다.
 - 취약점 식별 외에도 소프트웨어에 사용된 오픈소스와 라이선스를 확인할 수 있습니다.
 - 대시보드를 통해 취약점 식별 결과를 한눈에 확인할 수 있습니다.
 - 취약점 식별 결과와 SBOM 정보를 Report로 저장할 수 있습니다.
 
<br>

## 팀원 구성

<div align="center">

| **강민식** | **김도현** | **최수호** | **최영훈** |
| :------: |  :------: | :------: | :------: |
| [<img src="https://avatars.githubusercontent.com/u/127810857?v=4" height=150 width=150> <br/> @MynameisMansik](https://github.com/MynameisMansik) | [<img src="https://avatars.githubusercontent.com/u/118159407?v=4" height=150 width=150> <br/> @Dxhyeon](https://github.com/Dxhyeon) | [<img src="https://avatars.githubusercontent.com/u/71062855?v=4" height=150 width=150> <br/> @S4nso](https://github.com/S4nso) | <img src="https://github.com/Dxhyeon/cbom-project/assets/118159407/939243a3-2385-4412-8b76-614a80972694" height=150 width=150> <br/> 최영훈 |

</div>

<br>

## 1. 개발 환경
- Front : Django, Bootstrap, Chart.js
- Back-end : Python, Django
- Database : MariaDB
- 협업 툴 : Notion, Discord, Github
<br>

## 2. 개발 기간 및 작업 관리

### 개발 기간

- 전체 개발 기간 : 2023-09-05 ~ 2023-11-21
- DB 설계 & 구축 : 2023-09-21 ~ 2023-10-14
- Web 설계 & 구축 : 2023-09-28 ~ 2023-10-16
- 취약점 식별 기능 구현 : 2023-09-05 ~ 2023-11-21

### 작업 관리

 - Notion과 Discord를 사용하여 진행 상황을 공유하였습니다.
 - 매 주 대면 회의를 진행하며 작업 순서에 대하여 논의하고, Trouble Shooting을 진행하였습니다.

<br>

## 3. 프로젝트 구성도

![image](https://github.com/Dxhyeon/cbom-project/assets/118159407/04d74e46-712d-4a58-922f-f3c38c5ec333)

|단계|내용|
|-----|---|
|1. SBOM 업로드|사용자는 웹 플랫폼에 SBOM을 업로드|
|2. SBOM 구성 요소 추출 및 출력|각 구성 요소의 패키지와 버전등 사용된 정보를 추출하여 재가공 및 웹 플랫폼 출력|
|3. 취약점 식별 및 분석|CVE와 CWE 데이터를 활용하여 오픈 소스 패키지의 취약점을 식별하고 해당 취약점 내용 추출하여 저장|
|4. 시각적 결과 제공|취약점 분석 결과는 웹 플랫폼을 통해 사용자에게 시각적으로 제공|

<br>

## 4. 페이지별 기능
