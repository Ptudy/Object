# Implementing movie reservation application with GRASP pattern

# Domain modeling as a draft for structuring
- 우리가 해결해야 할 문제를 영역으로 나누었을 때 어떻게 나누어지는지를 먼저 생각해본다. 
- 이 domain modeling 이라는 행위는 반드시 정확할 필요는 없다, 요구사항을 잘 반영할 수 있는 설계를 만들어낼 수 있는 model 이 좋은 model 이라는 마음가짐으로 접근 해야한다. 

# Thinking about the message at first
- domain model 의 각각의 domain 에서 협력이 일어날 때, 어떤 메시지가 오가는지를 먼저 생각한다. 
## reserve a movie
- '예매한다' 라는 메시지가 일단은 먼저 생각이 난다.
  - 주의해야 할 점은, 이 메시지에 대해서 생각할 때 메시지의 '송신자' 의 관점에서 생각해야 한다는 점이다.
