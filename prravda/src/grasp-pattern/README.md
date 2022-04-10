# Implementing movie reservation application with GRASP pattern

# Domain modeling as a draft for structuring
- 우리가 해결해야 할 문제를 영역으로 나누었을 때 어떻게 나누어지는지를 먼저 생각해본다. 
- 이 domain modeling 이라는 행위는 반드시 정확할 필요는 없다, 요구사항을 잘 반영할 수 있는 설계를 만들어낼 수 있는 model 이 좋은 model 이라는 마음가짐으로 접근 해야한다. 

# Thinking about the message at first
- domain model 의 각각의 domain 에서 협력이 일어날 때, 어떤 메시지가 오가는지를 먼저 생각한다. 
## reserve a movie
- '예매한다' 라는 메시지가 일단은 먼저 생각이 난다.
  - 주의해야 할 점은, 이 메시지에 대해서 생각할 때 메시지의 '송신자' 의 관점에서 생각해야 한다는 점이다.
- 이 메시지를 받는 domain object 는 그 message 의 요구사항을 처리하기 위한 정보를 아는 '정보 전문가(information expert)' 여야 한다.
- 이 책에서 상영을 담당하는 domain object (`screening.ts`) 가 영화에 대한 정보도 알고, 상영 시간도 알고, 상영 순번도 알고 있으니 해당 message 를 처리하는 domain object 로서 적절하지 않을까?
- 영화의 예매를 위해서는 필요한 정보들이 꽤 많다. 인원수도 알아야 하고, 영화의 가격도 알아야 하고, 영화의 상영 시간도 알아야 한다. 
- screening 이라는 domain object 가 이런 일을 혼자서 전부 할 수 있을까? 부담스러울 것이다. 여기서 screening 이 아닌, 다른 객체에게 도움을 요청할 부분을 생각해보자.
  - 영화의 가격은 screening 에서 알 수 없다. `movie.ts` 라는 영화에 관련된 domain object 가 아무래도 본인 스스로의 영화 가격을 더 잘 알고 있을 것이다.
  - 그래서 `movie.ts` 에서 `getFee()` 라는 method 를 만들어, 영화의 값을 반환하게 해 주는 식으로 movie domain object 가 screening domain object 를 도울 수 있게 처리하였다.
- 그러나, movie domain object 도 어떤 영화의 할인 정보에 대해서는 알지 못한다.
  - 왜냐면, movie domain object 는 movie 와 관련된 정보에 대해서만 전문가이지, 할인조건에 대해서는 전문가가 아니기 때문이다. 
  - 그래서, 위와 비슷한 이유로 할인 조건(discount condition)에 대해서 메시지를 보내야 할 필요성을 실감하게 되었다.
  - '할인 조건에 대한 정보를 알려주세요' 라고 이야기를 했을 때(send a message) 그에 대해서 응답해 줄 전문가도 생각해보자 
    - 아마 `discount-condition.ts` 정도면 적절하지 않을까?
  - 그리고 할인 정책과 관련해서 좀 더 알아야 할 필요가 있을까? 일단은 없어보인다. 여기서 1차 설계를 마무리해보자.

## Cohesion, Coupling
- "응집도(cohesion) 는 높이고, 의존성(coupling)은 낮춰라" 라는 말이 미덕처럼 여겨진다.
  - 다시 개념을 정리하자면...
    - 응집도: 어떤 것과 관련된 요소들이 한 곳에 밀도있게 모여있는 정도
    - 의존성: 어떤 것이 수행/작동되기 위해, 다른 것에 의존하는 정도 
- 우리는 `information expert` pattern 으로 screening -> movie -> discount-condition 으로 책임을 위임/분할하고 각자를 협력시켰다.
- 그러나, 굳이 번거롭게 이렇게 한 이유가 있을까? 결국 screening 이 aggregation part 로서 일을 해 주어서, movie 에 대한 정보도 알고 discount-condition 에 대한 정보도 알게 된다면, 신경쓸 요소가 줄어들텐데 말이다. 
- 그렇다, 이유가 존재한다. 바로 coupling 은 느슨하게, cohesion 은 강력하게 만들기 위해서이다. 
  - 위에 이 번거로운 설계에 대한 대안으로서 주장한 설계는 screening 이라는 것이 작동하기 위해서 movie 와 discount-condition 에 모두 의존해야만 하는 상황을 만든다.
    - 이는 위에 정의한 의존성(coupling)이 증가하는 행위이며, 의존성이 증가한다는 것은 그만큼 변화에 취약해진다는 의미가 된다
      - 물론 이는 trade-off 적인 성격이 있어 관리해야 할 부분이 줄어든다는 장점 또한 있긴 하지만...
    - 그래서 screening 은 movie 에게만 message 를 던지고, movie 는 discount-condition 에게만 message 를 던지도록 의존성을 낮춘 것이다. 
- 이렇게 하는 경우 전체적인 결합도가 낮아지기에, 의존성이 낮아지고, 변화의 영향을 줄일 수 있으며, 재사용성을 증가시킬 수 있는 초석을 마련할 수 있다.
  - 해군 함정 내부에서의 수밀문을 생각하면 된다. 문이 여러개면 열고 닫기 귀찮아 지지만, 배에 물이 차는 경우 물이 들어오는 걸 격리할 수 있는 장치들이 많아진다.

## So, who creates?
- 어떤 메시지가 들어왔으면, 그 메시지를 처리해야 하는 책임을 가진 객체는 그걸 마무리 한 뒤 메시지에 대한 답신을 주어야 한다.
- 무소식이 희소식인 답신(return `void` type) 인 경우도 있지만, 요청한 것에 따른 결과물을 반환 해주어야 할 때도 있다.
  - 여기서는 결국 '영화를 예매해 줘' 라는 메시지에 대해서 다루고 있기에, '예매' 라는 결과물을 반환해 주어야 한다.
- 그렇다면, 어떤 domain object 가 이 결과물을 생성하고 반환해 주어야 할까?
- GRASP pattern 에서의 `CREATOR pattern` 은 아래와 같은 조건을 최대한 많이 만족하는 domain object 에게 그 결과물을 생성/반환하는 책임을 주어야 한다고 말한다.
  - 반환할 객체를 포함하거나 참조한다
  - 반환할 객체를 기록한다
  - 반환할 객체를 긴밀히 사용한다
  - 반환할 객체를 초기화 하는데 필요한 데이터를 가지고 있다 (즉, 반환할 객체의 정보 전문가이다)
- 영화 예매를 위해 우리가 만든 domain object 들 중 이 항목들을 가장 많이 만족하는 건 아무래도 `screening.ts` 이 아닐까?
  - 왜냐하면, screening 이 반환할 객체(가칭 `Reservation`)를 초기화하는데 필요한 데이터를 가지고 있는 정보 전문가이기 때문이다.