# 주요 프로젝트
- [자동차 번호판 인식기 경량화](https://github.com/shininghyunho/cctv_obect_detection)
- [건강기능식품 성분 분석 어플레이케이션](https://github.com/wbjung2917/HEFFAN)
- [국민청원 사전 청원 웹페이지](https://github.com/withseungryu/tave_conference)
- [채팅 로그분석](https://github.com/shininghyunho/4_1_Cloud_Computing/tree/master/RealChat)
- [어플 이름 추천](https://github.com/shininghyunho/3_2_SA/blob/master/%EB%82%BC%EA%B1%B0/AppAnalysis.ipynb)
- [폭파물 탐지 시뮬레이터](https://github.com/shininghyunho/3_2_SE)

## 사용가능한 언어 (1~5)
- python(4)
- c(3)
- c++(3)
- java(3)
- R(3)
- c#(2)

# 프로젝트 설명
## 자동차 번호판 인식기 경량화
### 개요
<img  src = "https://user-images.githubusercontent.com/46080945/112717489-793a5400-8f30-11eb-831c-600df823a7fb.JPG"  width="900px" height="500px">

2020.09.01~2020.12.21 [키센스](https://www.qisens-ai.com)에서 인턴으로 근무하며 개발에 참여했습니다. 기존에 [SSD](https://arxiv.org/abs/1512.02325) 기반으로 개발된 자동차 번호판 인식기 [인공지능 모델](https://www.qisens-ai.com/products)을 경량화하여 DVR(Digital Video Recorder)에 올리는 프로젝트 입니다.
### 개발 언어
- C, Python
### 역할
[Hisilicon](https://www.hisilicon.com/en)의 SDK를 이용하여 모델을 경량화하고 인식 결과를 후처리하는 업무를 담당했습니다.
- [경량화 과정 코드](https://github.com/shininghyunho/cctv_obect_detection/tree/main/sample)
- [경량화 소프트웨어 코드](https://github.com/shininghyunho/cctv_obect_detection/blob/main/sample_nnie_software/sample_svp_nnie_software.c)
- [후처리 과정 코드](https://github.com/shininghyunho/cctv_obect_detection/tree/main/inference)

### 결과 이미지
![201214_095328559822](https://user-images.githubusercontent.com/46080945/102562795-2f64f500-411b-11eb-918a-5b3f0cc23f96.jpg)
![201214_095239168018](https://user-images.githubusercontent.com/46080945/102562804-325fe580-411b-11eb-86f2-b5eb1c60f6d9.jpg)
![201214_095216093329](https://user-images.githubusercontent.com/46080945/102562806-33911280-411b-11eb-9418-61cdb16e65dd.jpg)
![201214_095019560535](https://user-images.githubusercontent.com/46080945/102562856-50c5e100-411b-11eb-9f5e-e1cf324bd3ac.jpg)

![201214_095239176142](https://user-images.githubusercontent.com/46080945/102562402-5a027e00-411a-11eb-9d9e-d3977971b3df.jpg)
![201214_094921375309](https://user-images.githubusercontent.com/46080945/102562624-d2693f00-411a-11eb-9f9f-9e6137d77723.jpg)
![201214_094623539784](https://user-images.githubusercontent.com/46080945/102562635-d8f7b680-411a-11eb-9666-7dd21f950b13.jpg)
![201214_094544139387](https://user-images.githubusercontent.com/46080945/102562663-e7de6900-411a-11eb-8b6e-a15fbee30d78.jpg)
![201212_181944152943](https://user-images.githubusercontent.com/46080945/102562698-fe84c000-411a-11eb-900e-460bc54174e5.jpg)
![201212_182122068749](https://user-images.githubusercontent.com/46080945/102562744-15c3ad80-411b-11eb-9834-c54c935e4394.jpg)

### 참고자료
[개발 일지](https://blog.naver.com/chlgusgh3315/222091134949)
[개발 문서](https://drive.google.com/drive/folders/1zB0Tn92V9HhhjCXLgEmZqmFbMkq2Co38?usp=sharing)

## 건강기능식품 성분 분석 어플레이케이션

### 개요
건강기능식품의 영양 성분을 제대로 알고 섭취할 수 있도록 영양 성분을 촬영해 분석해주는 어플리케이션을 개발했습니다. 컴퓨터종합설계 과목을 통해 개발하였고 이를 통해 A+학점을 받았습니다.

![캡스톤결과이미지](https://user-images.githubusercontent.com/46080945/112717800-2eb9d700-8f32-11eb-986e-d299057a8669.JPG)
### 개발 언어
- JAVA, Android
### 역할
- 어플리케이션 개발(안드로이드)
- 이미지 결과 후처리 과정
- 결과 분석
[소스코드](https://github.com/wbjung2917/HEFFAN)

### 유즈케이스 다이어그램
![heffan_usecase](https://user-images.githubusercontent.com/46080945/112718007-9ae90a80-8f33-11eb-9d09-e8b25092b75b.JPG)

### 액티비티 다이어그램
![heffan_activity](https://user-images.githubusercontent.com/46080945/112718028-bfdd7d80-8f33-11eb-933a-30b9b8671fb0.JPG)

### 설명 영상

[<img  src = "https://user-images.githubusercontent.com/46080945/112718216-e3ed8e80-8f34-11eb-970e-914d12130310.jpg"  width="200px" height="100px">](https://youtu.be/gy-MVboaXpo)

## Spring Boot 기반 게시판(토이 프로젝트)
### 개요
spring boot를 활용한 게시판 기능을 구현했습니다.
게시판
### 기능
- 게시판 기능
- 첨부파일 첨부 기능
- 로그인 기능
### 구현
- 유저, 첨부파일, 게시글 crud
-  Jpa를 이용한 DB 접근
-  MyBatis를 이용한 DB 접근
-  개발, 배포용 로그 관리
-  권한별 개별 페이지 기능(using spring security & csrf token)
## 상세한 이미지
![signup](https://user-images.githubusercontent.com/46080945/113245627-4c03f200-92f2-11eb-83bf-8a23afbf2f1a.PNG)
![login](https://user-images.githubusercontent.com/46080945/113245646-558d5a00-92f2-11eb-8548-d9446e2b3db2.PNG)
![onlyuser](https://user-images.githubusercontent.com/46080945/113245652-57571d80-92f2-11eb-9166-30fb8d00e96e.PNG)
![onlyadmin](https://user-images.githubusercontent.com/46080945/113245725-7a81cd00-92f2-11eb-9575-1e0d6ed2e573.PNG)
![board](https://user-images.githubusercontent.com/46080945/113245727-7c4b9080-92f2-11eb-86c2-c35e101b0171.PNG)
![write](https://user-images.githubusercontent.com/46080945/113245734-81104480-92f2-11eb-93e9-f8f147ad453a.PNG)
![detail](https://user-images.githubusercontent.com/46080945/113245739-82417180-92f2-11eb-9fec-6bdc446896dd.PNG)

