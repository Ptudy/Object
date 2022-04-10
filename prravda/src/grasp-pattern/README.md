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