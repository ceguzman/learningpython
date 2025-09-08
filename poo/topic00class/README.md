__Diagrma de clases__

```mermaid
classDiagram
    class Dog {
        -name: str
        -breed: str
        +bark(): str
        +walk(): str
    }

    class App {
        +main(): None
    }

    App --> Dog : usa

