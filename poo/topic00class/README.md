__Diagrama de clases__

```mermaid
classDiagram
    class Dog {
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
