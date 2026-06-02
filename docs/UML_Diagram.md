# QuickServe Straight-Arrow UML Diagram

This diagram uses a strictly linear flowchart layout to ensure all relationship arrows are perfectly straight, while mapping out the core entities and relationships.

```mermaid
%%{init: {'flowchart': {'curve': 'linear'}}}%%
graph TD
    classDef entity fill:#1e293b,stroke:#10b981,stroke-width:2px,color:#f8fafc,text-align:left;
    classDef abstract fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#f8fafc,stroke-dasharray: 5 5;

    %% Entities
    U["**User (Abstract)**<br/>-------------------<br/>+ _id: ObjectId<br/>+ name: String<br/>+ email: String<br/>+ role: Enum"]:::abstract
    
    C["**Customer**<br/>-------------------<br/>+ browseServices()<br/>+ bookService()"]:::entity
    P["**Provider**<br/>-------------------<br/>+ offeredServices: List<br/>+ acceptBooking()"]:::entity
    A["**Admin**<br/>-------------------<br/>+ manageUsers()<br/>+ viewAnalytics()"]:::entity

    S["**Service**<br/>-------------------<br/>+ _id: ObjectId<br/>+ name: String<br/>+ price: Float<br/>+ category: Enum"]:::entity
    
    B["**Booking**<br/>-------------------<br/>+ _id: ObjectId<br/>+ status: Enum<br/>+ date: Date"]:::entity
    
    Pay["**Payment**<br/>-------------------<br/>+ _id: ObjectId<br/>+ amount: Float<br/>+ status: Enum"]:::entity
    
    R["**Review**<br/>-------------------<br/>+ rating: Integer<br/>+ comment: String"]:::entity

    %% Inheritance (Straight arrows)
    U -- Inherits --> C
    U -- Inherits --> P
    U -- Inherits --> A

    %% Relationships (Straight arrows)
    P -- "Offers (1 to Many)" --> S
    C -- "Makes (1 to Many)" --> B
    P -- "Receives (1 to Many)" --> B
    S -- "Included in (1 to Many)" --> B

    B -- "Requires (1 to 1)" --> Pay
    C -- "Writes (1 to Many)" --> R
    S -- "Has (1 to Many)" --> R
```
