# pj_Umbrella_cop
project <br/>

### team : 엄브렐라(주)
### member: <a href="https://github.com/getto-dotted">강덕희(웹서버)</a> , 신재훈(ml, 크롤링)           

### 개발 언어 및 환경
python(3.7.4),
pycharm CE(2019.3.3),
VScode 1.43.0,
goormIDE

## 출근전 우산을 챙겨야하나 고민될때 

# 오늘 내일 비가 올지를 예측해서 우산을 챙겨야 하는지를 알려줌
사용자로부터 주소지의 지역 (시,군)값을 받아와서(Web) 해당지역의 현재,금일,내일까지의 날씨정보를 크롤링 후 
과거 자료를 토대로 학습된 알고리즘이 우산이 필요한지 아닌지를 알려주는 형태이다.


### 선택한 알고리즘 DecisionTreeClassifier
선택이유 : 어떤 항목에 대한 관측값과 목표값을 연결시켜주는 예측 모델이라 해서 제일 적합하다고 판단 </br>
          다른 알고리즘들에 비해 높은 정확도를 가지고있음  </br>
지역별 데이터량(지역별 데이터량이 다르지만 평균 8~9천개의 데이터들로 학습됨) </br>

학습시 사용한 데이터 :  x = 운량(구름의양 0:맑음 1:흐림으로 처리), 습도, 강수량  y = 강수시간
결과값
0 = 우산 불필요 , 1 = 우산 필요

우리나라의 기후 특성상 비가 오는날보다 맑은날이 더 많기때문에 자연히 맑은날의 데이터가 많은데
과적합 유무를 판단할 수 있는 분별력이 필요함
통계상 1/3~1/4 정도 

<img width="" height="" src='https://github.com/ttlevt/pj_Umbrella_cop/blob/master/readme/rst_kw.png'></img>


#### 학습 및 크롤링 데이터 출처
#### 1. 공공데이터 지역별 일간예보(1904~2018)
<a href="https://data.kma.go.kr/data/rmt/rmtList.do?code=400&pgmNo=570">공공데이터 바로가기</a>  
#### 2. sk telecom API 현재날씨현황
<a href="https://developers.sktelecom.com/">sktelecom api 바로가기</a>  
#### 3. weatheri 지역별 날씨현황
<a href="https://www.weatheri.co.kr/index.php">sktelecom api 바로가기</a>  




## 파일 설명
DIR apis : 크롤링 및 선택적 피클에 필요한 격자값, 지역값 들이 있는 폴더 </br>
DIR train : 알고리즘학습에 필요한 지역별 자료들이 있는 폴더 </br>
run_.py : 교차검증하여 결과출력 </br>
now_sk : 금일 skAPI를 통한 현재 기상상태 출력 </br>
apisdata_craw,  tom : 공공데이터 크롤링 및 학습된 알고리즘 호출하여 결과 출력(today,tomorrow) </br>
weatheri_today, tom : weatheri웹 데이터 크롤링 및 학습된 알고리즘 호출하여 결과 출력 (today,tom) </br>

## 실행단계별 설명
<img width="" height="" src='https://github.com/ttlevt/pj_Umbrella_cop/blob/master/readme/1.png'></img>
1. 이종연결된 web서버로부터 지역명을 요청값으로 받아와서 교차검증을하는 함수를 실행시킨다
<img width="" height="" src='https://github.com/ttlevt/pj_Umbrella_cop/blob/master/readme/2.png'></img>
2. 각각의 지정된 변수들은 요청값들로 호출되어 알고리즘으로부터 결과값을 받게되고 해당값들을 비교하여 최종적으로 결과를 출력시켜줌
<img width="" height="" src='https://github.com/ttlevt/pj_Umbrella_cop/blob/master/readme/3.png'></img>
3. 동명의 도시로 인한 광역시 별도처리 후 csv파일에서 도시명과 크롤링할때 필요한 자료(도시의 격자값 or 위도,경도 등)를 사전형태로 결합
  후 요청값이 사전의 key값 안에 해당되면 value값으로 반환해줌
<img width="" height="" src='https://github.com/ttlevt/pj_Umbrella_cop/blob/master/readme/4.png'></img>
4. 반환받은값들로 크롤링실행 후 받아온 자료를 알고리즘을 통해서 학습시킨 후 결과값을 반환하게 한다.


## ML부분
<img width="" height="" src='https://github.com/ttlevt/pj_Umbrella_cop/blob/master/readme/ml1.png'></img>
1. 알고리즘의 학습에 필요한 엑셀들을 병합후 컬럼들을 뽑아와서 결측치 처리 후 필요한 컬럼 및 자료들로만 이루어진 데이터파일로 재저장
<img width="" height="" src='https://github.com/ttlevt/pj_Umbrella_cop/blob/master/readme/ml2.png'></img>
2,3 데이터파일 x,y divide, 선택한 알고리즘으로 학습 후 피클로 저장한다.
          지역마다 다른 피클명으로 저장한다(ex) kk=경기, cc=충청등)
<img width="" height="" src='https://github.com/ttlevt/pj_Umbrella_cop/blob/master/readme/ml4.png'></img>
4. 함수에서 지역명을 요청값으로 받게되면 조건문을통해 해당지역의 데이터로 학습된 모듈이 실행되도록 지정(20.03.18 미완)


