__Diagrma de clases__

```mermaid
classDiagram
  class Animal {
    <<Abstract>>
    +eat() str
    +die() str
    +reproduce() None*
  }

  namespace asexualy {
    class Sponge {
      +str specie
      +reproduce() str
    }
  }

  namespace sexualy {
    class Dog {
      +str specie
      +reproduce() str
      +barks() str
    }
  }

  class App {
    +main()
  }

  Animal <|-- Dog : Inheritance
  Animal <|-- Sponge : Inheritance
  Dog <-- App: Association
  Sponge <-- App: Association