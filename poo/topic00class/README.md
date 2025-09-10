__Diagrama de clases__

```mermaid
classDiagram
    class Dog {
        -str espiecie
        -str name
        -str breed
        +bark() str
        +walk() str
    }

    class App {
        +main() None
    }

    App --> Dog : Association

    style App fill:
