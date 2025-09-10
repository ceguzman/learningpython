__Diagrama de clases__

```mermaid
classDiagram
    class Class01 {
        +normal_method()
        +@class_method()
        +static_method()$
    }

    class App {
        +main() None
    }

    App --> Class01: Association
