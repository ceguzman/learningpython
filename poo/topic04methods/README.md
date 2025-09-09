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

    Class01 --> App
    Class01 ..> App


